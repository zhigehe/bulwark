---
title: "对 OpenAI 故障的思考｜如何让 Kubernetes 更稳定？"
date: "2025-01-16 10:50:36"
summary: "作者 | 阿里云容器服务高级技术专家 张维 (贤维)、阿里云容器服务技术专家 刘佳旭 (佳旭)从 O..."
categories:
  - "infoq"
lang:
  - "zh-CN"
translations:
  - "zh-CN"
tags:
  - "infoq"
menu: ""
thumbnail: "https://static001.infoq.cn/resource/image/a3/64/a39399444061bca921c1b22fca42e264.jpg"
lead: ""
comments: false
authorbox: false
pager: true
toc: false
mathjax: false
sidebar: "right"
widgets:
  - "search"
  - "recent"
  - "taglist"
---

作者 | 阿里云容器服务高级技术专家 张维 (贤维)、阿里云容器服务技术专家 刘佳旭 (佳旭)

从 OpenAI 集群故障谈起
---------------

2024 年 12 月 11 日，OpenAI 出现了全球范围内的服务不可用故障，影响了 ChatGPT，API，Sora 等服务，故障持续时间超过四个小时，产生了严重影响。根据 OpenAI 在事后发布的故障报告 [1] ，此次故障的直接原因是升级监控组件导致 Kubernetes 集群控制面过载，然后因为数据面 CoreDNS 对控制面有强依赖导致影响应用服务，进一步放大了故障影响。（请参考详细故障报告 [2]）

![]()https://static001.geekbang.org/wechat/images/89/89396cbd868b2658c52d690c74c0fd37.png![]()

近年来，无论是在国内还是国际，我们都见证了许多自建 Kubernetes 集群遭遇故障的案例，这些故障为从事容器基础设施管理的人员提供了宝贵的学习机会。

从 Kubernetes 集群管理的视角，此次故障中值得被关注的技术问题有：

* OpenAI 自建 K8s 集群的单集群规模很大。

* 一个部署在节点侧的 Telemetry services 更新后，对 K8s 集群 API 控制面压力过大，导致控制面崩溃。

* 其 CoreDNS 对 K8s 集群控制面有强依赖，导致数据面服务受损。

* K8s 集群控制面过载后无法操作集群，进而导致故障时间拉长。

OpenAI 针对此次故障提出了几点后续要做的预防工作，在此我们就这些点进一步展开分析，并分享 ACK 在这些方面的稳定性实践经验。

Kubernetes 稳定性基础实践 ：OpenAI 故障复盘
-------------------------------

1. 健壮的分阶段部署 - Robust phased rollouts
------------------------------------

历史数据表明，故障大部分是由于变更导致的。灰度变更是基础设施稳定性要求的重要原则，通过强化灰度发布与所有基础设施变更的监控，控制故障爆炸半径并能及早发现。生产环境的变更发布需要严格遵守流程规范，尽量做到可灰度、可观测、可回滚。这里既包括多集群之间的分阶段部署（所有变更应先应用于测试和预发环境，留有一部分时间进行观察），同时也要求单集群内的变更也要尽量遵守可灰度原则。

灰度的过程主要遵循爆炸影响从轻到重，规模从小到大的步骤。灰度除了阶段控制外，尤为需要注意的是与可观测系统的联动。

社区 DaemonSet 的版本变更不支持灰度和分阶段部署，因此在进行变更时需格外谨慎，并持续监测对集群控制面和数据面的影响。为了解决社区 DaemonSet 缺乏灰度能力的问题，阿里云推出的 OpenKruise Advanced DaemonSet [3] 实现了可控的灰度发布功能，并提供多种滚动更新策略，以提升 DaemonSet 变更的稳定性。

2. 紧急访问 Kubernetes 控制面 - Emergency Kubernetes control plane access
------------------------------------------------------------------

控制面过载时，需要确保控制面的可操作性，进行限流等干预手段。

这里一方面是需要有针对 Kubernetes 控制面过载场景的更好应急限流手段，ACK 内部支持根据 ua/user/verb 等 client 多维度进行限流设置，从而通过更有效的限流快速控制过载情况。

另一方面是整体架构的设计，不同于自建 Kubernetes 集群通常多个 Master 节点独立部署架构（Apiserver 和 etcd 通也通常被部署在一个节点上），ACK 托管控制面采用容器化管理方式，在控制面的动态弹性伸缩和应急场景的可操作性可维护性，都带来更好的控制面管理优势。可参考下面介绍的“**控制面架构形态选择**”。

3. 解耦数据面和控制面 - Decouple the Kubernetes data plane and control plane
-------------------------------------------------------------------

由于应用层依赖 Kubernetes DNS 进行服务发现，导致了与 Kubernetes 控制面存在耦合。在 Kubernetes 集群中数据面和控制面的解耦是一个重要的设计原则。在 ACK 环境中我们进行架构改造，使得 Kubernetes 数据面与控制面解耦。

除了 CoreDNS 依赖问题，其他 Kubernetes 应用也可能对控制面有强依赖。在此我们建议集群管理者应常态化对集群做故障演练，停止 Kubernetes 控制面以观察数据面业务服务是否有影响，包括服务间的 DNS 查询、Service 网络通信、服务响应等。（另外，ACK 提供 Managed CoreDNS 托管组件，降低用户对 CoreDNS 组件的稳定性管理负担）

ACK 不仅确保系统组件不对控制面有强依赖，同时对云服务整体架构上也是同样的原则。对 ACK 云服务自身的管控面和元集群控制面，我们也进行了常态化的演练，确保极端情况下这两者的异常不影响用户的托管 K8s 控制面。

4. 故障注入测试 - Fault injection testing
-----------------------------------

OpenAI 提到的故障注入测试与 ACK 持续开展的“**故障演练**”相对应。我们要强调，常态性的故障演练对维护基础设施的稳定性至关重要。ACK 通过在控制面和数据面持续开展故障演练，确保各层面的稳定性不降低，并不断增强快速恢复和应急处理的能力。故障演练体系的建设与实施并非一蹴而就，而是需要与日常研发和运维工作相结合，常态化实施，以实现对系统熵增的有效控制。

![]()https://static001.geekbang.org/wechat/images/81/81c61647b7262804c7bcb088e363569c.png![]()

针对 Kubernetes 体系产品，可以把可能的依赖故障拆解成以下几种类型。针对可能出现的依赖故障，逐步进行场景的设计，计划演练、常态演练甚至混沌演练，并且还需注意故障演练过程本身的风险控制如隔离准备、流量分离等。以下是一些分析入手的场景思路。

* 控制面核心组件如 Apiserver 等负载所在基础设施的底层计算、存储、网络不可用。

* 主要网络存储组件 controller、webhook 等负载所在基础设施的底层计算、存储、网络不可用。

* 用户集群节点层面 Daemonset 或 kubelet 出现 Crash 或 OOM 等；

* 用户应用负载所在基础设施的底层计算、存储、网络不可用等；

* 控制面不可用的情况下，数据面受损程度（应当不受损）；

* 各组件对外资源依赖服务不可用、或返回异常；

* 集群控制资源规模、请求到达上限，或在上限的情况下进行集群整体批量运维动作（节点批量增减、负载迁移、组件批量升级重启等）；

5. 更快的恢复 - Faster recovery
--------------------------

故障影响的衡量程度包括故障影响面和故障时长，通过更有效的应急可以快速控制故障时长，减少故障最终影响程度。这里可以通过常态化、场景化的故障演练持续提升快速恢复能力。

除了上述提到的稳定性实践外，我们注意到 OpenAI 采用了自建的大规模 Kubernetes 集群。借此机会，我们希望进一步探讨其他需要关注的 Kubernetes 稳定性问题和实践。同时，我们也将分享阿里云 ACK 在这一领域的思考与经验，以及自建 Kubernetes 集群与云服务提供商托管 Kubernetes 集群在长期管理上的一些差异。阿里云 ACK 已承载了数万个托管 Kubernetes 集群的控制面和数据面的全生命周期管理，积累了丰富的 Kubernetes 稳定性技术优化和实践经验，其中包含多个大规模集群的案例。

Kubernetes 的其他稳定性挑战和实践
----------------------

1. Kubernetes 技术复杂度高
--------------------

![]()https://static001.geekbang.org/wechat/images/20/2052f1665fbae339181296189a71483c.png![]()

K8s 控制面被视为 K8s 集群管理的核心“大脑”，其中包含了关键组件如 kv 数据存储 etcd、apiserver、scheduler 和 kube-controller-manager 等。尽管 Kubernetes 社区持续努力简化 K8s 的部署与管理，使得从零构建测试或学习环境变得相对容易，但长期维护和管理生产级 K8s 集群依然是一项极具挑战的工作。K8s 技术的复杂性较高，涵盖了多个领域，包括有状态组件 etcd 的 Raft 共识算法、Apiserver 的高可用性和缓存机制、证书管理等。当控制面出现异常时，往往需要具备专业知识和丰富经验的 K8s 技术专家，以便迅速定位和修复问题。

![]()https://static001.geekbang.org/wechat/images/41/41050be4be0d22b28723e8907e1737c0.png![]()

从另一个角度看，对于大部分集群管理者而言，是没有必要去了解 K8s 控制面和数据面技术细节的，而是更应该关注业务应用的部署和管理。

2. 控制面架构形态选择
------------

传统自建 K8s 集群中控制面是采用多 Master 节点部署架构，这种架构让控制面的管理维护变得复杂和繁琐，让控制面高可用、弹性伸缩、故障应急的应对都更加复杂。我们看到这种形态下很多 K8s 集群 Master 节点自从创建之后就没有进行实质性的管理，进而导致在突发异常等情况下故障恢复和影响变得无法控制。

ACK 托管版集群 K8s 控制面是采用容器化的部署和管理方式，容器化云原生架构管理是 Cloud Scale 的稳定性架构基础，相比自建 K8s 集群 Master 多节点方式，以容器部署的托管控制面天然具有高度可扩展、可伸缩性、单副本容灾迁移、可运维操作性、灵活性、自动化运维等优势。

* 面向韧性设计（Resistancy）

* 面向弹性设计（Elasticity）

* 面向自动化设计（Automation）

ACK Apiserver/etcd 等托管组件都作为 Pod 运行在 K8s“元集群”中的数据面节点池中，通过技术手段保障不同租户的控制面得以单元化完全隔离。

![]()https://static001.geekbang.org/wechat/images/6f/6f3c0930f499c2d9daf613afa181d9ce.png![]()

3. 高可用性挑战
---------

高可用设计是分布式系统的难题，K8s 控制面的高可用需要关注：

* etcd 的高可用（奇数节点，避免脑裂等）；

* 无状态组件（Apiserver/kube-scheduler 等）的高可用；

* 底层依赖资源和服务的高可用（ECS/SLB/OSS/ACR 等）

对于大部分集群管理者而言，保障控制面在各种异常场景下的高可用是一件非常有挑战的工作。

自建 K8s 集群控制面往往以多 Master 节点方式部署，在可用区异常时的自动或者手动容灾迁移都是相对复杂的。而 ACK 托管控制面是基于容器化架构部署，在可用区异常时容灾迁移过程是更加简单且高效的，其可直接基于 K8s 原生 Pod 高可用语义设置。（ACK 托管集群控制面的 SLA 是 99.95%，参考 ACK 集群高可用架构推荐配置 [4]）

* 多可用区的地域：所有托管组件均严格采用多副本、多可用区均衡打散部署策略，确保在单个可用区或节点发生故障时，集群仍然能够正常提供服务。

* 单可用区地域：所有托管组件均严格采用多副本、多节点打散部署策略，确保在单个节点发生故障时，集群仍然能够正常提供服务。

控制面高可用保障是体系化的系统能力建设，不仅需要有良好的架构设计、完善的自动化运维体系应对容灾迁移场景，也包括在很多异常场景下的深度技术优化。

举例，当底层网络出现故障时，比如某些可用区之间可能相互连通，而其他可用区却无法连通，这容易导致 etcd 出现网络分区问题（Network Partition），从而引发 etcd “no leader”的情况。结合 Apiserver 的 HTTP/2 长连接机制，这种网络分区问题进而会导致节点变为 NotReady 状态。目前社区对 etcd 的网络分区问题尚未提供完善的解决方案，而 ACK Apiserver 针对此场景中进行了深度优化，通过更可靠的检查机制自动排除“no leader”的 etcd 后端。参考 etcd 设计网络分区问题 [5]。

4. 大规模集群的可扩展性挑战
---------------

K8s 已成为 AI 应用的重要基础设施，OpenAI 和 Google Cloud GKE 的单集群规模也在不断扩大。（参考 OpenAI 7500 nodes[6]，GKE 65K nodes [7]）

![]()https://static001.geekbang.org/wechat/images/cc/cce39d8cd1179e01c70b0871125776bb.png![]()

K8S 官方建议的最大集群规模是 5000 节点。然而，我们并不推荐自建 K8s 环境的用户将单集群扩展到如此大规模。但对于大多数集群管理者来说，确保大规模 K8s 集群控制面的稳定运行面临诸多挑战。例如，集群中大量节点的 kubelet、kube-proxy 和 DaemonSet 发起的 list-watch 请求可能会对控制面造成巨大压力，甚至引发服务风暴。而在 OpenAI 近期的故障中，正是由于 DaemonSet pod 产生的过载请求成为触发点。此外，K8s 在容器生态中作为分布式系统的 Universal Control Plane，尤其是在频繁使用自定义资源（CR）时，更容易导致控制面的崩溃。一旦控制面过载，客户端的重新连接请求会进一步加剧雪崩效应，OpenAI 的故障再次凸显了这一问题的严重性。

针对大规模场景，ACK 对 K8s 控制面进行了多方面的技术优化，以提升控制面的可扩展性。

* **控制面动态伸缩**：Apiserver/etcd 通过弹性伸缩自适应集群规模，根据组件资源水位进行动态 HPA/VPA。

* **Apiserver 限流增强：**

* 基于 QPS 的 ua limiter 限流：这种限流策略生效不依赖访问业务集群 Apiserver，过载场景下可根据配置策略快速阻止控制面流量。在 OpenAI 案例中这种限流能力对于故障恢复就会显得非常重要。

* 动态 APF 限制：ACK 集群默认支持标准 APF 限流能力，但社区 APF 限制不支持动态感知能力，在很多场景不是最优的限流策略。ACK Apiserver 根据资源水位动态调整 APF 最大并发限制。

* **Apiserver 关键优化：**

* 提供组件的最优参数配置，并针对不同规模的集群设定相应参数。

* 优化 protobuf 和 json List 开销，提升 List 查询性能。

* 减少 Apiserver 推送 watch 事件的延迟。

* 降低数据面组件的 watch 请求，例如关闭 kube-proxy 对 headless service 的 watch，以节省网络带宽。

* **Etcd 关键优化：**

* Data 和 Event etcd 分拆：Data 和 Event 存放到不同的 etcd 集群，数据和事件流量分离，消除事件流量对数据流量的影响。

* 自动碎片整理（AutoDefrag）：etcd operator 监控 etcd db 使用情况，自动触发碎片整理，降低 db 大小，提高查询速度。

* etcd 内核增强：对热点 key 和大象 key 进行跟踪监控。

* Raft 积压问题优化：优化大规模集群中常常出现的 raft 积压问题。

通过这些技术优化，ACK 能够平稳支持线上大规模集群的稳定运行，在某些场景下单个集群可承载 15K 节点和 5 万 ECI Pod。如需了解更多规模化集群的实践，请参考 ACK 大规模集群使用建议 [8]。

5. 持续运维的挑战
----------

K8s 集群的管理是一个长期且持续的复杂任务，贯穿集群的整个生命周期，生命周期内需要持续的监控、更新和升级。

**a. Kubernetes 版本升级**

K8s 的设计决定了在升级时默认不支持回滚到低版本，如何在确保集群稳定运行的前提下，平滑的升级自建 K8s 控制面，是集群管理者面临的一项重大挑战。

这几年我们常常看见业界自建 K8s 集群出现多起升级故障，而云上 K8s 托管集群基本没有见到类似的故障报告，其关键原因可以总结为两点：

* 自建 K8s 集群 Master 节点的升级复杂度是远远高于容器化管理的托管 K8s 控制面升级。自建集群以多个 Master 节点依次升级，每个 Master 节点内部需要做的升级操作复杂度较高，不仅要考虑各种 Manifest 文件的配置覆盖，也需要考虑 etcd 版本升级，还需要考虑 Master 节点 kubelet 的升级。而因为托管 K8s 控制面简洁的容器化管理架构，其升级过程是极大简化的，这种架构层面的简化会大大提升 K8s 控制面升级的稳定性。

* 云厂商提供更完善的产品化机制保障升级可靠性。云厂商对于 K8s 升级的可靠性极度重视，相比自建 K8s 集群，会提供更严谨更完善的升级前置检查体系，包括组件兼容性检查、废弃 API 检查等，提供让用户无感的自动 etcd 数据备份机制。另外 ACK 提供自动升级能力，进一步降低 K8s 升级的负担。参考 ACK 版本机制 [9] 和 ACK 自动升级 [10]。

**b. Kubernetes 可观测性系统**

Kubernetes 可观测性（Observability）是集群管理的重要基础能力，它使集群管理者能够检查服务的可用性和可靠性、进行故障诊断与排除、优化性能以及进行容量规划等。由于 K8s 环境的动态性和复杂性，构建一个独立的可观测性系统并进行持续监测的难度较大。ACK 在如何构建一个稳定的 K8s 可观测性系统方面有几点长期实践经验。

**c. 证书过期和轮转**

证书过期是 K8s 环境常见的故障原因，K8s 证书体系本身较为复杂，有 Apiserver 证书、etcd 证书、kubelet 证书、集群 CA 证书、kubeconfig 凭据等，这里一方面要求集群管理者需要无遗漏的进行全集群证书可用性监控，另一方面要求能够平滑稳定的进行证书轮转操作。云厂商托管 K8s 集群会全面负责这些基础证书管理，而不用用户关心。而在自建 K8s 集群中需要用户重视证书的管理问题。

6. 安全性的挑战
---------

在云计算行业，安全作为一个横向技术领域，需要企业投入较大的成本构建和培养同时具备云原生 K8s 和云安全等多个专业领域知识的安全运维团队。在 K8s 控制面安全方面，企业安全运维需要遵循最佳安全实践配置集群控制面参数，同时持续监控和应对 CVE 漏洞、并处理 kubeconfig 凭据和密钥的生命周期管理、以及是否最小化授权等安全问题。此外企业还需要基于 DevSecOps 原则构建内部供应链安全，保证企业应用从开发构建到部署运行的生命周期中，每一步的关键流程都是在安全规范的指导下进行，并满足行业合规要求。

7. 基础设施稳定性和安全性的责任共担
-------------------

在云上托管 Kubernetes 集群的基础设施稳定性和安全性中，云厂商与用户的责任是相辅相成、不可分割的。云厂商负责提供可靠的基础设施、全面的安全保障以及高可用性的服务架构，以确保集群的运行环境稳定、弹性和安全。用户则需合理正确的对集群进行配置、监控和管理，实施最佳实践，及时更新维护集群和应用，应对潜在的安全威胁和性能瓶颈。在这种共担责任模型中，才可实现高效稳定的 Kubernetes 集群环境，最大程度地提升业务的连续性与可靠性。

![]()https://static001.geekbang.org/wechat/images/58/58f71871c051ac8dcaba18bfc5e5ff39.png![]()

写在最后
----

Kubernetes 已成为云原生时代的重要基础设施，管理庞大复杂的基础设施从来都不是一件容易的事情。很多领先的技术型公司，也曾遭遇自建 Kubernetes 故障。在超大规模 Kubernetes 集群运维管理工作进入深水区的过程中，所有企业都面临着相同的故障风险和技术难题。

“Complexity has to live somewhere.” （复杂度是不灭的，只会转移）

云计算提供商在服务千行百业的客户过程中，一直在努力实现技术突破和积累工程化经验，并将这些突破和经验转化为标准化的产品服务。通过降低企业客户的运维复杂度，减少各类故障并帮助客户缩短业务恢复时间和降低影响程度，让企业能够更加关注业务创新。对于大部分企业，云服务或许是一个更优选择。

同时，经验的积累没有压缩算法。云计算也在经验中成长，努力为客户提供更稳定的基础设施服务，谨以此文与大家共勉。

**相关链接：**

[1] 故障报告https://status.openai.com/incidents/ctrsv3lwd797

[2] 详细故障报告https://status.openai.com/incidents/ctrsv3lwd797

[3] OpenKruise Advanced DaemonSethttps://openkruise.io/docs/next/user-manuals/advanceddaemonset/

[4] ACK 集群高可用架构推荐配置https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/cluster-high-availability-architecture-recommend-configuration

[5] etcd 设计网络分区问题https://etcd.io/docs/v3.5/learning/design-client/

[6] OpenAI 7500 nodeshttps://openai.com/index/scaling-kubernetes-to-7500-nodes/

[7] GKE 65K nodeshttps://cloud.google.com/blog/products/containers-kubernetes/gke-65k-nodes-and-counting

[8] ACK 大规模集群使用建议https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/suggestions-on-how-to-work-with-large-ack-pro-clusters

[9] ACK 版本机制https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions

[10] ACK 自动升级https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/automatically-upgrade-an-ack-cluster

[infoq](https://www.infoq.cn/article/SiC0YrEuk0pbCwPavWb2)
