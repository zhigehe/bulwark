---
title: "Gitpod Flex，替代 Kubernetes 的云开发环境"
date: "2025-01-21 08:00:00"
summary: "Gitpod 是一个云开发环境平台。在经过六年的使用和试验后，他们最近决定放弃 Kubernetes..."
categories:
  - "infoq"
lang:
  - "zh-CN"
translations:
  - "zh-CN"
tags:
  - "infoq"
menu: ""
thumbnail: "https://static001.infoq.cn/resource/image/f0/f8/f0b850265d7fabd59461693ec37403f8.jpg"
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

Gitpod 是一个云开发环境平台。在经过六年的使用和试验后，他们最近决定放弃 Kubernetes。这一决定源于他们管理 150 万用户的开发环境，同时每天处理大量环境的经验。

Gitpod 的首席技术官兼联合创始人 Christian Weichel 和高级工程师 Alejandro de Brito Fontes 在一篇博文中详细阐述了这一决定的历程。Gitpod 发现，虽然 Kubernetes 非常适合生产负载，但用于开发环境时会带来重大挑战。

开发环境的天然性质也是这些挑战的成因。与生产负载不同，开发环境具有高度的状态性和交互性，开发人员深度参与其源代码和更改过程。它们显示出了不可预测的资源使用模式，需要复杂的权限和功能，通常需要 root 访问权限和安装各种包的能力。这些因素使开发环境不同于典型的应用程序负载，并为 Gitpod 的基础设施决策提供了灵感。

最初，Kubernetes 因其可扩展性、容器编排和丰富的生态系统而成为 Gitpod 基础设施的理想选择。然而，在扩展时，他们遇到了许多挑战，特别是在安全和状态管理方面。先是资源管理出现了挑战，每个环境的 CPU 和内存分配尤其成问题。开发环境中 CPU 需求激增的情况使得管理人员很难预测何时用户何时需要使用 CPU 时间，这还引发了平台对 CPU 调度和优先级进行的许多实验。

存储性能优化是另一个关键领域。Gitpod 尝试了各种设置，包括 SSD RAID 0、块存储和持久卷声明（PVC）。每种方法在性能、可靠性和灵活性方面都有其权衡。备份和恢复本地磁盘被证明是一项昂贵的操作，需要仔细平衡 I/O、网络带宽和 CPU 使用率。

自动扩展和启动时间优化是 Gitpod 的重要目标。他们探索了各种扩大规模和向前发展的方法，包括“幽灵工作区”、ballast pod，最后则是集群自动缩放器插件。镜像拉取优化是另一个关键方面，Gitpod 尝试了多种策略来加速镜像拉取，包括守护进程预拉取、最大化层重用和预烘焙镜像。

Kubernetes 中的网络引入了其自身的一系列复杂性，特别是在开发环境访问控制和网络带宽共享方面。安全性和隔离带来了重大挑战，因为 Gitpod 需要提供安全的环境，同时为用户提供开发所需的灵活性。他们实现了一个定制的用户命名空间解决方案来解决这些挑战，其中涉及很多复杂组件，例如文件系统 UID 转换、安装屏蔽进程和自定义网络功能。

Hacker News 上有一场与 Gitpod 之旅相关的有趣 对话。HN 用户之一 datadeft 在回复中引用了原始 k8s 论文并说，

为了寻找更好的解决方案，Gitpod 尝试了微型虚拟机技术，如 Firecracker、Cloud Hypervisor 和 QEMU。虽然这些技术提供了一些不错的功能，例如增强的资源隔离和改进的安全边界，但它们也在开销、镜像转换和技术特有的约束方面带来了新的挑战。

最终，Gitpod 得出结论，使用 Kubernetes 实现他们的目标是可能的，但在安全性和运营开销方面需要权衡。这种结论促使他们开发了一种新的架构 Gitpod Flex，它继承了 Kubernetes 的重要优势，例如控制理论和声明性 API，同时简化了架构并改善了安全基础。

Gitpod Flex 引入了与开发环境相关的抽象层，并去除了许多不必要的基础架构。这种新架构允许用户顺利集成开发容器，并能够在台式机上运行开发环境。它可以在任意数量的区域中快速部署自托管，从而更好地控制合规性并在建模组织边界时提供灵活性。

总之，Gitpod 的历程强调了系统选择决策的重要性。选择系统时，必须考虑其改善开发体验、降低运营负担和提高利润的能力，而不是简单地在 Kubernetes 和替代方案之间进行选择。要了解有关 Gitpod Flex 架构的更多信息，感兴趣的读者可以观看这个深度分享。

原文链接：

Gitpod Flex, Cloud Development after Kubernetes()

[infoq](https://www.infoq.cn/article/o0vBzBidAUlWyBltH2yd)
