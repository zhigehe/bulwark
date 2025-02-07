---
title: "Netflix 通过新的配置功能增强了 Metaflow"
date: "2025-01-24 08:00:00"
summary: "Netflix 对其 Metaflow 机器学习基础设施做出了一项重大改进：一个新的 Config（..."
categories:
  - "infoq"
lang:
  - "zh-CN"
translations:
  - "zh-CN"
tags:
  - "infoq"
menu: ""
thumbnail: "https://static001.infoq.cn/resource/image/f5/26/f5c6740fa39861c5b5f017e84cd8e126.jpg"
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

Netflix 对其 Metaflow 机器学习基础设施做出了一项重大改进：一个新的 Config（配置）对象，为 ML 工作流带来了强大的配置管理能力。这一新增功能解决了 Netflix 团队面临的一个共同挑战，他们管理着跨不同 ML 和 AI 用例的数千个独特的 Metaflow 流程。

Netflix Metaflow 是一个开源数据科学框架，旨在简化构建和管理数据密集型工作流的过程。它允许用户将工作流定义为有向图，这样就能很方便地对其可视化和迭代了。Metaflow 自动处理工作流的扩展、版本控制和部署操作，这是机器学习和数据工程项目中的核心工作。它为数据存储、参数管理和计算执行等任务提供了内置支持，既可以在本地也可以在云端执行操作。

![]()https://static001.geekbang.org/wechat/images/af/af7f057f1e4eeced13abf40944700d9c.png![]()

Metaflow 基础设施栈

新的 Config 特性代表了 Netflix 配置和管理 ML 工作流方式的根本性转变。虽然 Metaflow 一直擅长提供数据访问、计算资源和工作流编排的基础设施，但团队以前缺乏统一的方式来配置流程行为，尤其是对于装饰器和部署设置而言更是如此。

Config 对象加入了 Metaflow 现有的工件（artifact）和参数（parameter）的组合，但在时间执行上有一个关键的区别。虽然工件在每个任务结束时保留，参数在运行开始时解析，但 Config 会在流程部署期间解析。这种时间差异使 Config 在设置针对部署定制的配置方面特别好用。

可以使用人性化，容易看懂的 TOML 文件指定 Config，从而轻松管理流程的各个方面：

Netflix 的内部工具 Metaboost 展示了该配置系统的强大能力。Metaboost 是一个用于管理 ETL 工作流、ML 管道和数据仓库表的统一界面。新的 Config 功能允许团队在保持核心流程结构的同时创建不同的实验配置。

例如，ML 从业者只需交换配置文件即可轻松创建其模型的变体，从而快速试验不同的特性、超参数或目标指标。事实证明，此功能对于 Netflix 的内容 ML 团队特别有价值，该团队负责处理数百个数据列和多个指标。

新的配置系统提供了几个优点：

* 灵活的运行时配置：可以混合使用参数和配置来平衡固定部署和运行时的可配置性。

* 增强的验证：自定义解析器可以验证配置，还能与 Pydantic 等流行工具集成。

* 高级配置管理：支持 OmegaConf 和 Hydra 等配置管理器，可实现复杂的配置层次结构。

* 动态生成配置：用户可以从外部服务检索配置或分析执行环境（例如当前 GIT 分支），以在运行期间将其作为附加上下文包含在内。

这项增强功能代表了 Metaflow 作为机器学习基础设施平台发展的重要一步。通过提供更结构化的方式来管理配置，Netflix 让团队更容易维护和扩展他们的 ML 工作流程，同时遵循各自的开发实践和业务目标。

该功能现已在 Metaflow 2.13 中提供，用户可以立即开始在他们的工作流程中实现它。

一些类似 Netflix Metaflow 的工具也能帮助数据科学家和工程师管理工作流程、编排管道以及构建可扩展的机器学习或数据驱动系统。这些工具有着略微不同的需求和优先级，但它们都旨在简化复杂的工作流程和扩展数据操作。以下是一些值得一提的例子：

* Apache Airflow：一个广泛使用的开源工作流编排平台。它允许用户将任务及其依赖关系定义为有向无环图（DAG）。Metaflow 专注于数据科学管道，而 Airflow 则更通用，擅长管理跨不同领域的工作流。

* Luigi（Spotify）：一个旨在构建复杂管道的开源 Python 框架。与 Metaflow 一样，Luigi 能处理依赖项、工作流编排和任务管理，但它不太关注机器学习方面的特定需求。

* Kubeflow：Kubernetes 的机器学习工具包。它专门用于管理 ML 工作流并在生产中部署模型，使其成为基于 Kubernetes 的环境的不二之选。

* MLflow：一个管理 ML 生命周期的开源平台，包括实验跟踪、可重复性、部署和监控等能力。MLflow 对模型版本控制和部署有强大的支持，但缺乏 Metaflow 的更广泛的工作流编排功能。

* Argo Workflows：一个 Kubernetes 原生工作流引擎，旨在在容器化基础设施上运行复杂的工作流。对于已经在使用 Kubernetes 并正在寻找轻量级解决方案的团队来说，它是理想的选择。

虽然这些工具在某些功能上有重叠，但 Metaflow 凭借其简单性、可扩展性以及对机器学习工作流程的内置支持脱颖而出，这对数据科学团队来说特别有吸引力。

**原文链接：**

Netflix Enhances Metaflow with New Configuration Capabilities()

[infoq](https://www.infoq.cn/article/CPer5DmbjoI57uEzorlc)
