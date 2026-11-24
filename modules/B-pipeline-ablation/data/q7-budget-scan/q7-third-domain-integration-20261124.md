# Q7 = workshop §4.3 等待的第三域数据 — 整合备忘（2026-11-24）

> 连接：workshop-draft-metacog-20261122.md 的 abstract + §4.3 反复把「Q7 第三域扫描」标为 pending 的
> 决定性检验（saturation point 是否 domain-dependent）。本目录的 Q7 预算曲线正是这份数据
> （队列注释：`Q7 budget scan = general 方法论 A1 第三域验证 (GPU+Q6+Q7)`）。

## 口径要害（喂进 workshop 必须用 cov 轴，不能用 composite）
- workshop 的 domain-dependence claim 关于 **coverage 层**（mechanical, self-bias-free）。
- 本曲线 headline（log 饱和 / concave Pareto）基于 **judge_total composite**（含 self-biased depth 层）。
- 因此整合进 §4.3 只能用 cov 轴，composite 的 concave 结论不直接迁移到 domain-dependence 论证。

## Q7 cov 轴（从 q7-budget-response-curve.json rows[].cov_mean 抽出）
| budget | cov_mean | 300→719 Δ |
|---|---|---|
| 50 | 0.1026 | |
| 100 | 0.1667 | |
| 150 | 0.1795 | |
| 300 | 0.2564 | |
| 719 | 0.3269 | **+0.0705** |

## 初读（n=1，待 r2/r3 确认）
- Q7 cov 在 719 **仍在升**（300→719 Δ+0.0705），与 Q6（719 仍升 Δ+0.029）同向，与 GPU（~300 饱和）相反。
- 三域对比：GPU 饱和@~300 / Q6 仍升@719 / Q7 仍升@719 → 初读支持 domain-dependence（2/3 域在 719 未饱和）。

## 两个诚实边界（整合进 workshop 前必须处理）
1. **n=1**：719 当前只有 r1，r2/r3 在途。workshop 自身纪律 = 719 点要 n=3 才落文。r2/r3 到位后用
   `q7-719-replication-check.py` 复现判定 + 重算 cov 均值区间。
2. **harness-regime confound（已定性 20:55）**：GPU 批 pre-clamp（soft cap，realized 50→103-423 / 719→381-747 大量重叠），
   Q7 批 post-clamp（hard cap，`47a8543cd` 11-23 13:44 之后；队列 11-23 22:55 起）。
   **实测 Q7 各档 realized==nominal 精确相等**（50/100/150/300/719 零 overshoot）→ Q7 是干净预算轴，GPU 是脏轴。
   因此 confound 的具体形态 = 树生长动力学本身不同（硬钳制改变每轮展开行为），不只是"测量口径"。
   跨域对比必须在 realized node count 轴上做：Q7 的 nominal 可直接当 realized 用，GPU 必须用实测 realized。
   300 档 n=2 独立 rep 已再确认（r1/r2 claim-set 哈希相同=复制，r3 独立；与曲线 JSON 一致）。

## 下一步（r2/r3 落盘后）
- [ ] 重跑 `q7-719-replication-check.py`（机制复现判定）
- [ ] 重算 Q7 cov 轴 719 档 n=3 均值 + 区间
- [x] 对账 300/719 档 realized node count（20:55 完成：Q7 各档 realized==nominal 精确相等，干净轴；见边界 2）
- [ ] 决定是否落进 workshop §4.3（三域 cov 对比表 + domain-dependence 初读；GPU 用实测 realized 对齐）
