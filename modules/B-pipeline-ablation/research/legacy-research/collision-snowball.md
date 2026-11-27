# G2 滚雪球撞车调研 — pfb 核心 claim 的四象限覆盖

> origin: ai · 2026-11-08 · goal-pfb-production-hardening.md G2 门禁
> 方法：arXiv API 按 submittedDate 降序扫描（ego-browser 通道），四象限 = 权威 / 小众 / 最近轨迹 / 过去轨迹；每象限多组关键词交叉，特征短语做低垂果实精确检查。
> 撞车判定标准：有人做过「prompt 层 research pipeline 逐阶段组件贡献测量 + 离散组件独立性度量」且结论可比。仅维度重叠不算撞车，算 related work。

## 一句话结论

**无直接撞车。** RL 侧的 credit assignment 文献在 2026-09~11 爆发（一周内 5+ 篇），全部是训练侧、需要可微/可采样 rollout；prompt 层的组件消融有单点先例（Dissecting Agentic RAG, 2606.21553）但对象是 QA 检索循环不是 research pipeline，且没碰「搜索质量 × 校验质量无统一贡献函数」这个 gap claim。我们的差异化空间确认存在，但窗口在收窄——RL 系正在向 prompt 层渗透，论文里必须把这条时间线写进 related work。

## 撞车风险矩阵

| # | 候选 | arXiv | 日期 | 它做什么 | 与 pfb 的重叠 | 判定 |
|---|------|-------|------|---------|--------------|------|
| 1 | **Dissecting Agentic RAG: A Component Ablation for Multi-Hop QA with a Local 7B Model** | 2606.21553 | 2026-06-19 | agentic RAG 全管线（推理循环/query 分解/自适应检索）受控消融，HotpotQA 5000 题，本地 7B | **最高**。同样是"组件级边际贡献测量 + 小模型 + 本地跑" | **不撞车**。对象不同（multi-hop QA 检索循环 vs deep research 六阶段流水线）、评分维度不同（QA 正确率 vs M1-M6 多维 coverage）、没有 gap claim（没主张"不存在统一贡献函数"）。→ related work 必引，且是我们方法论最近的先例 |
| 2 | Grounded Credit Assignment in RL for Multi-Turn Search Agents | 2610.23148 | 2026-10-16 | GRPO 给所有 token 同 advantage → "找证据"和"用证据"两种能力混在一起；Search-R1 准确率涨但 evidence-supported 占比 84%→42.9% | 中。它也区分 search 和 use 两个能力，也发现 outcome reward 分配不了信用 | **不撞车**。训练侧（改 reward/advantage），我们是推理侧 prompt 层；它的发现（grounding gap）反而是我们 gap claim 的**佐证素材** |
| 3 | Beyond Outcome Rewards: Retrieval Credit for Search Agents | 2610.10179 | 2026-10-07 | 系统研究中间监督/reward shaping 改善 search agent RL 的 credit assignment | 同上，训练侧 | **不撞车**。related work 引用 |
| 4 | CASI: Credit Assignment via Set Intervention for Agentic Retrieval | 2610.20293 | 2026-10-14 | 集合干预构造反事实，解决"一个 reward 分给一组 retrieval action"的 within-set 归因 | 中。方法论上最接近"组件独立性"思想（反事实隔离） | **不撞车**。它是 RL 梯度估计问题（score-function estimator），我们是 prompt 杠杆的离散开关实验；且它只处理 retrieval 集合内部，不覆盖 verify 组件 |
| 5 | ToolRLA: Multiplicative Reward Decomposition | 2603.01620 | 2026-03-02 (v4) | 乘性 reward 分解：format validity × tool selection × param correctness × task success | 表面像"贡献函数" | **不撞车**。这是人为设计的乘性 reward 结构（训练信号），不是"证明不存在自然贡献函数"的分析结论。方向相反：它假设可以分解，我们在论证为什么不能 |
| 6 | Reflective Prompt Optimization of a Deep-Research Agent (GEPA) | 2610.12601 | 2026-10-08 | 用 GEPA 优化 DRA 两个 system prompt，topic-disjoint split 防记忆化，held-out citation reward +0.079 | 中。也是 prompt 层动刀 DRA | **不撞车**。它优化整段 prompt（端到端黑箱增益），不做逐阶段组件分解；它的 topic-disjoint 协议值得借鉴到我们的 G1 判读（防题目记忆化混淆） |
| 7 | Cited but Not Verified: Source Attribution in LLM Deep Research Agents | 2605.06635 | 2026-05-07 | AST parser 抽 inline citations，检索实际被引内容验证 claim-source 一致性 | 中。戳中 citation grounding（我们三道闸的目标域） | **不撞车**。它是评测框架（测现有系统的引用烂不烂），不是组件贡献测量；是 DREAM 一脉的延伸 |
| 8 | Long-Horizon Agent Trajectory Attribution | 2608.06909 | 2026-08-07 | 长程轨迹的细粒度归因 benchmark + 标注框架，统一 component schema | 中。"component attribution" 词面最像 | **不撞车**。它是行为归因（哪一步导致失败，人工标注），不是模块边际收益（去掉某阶段掉多少分）；且面向通用 agent 轨迹非 research pipeline |
| 9 | Reasoning-Search-Augmented LLMs: Taxonomy + Controlled Evidence Synthesis | 2610.29189 | 2026-10-21 | reasoning-search 耦合的操作分类学 + 基准分析 + 受控证据综合 | 低-中 | **不撞车**。综述+基准性质，controlled evidence synthesis 指证据融合不是组件消融 |
| 10 | Improving and Evaluating Open Deep Research Agents (BC-Small) | 2508.10152 | 2025-08-13 | BrowseComp 子集做 DRA 轻量基准，ODR vs 闭源 | 低 | **不撞车**。端到端总分榜，无组件维度 |

## 四象限覆盖记录

### 权威象限（高引/大厂/顶会脉络）
- DREAM (ACL 2026 long.448)：citation grounding 评测，已在 competitor-survey.md §1，本轮未重复查。
- RubricAtlas (2610.36878, 2026-10-27)：从专家报告挖 type-level rubrics 评 DRA —— 评分器设计相关，无组件消融。
- EMBERS (2611.03723, 2026-11-01)：defect-guided robustness testing of DRS —— 鲁棒性测试，新近出现，注意跟踪。
- DRACO (Perplexity+Harvard)：已在 competitor-survey.md，端到端 rubric 榜。
- 结论：权威圈在做的是**端到端评测 + 评测维度创新**（rubric mining / robustness / grounding），没人做组件级贡献测量。

### 小众象限（小团队/新玩法）
- Dissecting Agentic RAG (2606.21553)：见矩阵 #1，小众圈里离我们最近的。
- Real PMIDs, Wrong Papers (2610.29812, 2026-10-21)：harness design for biomedical claim-verification agents —— harness 设计视角，无消融。
- Object-Oriented Harness (2610.28380, 2026-10-20)：agent harness 演化，工程视角。
- 结论：小众圈在卷 harness 架构和领域特化（医疗/金融/专利），组件贡献测量仍是空白。

### 最近轨迹（2026-09 ~ 11，窗口期风险）
时间线（submittedDate）：
- 09-26 ASCT (counterfactual trees for CA)
- 09-30 ITER (interaction-aware retrieval)
- 10-07 Beyond Outcome Rewards (#3)
- 10-14 CASI (#4)
- 10-16 Grounded CA (#2)
- 10-19 Self-Consistency of Entity Sets & Citations under Repeated Probing (2610.26421) —— 重复探测下引用稳定性，与我们 anti-cache 扰动同精神
- 10-21 Reasoning-Search taxonomy (#9)、Trajectory Attribution (#8 后续)
- 10-26 Quantifying Claim Smoothing by LLM Research Agents (2610.35793) —— claim 平滑度量化，评测维度创新
- 11-01 EMBERS、FinForesight
- 11-02 CREDO (evidence-conditioned CA for temporal reasoning)
- 11-05 CORE (coarse-to-fine search + context management)

**趋势判断**：credit assignment 正从"纯 RL 训练信号"向"证据条件化/交互感知"细化，下一步很可能有人把这套语言用到 prompt 层（因为 prompt 层便宜、可解释、不需要训练预算）。我们的时间窗大概还有 1-2 个季度。**G1 数据出来后应尽快落文，不宜再拖到明年。**

### 过去轨迹（2024 ~ 2026-03）
- Shapley-based CoT attribution (SalaMAnder 2509.16561)：CoT 步骤的 Shapley 值 —— 组件归因思想的老根，但对象是单条 CoT 不是 pipeline 阶段。
- Explaining LLM Decisions Using Shapley Values (2404.01332)：更老的 XAI 脉络。
- ToolRLA (2603.01620)：乘性 reward 分解，见 #5。
- 结论：过去的工作要么在 CoT 内部（步骤级 Shapley），要么在 reward 设计（训练侧），没有人跨到"research pipeline 阶段级 + prompt 杠杆"这个位置。

## 低垂果实精确检查（特征短语零命中 = 没人用这些说法）

| 短语 | 命中 |
|------|------|
| "search quality" AND "verification quality" | **0** |
| "contribution function" AND "search" AND "LLM" | 1（MemSearch-o1，memory growth 语境，无关） |
| "independence" AND "component" AND "research agent" | 4（YouRA/Scaling Auto Research/Novelty-Aware Retrieval/AgentIR，均为架构或新颖性评估语境，无组件独立性度量） |
| "prompt layer" AND "reinforcement learning" AND "analog" | **0** |

**"prompt 层 RL 类比"这个 framing 本身无人使用** —— 这是 pfb 论文标题级 claim 的独特性证据。

## 对 G5 报告的输入

1. related work 节必须含：#1（最近先例）、#2/#3/#4（RL credit assignment 三条线，说明我们为什么不走训练侧）、#5（反向对照：有人假设可分解）、#6（prompt 层优化的另一条路：端到端 GEPA vs 我们的逐阶段）、#7（citation grounding 评测脉络）。
2. gap claim 的表述要加限定："在 2026-11-08 前的 arXiv 公开文献中"——滚动核验纪律，投稿前重跑一次本调研。
3. 时间压力：RL 系向 prompt 层渗透的趋势明确，落文窗口 1-2 季度。
4. 可借鉴项：#6 的 topic-disjoint split 协议（G1 判读时排除题目记忆化混淆）；2610.26421 的 repeated probing（与我们 anti-cache 扰动互证）。

## 核验回执

- 通道：ego-browser（ego-lite 持久会话），arXiv export API，2026-11-08 执行。
- 查询组数：8 组关键词 × 最多 25-40 条/组，去重后人工筛出 10 个候选精读 abstract。
- 置信度：medium-high。限制：① 只扫了 arXiv（预印本主渠道，够但非全量）；② 关键词组合不可能穷尽所有表述变体（如完全不用 "ablation" 而用 "leave-one-out" 的工作可能漏网）；③ 未查非英语文献。缓解：投稿前按滚动纪律重跑 + 让 arena 换一组同义词再扫一遍。