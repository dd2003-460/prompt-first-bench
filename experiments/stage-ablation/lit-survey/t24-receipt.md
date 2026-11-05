# T24 文献调研回执（Arena agent 产出 · 2026-11-05）

## 状态
- 调研完成：65 篇文献（42 篇同行评议 + 3 篇技术报告 + 1 篇 position paper + 其余预印本/博客）
- Push 失败：Arena GitHub App token 对 pfb 只有读权限（POST /git/refs, /git/blobs → 403）
- JSONL 原始数据在 agent workspace `/home/user/prompt-first-bench/experiments/stage-ablation/lit-survey/decomp-prerequisite-survey.jsonl`（65 行）
- 需 Arena 重新授权 pfb 写权限后 `git push origin arena/4a614e63-prompt-first-bench`

## 三子问题结论

### Q-A: 分解是前提条件吗？
**Partially。** 61 条证据里：反对 H1 有 10 条、支持 H1 有 20 条、部分支持 26 条。
- SOTA 方法（Self-Consistency +17.9%、ToT 4%→74%、ReAct、Search-R1 +41%、Agentless 32.00%/$0.70）都在**无显式分解**时达到同等或更好。
- **反证**：Khan (NeurIPS'23) 明确 "naive model-written decomposition can hurt performance"；Khandelwal (EMNLP'23) 受控拆解证明增益来自任务专用模块而非分解结构本身。
- **修正措辞**：从「分解是前提」改为「分解在需要跨文档组合的任务上是稳健杠杆」。

### Q-B: 机制是什么？
Sprague et al. (ICLR 2025) 的 110 篇元分析 + AC 元评审：把轨迹拆成 planning/execution 后，**增益主要来自更可靠的执行，而非更好的规划**。
- S1 应解释为「把题拆到可核验粒度」，不是「提升规划能力」。
- H3 负效应的可引用解释：一次性 prompt 核验会放大确认偏误（Xie et al., ICLR'24 spotlight）。

### Q-C: 留空/弃答有独立价值吗？
**有条件有效。**
- 证据缺失时有效：语义熵、口头置信度、主动澄清 → +5 F1。
- 证据误导时基本失效：GRAB-RAG 41.6% 仍作答，其中 63% 逐字复述植入的错误实体。
- 硬 trade-off：更强 RAG 把幻觉率 87.6%→65.4%，同时把弃答率 5.0%→0%（REASONS）。

## 对 H1 的两处必须修正
1. **措辞**：「分解是前提」→「分解在需要跨文档组合的任务上是稳健杠杆」
2. **机制**：增益来自执行可靠性（拆到可核验粒度），不是规划能力提升

## Agent 自发现并修正的错误
- 已发表 venue 计数从 44 改为 42（原先误把 3 篇技术报告 + 1 篇 position paper 算作同行评议）
- evidence_type 有 3 条超出任务书枚举值已归一化
- JSONL 行数始终是 65，未破坏 append-only

## 下一步
- [ ] Arena GitHub 授权 pfb 写权限 → push 两个 commit（sha 保留）
- [ ] 或：让 agent 输出 base64(JSONL) → 本地解码落盘
- [ ] 更新 tasks/T24-decomp-prerequisite-lit-survey.md 标记完成