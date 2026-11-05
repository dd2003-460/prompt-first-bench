# ScientistTwo vs pfb — 对比调研（2026-11-05）

> 来源：小红书帖 → arXiv:2609.19644 "ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI"（Google Cloud AI Research，Jaehyun Nam, Jinsung Yoon 等，2026-09-17）。
> 项目页：scientist-two.github.io。代码未开源（评论区确认"代码都没有开源"）。

## 一句话定位差异

- **ScientistTwo**：自主科研执行系统——给一个顶会论文级别的研究问题，它自己找短板、提假设、写代码跑实验、做消融、写论文、模拟同行评审+申诉答辩，直到过接收线。产出 = 86 篇可发表论文 + 可复现代码。
- **pfb (prompt-first-bench)**：流程评测基准——测"prompt-first 研究流程（分解/检索/交叉验证/结构化输出）到底有没有提升模型表现"，用 6 个复杂度递增的臂 × 5 道调研题 × 双评委打分。产出 = 关于"什么流程组件有效"的证据。

**本质区别**：ScientistTwo 是"选手"（做研究），pfb 是"裁判+训练方法学"（测哪种训练方式有效）。两者不在同一层，但互相需要。

## 关键指标对比

| 维度 | ScientistTwo | pfb (T17 stage-ablation) |
|---|---|---|
| 任务类型 | 开放式研究（超越人类 SOTA） | 固定调研题（有 gold answer） |
| 规模 | 107 题（ICLR/ICML/NeurIPS 录用论文） | 5 题（GPU 硬件调研）×3 run |
| 底座模型 | Gemini 3.6 Flash + Claude Opus 4.8（前沿闭源） | qwen3.8-27b（本地开源） |
| 成功判据 | 超越人类 SOTA（80.4%）+ AI 评审过线 | 流程组件的边际贡献（H1-H4 假设检验） |
| 评审 | ScholarPeer（91.9% 接收）+ Stanford Agentic Reviewer（72.1%，所有基线 0%） | 同族 27B judge + 异族 GPT judge |
| 完整性审计 | 4/4 通过：分数可复现、无规格违反、1814 条引用 0 幻觉、方法与代码逐行匹配 | M5 来源锚定率 + M7 矛盾推理（规则判分） |
| 代码 | 每篇论文配完整可运行 codebase | 评分器/门禁/gold 全部开源在仓内 |
| 成本 | 未公开（估计极高：全量实验+多轮评审迭代） | 90 runs × 27B 本地推理 ≈ 数小时 GPU 时间 |
| 单篇周期 | ~2.5 天/篇 | 不适用（bench 不是生产系统） |

## ScientistTwo 的架构（6 个 agent 组闭环）

1. **Idea Generator**：分析目标论文的局限 → 生成改进假设 → 新颖性筛选
2. **Evaluator**：小数据集子集快速筛选（subset-first，省算力）→ 全量多指标验证
3. **Analyzer**：自动设计消融实验 → 隔离各组件贡献 → 剪枝无效改动
4. **Writer**：撰写会议格式论文
5. **Peer-Review + Rebuttal**：评审 agent 批判草稿；申诉 agent 不是改文字而是设计新实验、写代码、跑出来再回应
6. **Meta-Review**：监督整个循环，不达标就重新触发精炼

闭环特征：实验结果、消融结论、评审意见全部反馈回假设迭代。

## pfb 相对 ScientistTwo 的优势

1. **测量严谨性**：pfb 的核心贡献是发现"judge identity 翻转结论"（同族 +0.129 vs 异族 -0.187）——ScientistTwo 用两个 AI 评审都报高分，但没有检验评审本身是否可靠。pfb 证明：**没有独立于被评系统的评审，任何"AI 评分"都可能自证清白**。
2. **可复现性**：pfb 的 gold answer、评分器、门禁逻辑、原始数据全部在 git 仓里，任何人可以重跑。ScientistTwo 代码未开源，只能看生成的论文 PDF。
3. **流程归因**：pfb 做的是消融式归因（哪个组件贡献多少），ScientistTwo 整体报 80.4% 但不拆"idea generation 贡献多少 vs ablation 贡献多少 vs rebuttal loop 贡献多少"。
4. **低成本可及**：27B 本地就能跑 pfb，不需要 Gemini/Claude 级 API。
5. **M7 矛盾推理维度**：pfb 新增了"建模/矛盾推理"评分维度，能区分"搜得多"vs"想得深"——ScientistTwo 的评审只打总分，不测这个。

## ScientistTwo 相对 pfb 的优势

1. **端到端能力**：从问题到可发表论文+代码，pfb 只到"回答质量评分"。
2. **计算效率策略**：subset-first 筛选（先小子集筛掉差 idea 再全量跑）——pfb 没有这种分层验证机制，每个臂每题都跑满。
3. **评审闭环深度**：Rebuttal Agent 会设计新实验来回应质疑（不是文字修改），这比 pfb 的"一次评分"深得多。
4. **完整性审计**：1814 条引用 0 幻觉 + 方法-代码逐行匹配 + 分数复现——pfb 的 M5 只测"数字有没有来源锚定"，没做到"引用存在性验证"和"代码-方法一致性"。
5. **规模与领域覆盖**：8 个 AI 领域 × 107 题 vs pfb 的 5 道 GPU 题。
6. **前沿模型**：Gemini 3.6 Flash + Claude Opus 4.8 的能力上限远高于 27B。

## 填补空白点（双方各自的盲区）

| 空白 | 谁该补 | 具体做法 |
|---|---|---|
| 评审可靠性检验 | ScientistTwo 缺 | 引入 pfb 式 dual-judge（同族+异族）+ 检验 judge identity 是否翻转结论 |
| 流程组件归因 | ScientistTwo 缺 | 对 6 个 agent 组做消融（去掉 Idea Generator 还剩多少？去掉 Rebuttal Loop 还剩多少？） |
| 矛盾推理/加工层测量 | 双方都弱 | pfb 的 M7 思路可以移植到 ScientistTwo 的评审中：不只打总分，还测"是否识别了源间矛盾并裁决" |
| 固定题 benchmark | pfb 缺 | pfb 只有 5 道调研题，无法测"开放式研究能力"。可以借鉴 ScientistTwo 的任务构造方式（取顶会论文 → 提取局限 → 作为研究任务） |
| 低资源可及性 | ScientistTwo 缺 | 用 27B 级开源模型复现 ScientistTwo 流程的简化版，测"能力下限在哪里" |
| 引用存在性验证 | pfb 缺 | pfb 的 M5 应加一步：抽查来源 URL 是否真实存在（目前只测"有没有写 URL"） |
| 方法-代码一致性 | pfb 不适用 | pfb 不产代码，但如果未来 bench 扩展到"agent 写代码"任务，需要 ScientistTwo 式的逐行匹配审计 |

## 可借鉴的点（pfb → 吸收 ScientistTwo）

1. **Subset-first 分层验证**：pfb 的 90 runs 全量跑很贵。可以改为：先在 1 道题上跑 6 臂 × 1 run（6 runs）筛出有信号的臂，再对 top-2 臂扩到 3 runs。省 ~67% 算力。
2. **Rebuttal-as-experiment**：pfb 目前是"答完就评"。可以加一轮：judge 指出缺陷后，让模型针对缺陷补充证据/实验再评第二次，测"自我修正能力"。
3. **引用存在性抽查**：M5 加一个轻量步骤——对 sources 字段里的 URL 随机抽 3 条 HEAD 请求验活。
4. **完整性审计报告**：bench 报告末尾加一节"审计"：gold answer 是否有 hallucinated 事实、评分器是否对特定格式有偏、runs 之间是否有信息泄漏。

## 已超越的地方（pfb → 领先 ScientistTwo）

1. **Judge-dependence 发现**：这是 pfb 最核心的科学贡献，ScientistTwo 完全没有。如果 ScientistTwo 的 91.9%/72.1% 接受率在换评审后翻转（很可能），那它的核心 claim 就有问题。pfb 已经证明了这种翻转是真实存在的。
2. **开源可复现**：ScientistTwo 代码不开源，pfb 全部开源。在学术规范上 pfb 更站得住。
3. **M7 矛盾推理维度**：ScientistTwo 的评审是 holistic 打分，pfb 有细粒度的"加工层"测量。
4. **成本透明**：pfb 的实验成本完全可量化（90 runs × 本地 27B），ScientistTwo 的成本黑箱。

## 风险与保留判断

- ScientistTwo 的 80.4% 成功率是在"给定顶会论文作为起点"的条件下——这些论文的局限已经被人类专家识别过了，AI 只需要在已知方向上推进。真正的开放式探索（没有明确 SOTA 可以参考）可能远达不到这个数字。
- 两个 AI 评审（ScholarPeer、Stanford Agentic Reviewer）都是 LLM-based，pfb 已证明 LLM judge 有系统性偏差。ScientistTwo 没有做 judge robustness check。
- "平均提升 25.2%"的定义需要看原文公式——如果是相对提升（(new-old)/old），在小基数上会被放大。
- 代码未开源意味着"可复现"目前只是论文声称，未经第三方验证。

## 结论

ScientistTwo 和 pfb 是互补关系：前者证明"前沿模型 + 完整 pipeline 能做研究"，后者证明"你怎么知道它做得好"。pfb 的最大价值不在于它测了什么，而在于它揭示了**测量本身的脆弱性**——这对 ScientistTwo 这类系统是一个直接的方法论挑战。

如果成璐要跟进 ScientistTwo 的方向，最有价值的切入点不是复现它（没代码、没前沿模型），而是：
1. 用 pfb 的 dual-judge 方法去审它的 86 篇论文（judge robustness attack）
2. 用 27B 复现其 pipeline 的简化版，测能力下限
3. 把 M7 矛盾推理维度加入其评审框架，测"想得深"vs"做得多"
