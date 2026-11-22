# T-PR-17 任务书 — Prompt 序列消融文献滚雪球

**日期**: 2026-11-22 · **仓库**: prompt-first-bench · **分支**: arena/f65a5a27-prompt-first-bench
**背景**: 本仓 SM（状态机）pipeline 有固定 prompt 序列：L1 骨架 → 逐层 decompose（含索引维护）→ verify（相关性过滤）→ synthesize。我们计划做**路径依赖消融**：从同一中间 checkpoint 出发，用不同后续 prompt 序列（canonical / verify 删除 / 顺序置换 / minimal）续跑，比较最终 depth 分数（对 gold 树的多档连续分）。派发本任务前需文献滚雪球：确认这个实验设计在学界有没有先例、有没有已知机制解释、有没有方法学陷阱。

## 调研问题（3 条，每条给 verdict + 反例/近邻 + conf）

**C1. 多阶段 LLM pipeline 中 prompt/instruction 顺序或阶段编排的效应，有系统性研究吗？**
- 目标：找 2023-2026 论文，显式比较"同一任务、不同阶段顺序/不同指令序列"对最终输出的影响（不是 prompt 风格/语气，是**序列结构**：哪些阶段、什么顺序、哪些可省）。
- 判据：verdict = 有先例（列出）/ 部分（近邻但不完全同构）/ 未找到（否定性结论 conf ≤0.6）。
- 关键词方向（不限于）：pipeline orchestration ablation / stage order effect / multi-step instruction sequence / phase ablation LLM agent / workflow structure vs content。

**C2. "从中间状态用不同后续策略续跑、比较终态"（path dependence / checkpoint continuation）有先例吗？**
- 目标：LLM agent 或推理系统中，固定中间状态（partial solution / 中间树 / 对话历史），用不同后续策略（不同工具序列/不同 prompt/不同搜索策略）继续，比较终态质量的实验设计。
- 判据同上。关键词方向：path dependence LLM / continuation from intermediate state / policy ablation fixed state / trajectory suffix ablation。

**C3. 机制层：长上下文中指令位置/顺序的效应（lost-in-middle 家族）与"序列效应"的关系？**
- 目标：lost-in-middle（Liu et al. 2024）及后续工作里，指令/关键信息在长上下文不同位置的效果差异，是否足以解释"多阶段 pipeline 中阶段顺序影响终态"？即：我们的序列消融效应，多大程度可能只是位置效应的下游？
- 判据：给出机制映射（位置效应 → 序列效应的传导路径是否成立 + conf。

## 检索纪律（硬约束）

1. **每个引用的 arXiv ID 必须经 abs 页验证**（arXiv API id_list 在 arena 环境连挂过 3 次，直接走 abs 页）。
2. **OpenReview 2025-2026 必须查**（T-PR-16 的方法学缺口，本轮补上）：ICML/NeurIPS/ICLR 2025-2026 里 C1/C2 方向有无 OpenReview-only 投稿。
3. 否定性结论 conf ≤0.6，按纪律压低。
4. 检索记录逐条落盘（通道 + query + 结果），失败通道如实登记不静默跳过。

## 交付

- 文件：`tasks/T-PR-17-result.md`
- 格式：§C1/§C2/§C3 各一节（verdict 表 + 反例/近邻 ID·venue·一句话 + conf）+ §检索记录 + §方法学缺口
- commit + push 到 `arena/f65a5a27-prompt-first-bench`
- 回执必须含：repo URL + branch + commit_sha + 本任务书 sha256（防读旧版）
