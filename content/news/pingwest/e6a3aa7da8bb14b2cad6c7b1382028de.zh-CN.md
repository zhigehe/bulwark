---
title: "OpenAI 推 Deep Research：复刻Google、“致敬”DeepSeek，啥也不管了就是追"
date: "2025-02-04 11:30:48"
summary: "刚推出o3-mini的OpenAI没闲着，昨天又马不停蹄地发布了一个新东西：能为用户独立工作的AI..."
categories:
  - "pingwest"
lang:
  - "zh-CN"
translations:
  - "zh-CN"
tags:
  - "pingwest"
menu: ""
thumbnail: ""
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

刚推出o3-mini的OpenAI没闲着，昨天又马不停蹄地发布了一个新东西：能为用户独立工作的AI研究助手**「Deep Research」**。

Deep Research 是 ChatGPT 内嵌的一款增强工具，专为自动化复杂的在线多步骤研究任务而设计。不光中英文名字跟DeepSeek高度相似，就连功能也颇为相近：

用户只需输入提示，它就会在互联网上快速搜索、分析并整合上百个信息来源，最终生成质量媲美专业研究分析师的综合报告。

原本人类需要数小时完成的研究工作，Deep Research 在短短几十分钟内即可完成。其目标用户覆盖金融、科学、政策和工程等领域的专业人士。像是解读10-K财报、分析实验数据、研究法律案例、检索技术文档等复杂任务。同时也适用于需要精细研究的消费者。当购买汽车、电器、家具等高价值商品难以抉择时，Deep Research 就会提供高度个性化的消费建议。

![](https://cdn.pingwest.com/portal/2025/02/04/jy85ATmTFF7fSW30zBwGQKfb68R7tzaH.png?x-oss-process=style/article-body)

优化版o3驱动 + 端到端RL训练
-----------------

官方介绍，Deep Research由一个**优化版的 o3 模型**驱动，专注于网页浏览和数据分析，并基于**端到端强化学习(RL)**进行训练。它能做到在互联网上跨模态搜索、解读和分析大量文本、图片及 PDF 文件，同时根据实时信息动态调整搜索策略。

除网络搜索外，它还可以分析用户上传的文件并提取关键内容；使用Python工具制作数据可视化图表，将这些图表和网站抓取的图片整合到回复中；为了保证研究结果的可靠性，系统也会严格标注信息来源，精确引用原文中的相关段落。

怎么用，谁能用？
--------

Deep Research 的使用非常简单：在 ChatGPT 界面选择“Deep Research”模式后，输入研究需求即可。如果有具体的参考资料，也可以直接上传文件提供更多上下文信息。

整个研究过程会在侧边栏实时显示进度和参考来源，通常耗时 5 到 30 分钟。这期间用户可以先去处理其他事务。研究完成后，系统会通知查看报告。未来几周内还将支持在报告中展示图表等可视化内容，提升阅读体验。

与注重实时多模态对话的 GPT-4o 相比，Deep Research 专注于深度研究，不仅能广泛收集信息，还会为每个结论附上详细的源头依据，最终生成一份完整且经过验证的研究成果，直接满足工作需求。

下面是一个OpenAI官网示例，展示用Deep research生成“零售业三年变革”报告的工作过程。值得注意的是，获得指令后它还主动要求用户澄清地域范围与关注维度，体现出类人交互能力。

只是由于Deep Research的计算需求非常高，查询耗时越长，所需的计算资源就越大。所以目前仅优先提供 Pro 每月100次查询额度，预计一个月内开放给Plus、Team和Enterprise用户。

OpenAI 还计划推出更快、更具成本效益的小型模型版本。未来允许连接到更专业的订阅数据源，使输出更加可靠和个性化。以及与能自动操作计算机的Operator结合，实现“行动—研究”闭环。

和DeepSeek比谁赢了？
--------------

说起来，OpenAI这款Deep Research由于命名与DeepSeek相似，又颇有赶着出来反击的意味，着实被广大推特网友调侃了一番。还预测今后各大模型厂商都要调转矛头，开启Deep系列了。

不过与其说 OpenAI此次的灵感来源于DeepSeek，倒不如说直接做了Google的伸手党。去年12月，Gemini订阅版本里就集成了「Gemini 1.5 Pro with Deep Research 」功能，同样是一款帮用户深度研究的智能体，也具备联网和上传文件的能力，只是底座模型并非推理模型。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/Q7WAM6za7163Dn318G6t47scMEZpZXJB?x-oss-process=style/article-body)

鉴于大家都关心OpenAI Deep Research与DeepSeek R1“深度思考+联网功能”的技术对比。我们直接拿这个问题去问了该模式下的DeepSeek，得到以下这张表格：

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/rwyPP4ywx7Z73Z3632cQxaHZbf5JHP34?x-oss-process=style/article-body)

可以看出，两者在几大维度上各有侧重和优缺。**Deep Research 适用于深入分析、长时推理和动态调整，尤其擅长专业级研究、商业报告和复杂数据解析。DeepSeek 更适合快速推理、代码生成和数学计算，主要面向开发者、学习者和基础信息检索。**

然而，Deep Research 真正的突破点，以及几项在基准测试上超过 DeepSeek 的关键优势，并未在上表中被突出展示——即 **HLE、GAIA** 和 **Expert-Level Tasks**。

这都是什么意思？

**HLE （Humanity’s Last Exam）**翻译为“人类终极测试”，涵盖 100 多个学科，从语言学到航天科学、从经典文学到生态学，总计超过3,000道多选题和简答题。旨在评估AI表现是否达到人类水平。测试时会让AI和人类专家完成相同的任务，然后比较他们的表现，看看AI的输出质量是否能够媲美人类专家。

在这项测试中，Deep Research准确率高达26.6%，横扫包括o3-mini-high（得分13%）和Deep Seek R1（得分9.4%）在内的一切竞争对手。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/n8T3sy7KB6XSyEksm8xRHtsxCE2y4tt3?x-oss-process=style/article-body)

**GAIA** 测试用于评估 AI 处理现实世界问题的能力。涵盖三个难度等级，要求 AI 具备推理、多模态理解、网页浏览和工具使用等能力才能成功完成任务。这里Deep Research 达到了当前最先进水平，并登顶外部排行榜。

![](https://cdn.pingwest.com/portal/2025/02/04/59SJyQm4Gs527KP3beG7d3G34kMzRmif.png?x-oss-process=style/article-body)

不好理解的话，可以看下面这个官方挂出的level 3示例感受一下：

“1959 年 7 月 2 日，美国发布了加工水果、蔬菜及某些脱水类产品的等级标准。其中，“干燥和脱水”类别下明确标注为“脱水”的项目，以及“冷冻/冷藏”类别中完整名称包含该产品但未标注为“冷藏”的项目均适用该标准。截至 2023 年 8 月，这些标准中已有多少百分比（四舍五入到最接近的整数）被新版本取代？”——是不是觉得读明白都有困难…

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/zzmxMKbmr188GpJbbQfNZAZ3s66Tnn_G?x-oss-process=style/article-body)

Deep Research在完成识别 1959 年标准、收集相关标准、查找更新版本、评估更新比例、验证与补充这些思考步骤后，得出6/7的标准被取代。

有推特用户为了验证它的综合能力提出一系列问题，从总结历史到分析小说，再到研判财务违规，DeepSeek都回答得不错。但也提到Deep Research有一定限制，比如引用不完全，没有暂停按钮。但瑕不掩瑜，这仍然是“人类与AI协作的巅峰”。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/Y6jTM6XN3cJ4exc1sa3i4w681mXzMR2a?x-oss-process=style/article-body)

再来是**Expert-Level Tasks**。在内部评估中，Deep Research 获得领域专家认可，能够自动化完成复杂的研究任务，将原本需要数小时的手动调查大幅缩短。这一能力使其被认证为专业领域的重要辅助工具，为专家级研究提供高效支持。

杰克逊实验室和前纽约大学教授、人类免疫学家Derya Unutmaz使用Deep Research撰写了一份25页的癌症研究专利，表示质量完全过关，省下1万美元费用。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/3d37xYj_zi73K50ndQ_37PB4B558w3X5?x-oss-process=style/article-body)

还转发了Deep Research媲美专业会计师的案例：一位即将搬离美国的用户，通过它获得了一份详尽的税务优化、法律和遗产规划建议，而这些问题连自己的CPA都没有解决。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/c7EisETrkmeT8xyET6rh3Nc35ewaTjH8?x-oss-process=style/article-body)

Runway.com首席执行官Siqi Chen分享使用Deep Research研究女儿颅咽管瘤治疗方案的价值，已经超过了支付给私人研究团队的15万美元。

![](https://cdn.pingwest.com/portal/2025/02/04/7fcG5C6836ecZY1Ay_yZ7Q812biwFb3Q.png?x-oss-process=style/article-body)

当然，必须有人用Deep Research写了一份DeepSeek的研发历史，并对未来发展做出推断。洋洋洒洒几千字下来，评论是：“疯狂”。

![](https://cdn.pingwest.com/portal/2025/02/04/portal/2025/02/04/WtAZr4crGQrFi5hHc4R6d68s_6h6R638?x-oss-process=style/article-body)

局限与未来
-----

OpenAI表示，尽管Deep Research解锁了许多新功能，但仍处于早期阶段，存在一些局限性。包括幻觉问题（可能捏造事实或错误推断）、难以区分权威信息与传言、可信度校准不足、以及报告和引用格式上的轻微错误，同时某些任务的启动时间可能较长。不过，随着用户使用量的增加和模型的持续优化，这些问题有望在短时间内显著改善。

现在推特上的ChatGPT Pro用户评论区底下，已经有大批网友排队问问题，期待帮忙用Deep Research来解答了。可以想象，等这项功能向Plus用户开放后，OpenAI优化算力基础设施有多么迫在眉睫。在推理模型的进化带动下，AI辅助工具的发展正在从简单的对话助手，逐步向专业研究助手转变。

OpenAI这一波发力，是否从DeepSeek那儿赢回一些好感，能撬动用户的付费意愿了吗？

但这还没结束，Sam Altman已经透露，Deep Research并不是o3-mini的one more thing，过几天还有惊喜。

如果DeepSeek真地能让OpenAI重新支棱起来，对于用户来说，倒也不是一件坏事。

![](https://cdn.pingwest.com/portal/2025/02/04/e5rGBZRR6fbH6fs7Tr76ns_63_WE67p8.png?x-oss-process=style/article-body)

[pingwest](https://www.pingwest.com/a/302108)
