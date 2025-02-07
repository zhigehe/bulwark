---
title: "GMI Cloud 上架基于英伟达 H200 的 DeepSeek 系列模型！"
date: "2025-02-07 01:18:53"
summary: "1 月下旬，DeepSeek 推出性能媲美 OpenAI o1 模型的推理模型 R1，不仅成本远低于..."
categories:
  - "infoq"
lang:
  - "zh-CN"
translations:
  - "zh-CN"
tags:
  - "infoq"
menu: ""
thumbnail: "https://static001.infoq.cn/resource/image/8b/7c/8b84195dfda727c3af7a57e8yy1de17c.jpg"
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

1 月下旬，DeepSeek 推出性能媲美 OpenAI o1 模型的推理模型 R1，不仅成本远低于 o1 而且还开源，API 付费价格也远低于 o1，一经发出，立刻引起了 AI 圈的广泛关注。

一周后的除夕当天，DeepSeek 再次推出并开源了多模态人工智能模型 Janus-Pro，一款基于 DeepSeek-LLM-1.5b-base 和 DeepSeek-LLM-7b-base 构建的模型。在这系列模型中，Janus-Pro-7B 在 GenEval 和 DPG-Bench 基准测试中，在文本生成、语义理解、知识问答等关键任务上，击败了 OpenAI 的 DALL-E 3 和 Stable Diffusion，直接将国内外 AI 狂欢推向高潮。

据悉，DeepSeek 在 GitHub 开源后，代码库快速吸引大量开发者关注，star 数短期内突破十万，且众多基于 DeepSeek 的二次开发项目如代码自动补全、智能文档摘要等，已在金融、医疗、科研等多领域实现高效部署，有力推动了 AI 应用的创新与落地。

而在这个过程中，GMI Cloud 技术团队第一时间在北美完成了对 DeepSeek R1 基于英伟达当前量产最强的 H200 GPU 服务器的部署适配和优化，构建了专属 DeepSeek - R1 推理端点！

为了让更多 AI 企业进行体验，GMI Cloud 本周正式推出限免体验 2 天活动！识别下方二维码，即刻获取体验资格，完成一键部署！

![]()https://static001.geekbang.org/infoq/bc/bcbde218384a992bf78f44b7c9d0335e.webp![]()

技术细节
----

**模型提供商**：DeepSeek

**模型名称**：DeepSeek-R1

**类型**：聊天模型

**参数**：6850 亿

**部署方式**：专用端点（可动态扩容）

**量化方式**：FP8

**上下文长度**：该模型在单个会话中，能够处理 128,000 tokens

此外，GMI Cloud 还提供以下模型：

**DeepSeek-R1-Distill-Llama-70B**

**DeepSeek-R1-Distill-Qwen-32B**

**DeepSeek-R1-Distill-Qwen-14B**

**DeepSeek-R1-Distill-Llama-8B**

**DeepSeek-R1-Distill-Qwen-7B**

**DeepSeek-R1-Distill-Qwen-1.5B**

敏捷部署
----

1、与GMI Cloud 建立链接

2、创建模型包

3、部署

SDK部署示例：

![]()https://static001.geekbang.org/infoq/67/6791f368e02b5c1136cbadbd395807de.webp![]()

关于 GMI Cloud
------------

由 Google X 的 AI 专家与硅谷精英共同参与创立的 GMI Cloud 是一家领先的 AI Native Cloud 服务商，拥有遍布全球的数据中心网络，**为企业 AI 应用提供最新、最优的 GPU 资源，为全球新创公司、研究机构和大型企业提供稳定安全、高效经济的 AI 云服务解决方案**。GMI Cloud 凭借高稳定性的技术架构、强大的GPU供应链以及令人瞩目的GPU产品阵容（如拥有AI 强大算力的H100；能够精准平衡AI 成本与效率的H200；以及未来即将上线的具有卓越性能的GB200等），确保企业客户在高度数据安全与计算效能的基础上，高效低本地完成 AI 落地。

[infoq](https://www.infoq.cn/article/YzAkBt4K0Zw3S2j1oV9c)
