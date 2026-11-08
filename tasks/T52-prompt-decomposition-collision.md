# T52: Prompt Decomposition → Reasoning Depth — 滚雪球撞车调研

> origin: ai · 2026-11-09 · 成璐指令「非常怕撞车」
> 本任务只涉及 prompt-first-bench / arena/sigma-nlnk-snowball，忽略历史中其他仓库的消息。

## 【目标】

系统调研：**有没有人做过"通过 prompt 层的逐层/递归分解来提升 LLM 推理深度或答案质量"的研究？** 具体包括：

1. **机制层面**：把复杂问题拆成子问题树（hierarchical/recursive decomposition），让 LLM 逐层回答，最终聚合——这种 pipeline 是否被系统研究过？效果量多大？在什么条件下有效/无效？
2. **与我们 S5 的差异化**：我们的 S5 pipeline = P1(逐层分解+source tagging) → P1.5(gap check) → P2/P3(逐节点检索验证) → P4(综合)。核心创新点是：(a) 分解不是单次生成而是迭代加深（状态机架构，允许返回 P1）；(b) 每个节点独立检索验证而非整体上下文；(c) 用显式目标函数 S_α = Σ[n·ln(kₙ)] 驱动模型自主调节分解深度。这三点分别有没有先例？
3. **最近邻工作**：GPT Researcher 的 deep mode (breadth×depth 递归树)、STORM 的 persona 对话→大纲、Self-Refine/Reflexion 的迭代改进、Tree of Thoughts 的搜索树——这些跟我们的区别是什么？它们有没有量化"分解本身贡献了多少分"？

## 【背景】

- pfb 当前核心 claim 有两个支柱：
  - **支柱 A**（已有 G2 调研覆盖）：组件贡献测量 + "不存在统一 search×verify 贡献函数" → `research/collision-snowball.md`
  - **支柱 B**（本任务覆盖）：prompt 层分解 + 逐节点验证可以系统性提升推理深度 → 尚无专门调研
- 本地实验证据：S5 depth score 从 v8(0.354) → v12(0.377) → v13(0.487)，纯靠 prompt 改进（few-shot 结构示例、source tagging、S_α 目标函数），无训练、无架构改动。
- 如果已经有人做过类似的事且结论可比，我们需要知道：(a) 他们的效果量是多少；(b) 我们的增量在哪；(c) 论文 related work 怎么定位。

## 【SOP 索引】

- `loop/prompt-first/01-goal-decomposition.md`
- `loop/prompt-first/02-information-research.md`
- `loop/prompt-first/02.5-cross-check.md`
- `sop/arena-loop-pipeline.md` §3（会话台账）

## 【实验设计】

### 调研维度（四象限 × 三特征）

| 象限 | 特征 | 关键词组（arXiv API + Google Scholar） |
|------|------|----------------------------------------|
| 权威 | 高引/顶会/大厂 | "hierarchical decomposition" + "LLM reasoning"; "question decomposition" + "multi-hop"; "tree of thoughts"; "recursive problem solving" + "language model"; "iterative refinement" + "reasoning depth" |
| 小众 | 小团队/新玩法 | "decomposition-guided retrieval"; "node-level verification" + "LLM"; "progressive deepening" + "prompt"; "iterative decomposition" + "state machine" + "LLM" |
| 最近轨迹 | 2026-06 ~ 2026-11 | 同权威象限关键词 + submittedDate 过滤; "deep research agent" + "decomposition"; "research pipeline" + "ablation" + "stage" |
| 过去轨迹 | 2024 ~ 2026-03 | "Self-Refine"; "Reflexion"; "Least-to-Most prompting"; "Tree of Thoughts"; "Graph of Thoughts"; "plan-and-solve" + "pruning" |

### 低垂果实精确检查（特征短语）

| 短语 | 预期命中 |
|------|---------|
| "iterative deepening" AND "LLM" AND "decomposition" | ? |
| "per-node" AND "retrieval" AND "verification" AND "LLM" | ? |
| "objective function" AND "decomposition depth" AND "prompt" | ? |
| "state machine" AND "decomposition" AND "language model" AND "reasoning" | ? |
| "source tagging" AND "knowledge" AND "search" AND "LLM pipeline" | ? |

### 评分标准（每篇候选）

对每篇找到的相关论文，按以下维度打分：

| 维度 | 说明 | 权重 |
|------|------|------|
| 机制重叠 | 它做的分解方式跟我们 S5 有多像（单次 vs 迭代、有无验证、有无目标函数） | 30% |
| 量化程度 | 是否量化了"分解本身"的贡献（消融实验）vs 只报端到端总分 | 25% |
| 任务类型 | open-ended/reasoning vs factual QA vs code generation | 20% |
| 时间 | 2026 年 > 2025 > 更早 | 15% |
| 可复现性 | 开源代码/数据 vs 只有论文 | 10% |

### 验收标准

1. ≥300 行调研报告，落盘 `research/prompt-decomposition-collision.md`
2. ≥15 个来源，其中 ≥8 读了原文（不是只看 abstract）
3. 每个候选有明确判定：撞车 / 部分重叠(related work) / 无关
4. 三个核心问题的判决句（带 conf）：
   - Q1: "迭代加深分解"（允许返回上一层重新拆）有没有先例？
   - Q2: "逐节点独立检索验证"（非整体上下文）有没有先例？
   - Q3: "显式目标函数驱动分解深度"（告诉模型 S_α 让它自己调节努力程度）有没有先例？
5. 反方复核：≥3 个质询（"你的关键词组合可能漏掉 X 类工作"、"你把 Y 判为无关但它的 Z 特征其实重叠"等）
6. 撞车风险矩阵（表格形式，类似 collision-snowball.md 的格式）

## 【失败降级】

- arXiv API 不可用 → 用 ego-browser 访问 arxiv.org 网页搜索
- 某关键词组零结果 → 换同义词再试一轮（如 "hierarchical" → "layered"/"tiered"/"multi-level"）
- 找不到原文 → 标 [abstract-only]，conf 降一档
- 全部通道失败 → 报告已尝试的查询组和零结果事实，不编造

## 【交付物】

- `research/prompt-decomposition-collision.md`（主报告）
- `research/prompt-decomposition-search-log.json`（所有查询组 + 命中数 + 筛选过程）

## 【给 Lead 的备注】

- 与 T51（S_α 目标函数滚雪球）的关系：T51 聚焦"Σn·ln(k) 这个公式有没有人用过"，本任务聚焦"prompt 分解提升推理深度这个机制有没有人系统研究过"。两者互补但独立。
- 如果 Q1-Q3 全部"无先例"，则 pfb 的方法论贡献是完整的；如果某个有先例，需要评估差异化空间并调整论文叙事。
- 优先级：本任务 > T51（机制撞车比公式撞车严重得多）。