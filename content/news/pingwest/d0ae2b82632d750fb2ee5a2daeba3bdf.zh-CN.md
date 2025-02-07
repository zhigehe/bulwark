---
title: "Altman因DeepSeek“认错”：在开源上OpenAI站在了历史的错误一方"
date: "2025-02-01 10:30:49"
summary: "在开源上我们站在了历史的错误一方。这是Sam Altman对DeepSeek冲击做出的最新回应。O..."
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

在开源上我们站在了历史的错误一方。

这是Sam Altman对DeepSeek冲击做出的最新回应。

OpenAI从来都是主动出击，这一次因DeepSeek而被动调整了它自己的节奏，甚至第一次在开源权重的问题上，有了动摇。

一切都发生的太快了。

o3-mini全线开放，免费用，可联网
-------------------

在DeepSeek压力之下， OpenAI今天凌晨突然宣布，其最新推理模型**o3-mini全面上线**。

而且居然一改往日藏着掖着的调性，一次性向所有人开放了o3-mini在ChatGPT和API中的使用权限，**包括免费用户**。

不仅**支持联网**，也终于舍得展示思考过程了。

![](https://cdn.pingwest.com/portal/2025/02/01/7b75502AAm7niT8BwrsyXBzXaD_HZEJw.png?x-oss-process=style/article-body)

o3-mini 于去年底的技术直播中首次亮相，是 OpenAI 推理系列中最新、最具性价比的小型 AI 模型，在科学、数学和编程领域表现出色，同时兼具低成本和低延迟优势。

强度模式上，o3-mini提供了低、中、高三种选择，用户可根据需求在快速响应和深度思考之间灵活调整。只是o3-mini 尚不支持视觉任务，需要进行视觉推理时仍要调用o1。

此次发布，**ChatGPT Pro 用户可无限制访问 o3-mini**；**Plus 和 Team 用户**每日消息限制**从 o1-mini 的50条提升至150条**；**免费用户**也可通过**选择“Reason”模式或重新生成回复**来体验新模型（具体消息限制未说明）。所有付费用户还可在模型选择器中选择 “o3-mini-high”，以获得需要更长时间响应的更高智能版本。

此前曾被社区贴脸对比DeepSeek有而 OpenAI 没有的**深度思考 + 联网功能**，这次也高亮加入：所有用户均可选择 “Search + Reason” 组合，利用搜索功能查找带有相关网络资源链接的最新答案。

![](https://cdn.pingwest.com/portal/2025/02/01/k38x8K33MEm8zBbxhExc0Nna38jeCcHB.png?x-oss-process=style/article-body)

来到开发者这边。即日起，API 使用等级 3-5 的开发者可在Chat Completions API、Assistants API 和 Batch API 中调用o3-mini。OpenAI称它是自己首款支持函数调用、结构化输出和开发者消息的小型推理模型，可直接用于生产环境。

变快变便宜，但仍不如DeepSeek实惠
--------------------

速度与效率方面，o3-mini 相较于o1具备更快的响应速度和更高的计算效率。测试结果显示，o3-mini推理速度比o1-mini快24%，将平均响应时间从10.16秒缩短至7.7秒。此外，o3-mini 的首个token生成时间也比o1-mini快2500毫秒，为用户提供更加流畅的交互体验。

而面对“模型界拼多多”DeepSeek，OpenAI也不得不加入了价格战。官方表示，自 GPT-4 推出以来，OpenAI 已将每 token 价格下调 95%。

最新的定价方案中，o3-mini输入每百万tokens收费$1.10，输出每百万tokens收费$4.40，在使用缓存输入的情况下，费用可以减半至每百万tokens $0.55。

这个价格相比之前有了显著下降，比o1-mini低63%，比完整版o1更是降低了93%。然而即便如此，与DeepSeek R1输入和输出费用分别为每百万tokens $0.14和$0.55相比，仍然明显偏高。

![](https://cdn.pingwest.com/portal/2025/02/01/zYHaznbn8an71_5AJEYRt46MKTybnS53.png?x-oss-process=style/article-body)

性能超o1，采用“审慎对齐”技术
----------------

OpenAI在官方博客中展示了o3-mini在多个领域相比o1和o1-mini的性能提升。

**数学推理**方面，o3-mini于AIME 2024数学竞赛中表现优异。使用高推理强度时，其准确率达到87.3%，全面超越o1。即便在低推理强度模式下，其表现也能与o1-mini比肩。

![](https://cdn.pingwest.com/portal/2025/02/01/8437jnKyFKja8a2aXzs03fmRT4weJ7z8.png?x-oss-process=style/article-body)

在**科学领域**评测中，o3-mini的高推理强度模式在PhD级科学问题（GPQA Diamond）上达到79.7%的准确率，显著优于前代模型。在生物、化学和物理等高难度学科问题上，其高推理强度模式的表现与o1相当。

![](https://cdn.pingwest.com/portal/2025/02/01/6JPw9S3a73Wf4_RcyBe51sF5hjSGPM73.png?x-oss-process=style/article-body)

**编程能力方面，o3-mini这次展现出了肉眼可见的显著优势。**在Codeforces编程竞赛中，其高推理强度模式获得2130的Elo评分，远超前代模型，即使最低推理强度也与o1持平。在SWEbench-verified软件工程测试中，高推理强度模式达到49.3%的准确率。在LiveBench编程任务中，中等推理强度已超越o1-high，高推理强度模式则更是大幅领先。

![](https://cdn.pingwest.com/portal/2025/02/01/R4A1MBb_ZQWYW3P3PmthCh9cCzC324a3.png?x-oss-process=style/article-body)

在**一般知识评估**中，o3-mini全面超越o1-mini。同时，人类偏好测试显示，56% 的专家更倾向于选择 o3-mini 的回答，认为其更准确且逻辑性更强。此外，o3-mini 在处理现实世界高难度问题时，主要错误率下降了 39%，凸显了其在复杂任务中的可靠性。

**安全性方面**，OpenAI表示在o3-mini的安全性工作上取得了重要进展。最显著的是采用了他们开发的**审慎对齐”（deliberative alignment）**技术，让o3-mini能在回答用户问题前，主动对安全规范进行推理思考。这种方法使其在应对各种安全挑战和越狱测试时的表现明显优于GPT-4o。

为确保安全性，o3-mini采用了与o1同样严格的流程，包括准备度评估、外部红队测试 等多个环节。评估结果显示，o3-mini 的总体风险等级被评为 “中等”，其中在说服力、危险物质、模型自主性等方面风险为中等，而在网络安全领域的风险则为低。通过强化 “思维链”推理能力，o3-mini 在处理潜在风险场景（如非法建议和偏见回应）时达到了目前的最高安全水平。

![](https://cdn.pingwest.com/portal/2025/02/01/2Pp27381w2XfH3271xrj27t3SS8KkWM7.png?x-oss-process=style/article-body)

值得注意的是，随着模型能力的不断提升，OpenAI也意识到了潜在风险的增加。为此他们建立了完善的安全评估和防护体系，确保只有经过安全处理且风险达到中等或更低的模型才会被部署。

奥特曼领衔，OpenAI团队上阵Reddit开版答疑
--------------------------

o3-mini发布后，OpenAI CEO Sam Altman带领首席研究员Mark Chen、首席产品官Kevin Weil、工程副总裁Srinivas Narayanan、API 研究主管Michelle Pokrass，和o3-mini团队研究主管Hongyu Ren，上阵Reddit和网友们来了场互动Q&A。

![](https://cdn.pingwest.com/portal/2025/02/01/S681C2r8GNsS2M633XkbcMJx7E557mbf.jpeg?x-oss-process=style/article-body)

**下面是几个点赞排名靠前的问题：**

**问题1：**我们能看到所有的思维tokens吗？

**回答（Sam Altman）：**是的，我们将很快展示一个更有帮助和详细的版本。**感谢r1提醒我们。**

**问题2：**你们会考虑发布一些模型权重和发表一些研究吗？

**回答（Sam Altman）：**这个还在讨论中。我个人认为在这个问题上我们站在了历史的错误一方，需要找出一个不同的开源策略。不过不是所有OpenAI的人都同意这个观点，而且目前这也不是我们最高优先级。

**问题3：**完整版o3什么时候发布？

**回答（Sam Altman）：**我估计超过几周，少于几个月。

**问题4：**语音模式会更新吗？这是GPT-5o的一个重点吗？GPT-5o的大致时间表是什么？

**回答（Sam Altman）：**语音模式更新即将到来！我想我们会直接叫它GPT-5而不是GPT-5o。目前还没有时间表。

**问题5：**你们会推出基于4o的图像生成器吗？

**回答（Kevin Weil）：**是的！我们正在开发。而且我认为这值得等待。

**问题6：**你们计划在未来推理模型中会添加文件附件功能吗？

**回答（Srinivas Narayanan）：**正在开发中。推理模型未来将能够使用包括检索在内的不同工具。

**补充回答（Kevin Weil）：**我只想说，我迫不及待想看到带工具使用的推理模型了:)

**问题7：**Stargate的成功对OpenAI的未来有多重要？

**回答（Kevin Weil）：**非常重要。我们看到的一切都表明，计算能力越多，我们就能建立更好的模型，并制造更有价值的产品。我们现在同时在两个维度上扩展模型——更大的预训练和更多的强化学习/strawberry训练，这两者都需要计算资源。为数亿用户提供服务，并且随着我们转向更多为您持续工作的智能产品，这些也都需要计算资源。因此可以将Stargate视为我们的工厂，将算力/GPU转化为令人惊叹的产品。

目前，大部分评论区群众表示喜闻乐见，“打起来了，爱看，多发！”

![](https://cdn.pingwest.com/portal/2025/02/01/BY18k4HFejHWY_PW8H2Q2aSA7F48Msx4.png?x-oss-process=style/article-body)

编程软件Cursor算是手快的，最新两条推文相继宣布DeepSeek模型和o3-mini都已经整合进来，但对平台的开发人员们仍然最爱Claude Sonnet“表示很惊讶”。

![](https://cdn.pingwest.com/portal/2025/02/01/83Dh66P93kww7cMEBt7E51Th3yfzXd2e.png?x-oss-process=style/article-body)

当然也有人表示，既然DeepSeek已经免费提供这些尖端AI技术了，为什么要花钱升级GPT呢？

![](https://cdn.pingwest.com/portal/2025/02/01/bEF7ixwHf2iP6AC773c7bCy7sP7YPe2H.png?x-oss-process=style/article-body)

就像Lex Fridman说的，“OpenAI o3-mini是一个很好的模型，但DeepSeek R1的性能相似还更便宜，并且展示推理过程（目前大家反映o3-mini并没像奥特曼说的那样看到思维链显示）。

**尽管更好的模型将会出现（迫不及待地想看 o3pro），但「DeepSeek 时刻」是真实存在的。我认为 5 年后它仍将作为科技史上的关键事件被人们铭记。**”

![](https://cdn.pingwest.com/portal/2025/02/01/3r9KxK73ZH873P3BWG89KeA_zS3MF57h.png?x-oss-process=style/article-body)

[pingwest](https://www.pingwest.com/a/302095)
