# 阶段 01：目标分解 — RUBRIC-V3-FULL-AUDIT / G2 构念效度根因

> goal: rubric-v3-audit-g2 · 分支 ralph/rubric-v3-audit-g2 · 2026-10-30
> 上游任务书: tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md（队首大 goal，G1-G6 串联）
> 前置: G1 机判脚本已落盘并跑通（assert-g1-audit.py, exit 0, 信号 S2/S3/S4 已产出）；本 goal 消费 G1 信号 + blindtest-r1 数据做根因解剖。

## 因素分解

目标 = 回答「blindtest 1/5 否决的根因是什么」，拆成四个正交因素：

### F1 · 公式层（w2/w3 计算是否算错）
- 已知条件：权重公式 `w2 = 1 + min(-log2(p̃), log2(100))`，p̃=null→1.0（root policy）；W3=w1×w2。
- 待验证：新 judge 与旧 judge 的 w2 值是否与公式精确一致（逐节点复算）。
- 研究路径：对 prior-estimates.json 与 judge-blindtest-r1.json 各 31 节点按公式重算 w2，比对落盘值。
- 判定标准：全部精确一致 → 公式层排除；任何 mismatch → 公式层是根因候选。

### F2 · p̃ 估计层（两个 judge 的先验偏差方向与幅度）
- 已知条件：cross-judge Spearman ρ=0.688（n=30，过 0.6 线，方向稳定）；但节点级 top-5 完全不同。
- 待验证：
  - F2a 系统性偏差：新 judge 相对旧 judge 的 p̃ 漂移方向（整体上调还是局部翻转？）
  - F2b 零命中高估：经验命中率=0 的节点中，新 judge 给了 p̃≥0.2（w2 被压低→w3 虚高）的有多少？
  - F2c 低先验抬升：旧 judge 给极低 p̃（≤0.05）的节点，新 judge 是否系统性抬到 0.3 附近（疑似保守下界效应）？
- 研究路径：hit-matrix 8run 经验命中率 vs 双 judge p̃ 的逐节点对照表（31 行），分类统计。
- 判定标准：若多数 w2 大幅变化来自「零命中节点被新 judge 抬 p̃」→ p̃ 估计层是主根因。

### F3 · gold 标注层（gold-marked set 本身是否有争议）
- 已知条件：strict 口径 5 节点（N-2.1 ■瓶颈#1 / N-3.2.2 ★2倍分歧 / N-2 ★F-B / N-4 ■瓶颈#2 / N-1.3 ★F-C），r71b 冻结；F-A 订正标记不计入。
- 待验证：
  - F3a 五个 gold 节点的 8run 经验命中率分布（若 gold 节点普遍零命中，说明 gold 标的是「理论重要性」而非「实际出现率」——p̃ 机制天然测不到这类节点）。
  - F3b 非 gold 的高命中节点（如 N-5.3 hitrate=1.0、N-3.2.3=1.0、N-1.1=1.0）为何没进 gold set——gold 定义是「瓶颈/订正」不是「高频」，这个口径差异是否就是构念效度失败的结构性原因？
- 研究路径：gold-tree.md 标记行 + hit-matrix 交叉表。
- 判定标准：若 gold set 与 hitrate 相关性≈0 且口径可解释（瓶颈≠高频）→ gold 标注层存在构念错配，需修判据或换 gold set。

### F4 · 判据层（top-5 ≥3/5 判据本身是否合理）
- 已知条件：判据 = W3 top-5 中带 gold 标记的节点数 ≥3/5（strict 口径）。
- 待验证：
  - F4a 该判据在 n=31 节点、5 个 gold 下的期望基线：随机 top-5 命中 gold 的期望 = 5×5/31 ≈ 0.81，≥3 的概率很低（超几何 P(X≥3) ≈ 2.6%）——判据本身极严。
  - F4b 旧 judge 3/5 刚过线、新 judge 1/5 否决，差异主要来自哪几个节点进出 top-5（diff 分析）。
- 研究路径：超几何期望计算 + 双 judge top-5 diff。
- 判定标准：给出判据严格度的量化描述，供 G6 定稿建议用。

## 空缺清单

| # | 空缺 | 类型 | 影响 |
|---|------|------|------|
| G1 | 三个失败节点（new top-5 中无 gold 的三个：N-1.1.3/N-5/N-3.2.4）的逐个 rationale 文本细读 | 仍需研究（02 阶段） | F2/F3 归因需要 rationale 佐证 |
| G2 | gold set 是否应加入「高频非瓶颈」节点作为第二判据 | 开放设计问题 | F4 结论依赖此决策，留给 G6 |
| G3 | 第三个独立 judge（R5.2-third-scorer 未完成）的数据 | 外部阻塞 | 本 goal 只用双 judge，三 judge 一致性留 R5.2-third-scorer |

## 阶段 02 研究入口

- 仓库内材料足够（F1/F2/F4 全部可从 JSON 复算；F3 从 gold-tree.md + hit-matrix）→ 02 阶段以「web-llm 强制步骤 + 仓库内证据固化」为主，不依赖外网。
- web-llm 预期三 provider 仍失效（上次回执 error）→ 记录失败回执后继续，不阻塞。

## 判定

分解完成：四个叶子因素（F1 公式 / F2 p̃ 估计 / F3 gold 标注 / F4 判据）互相正交、合起来覆盖「根因」的全部候选空间；空缺 G1-G3 均已登记且不影响 02 启动。→ 进入 02。