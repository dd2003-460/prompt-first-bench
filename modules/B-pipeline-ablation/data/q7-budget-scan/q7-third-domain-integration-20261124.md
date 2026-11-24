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
2. **harness-regime confound**：GPU 批 pre-clamp（soft cap），Q6/Q7 post-clamp（hard cap），max_depth 不同。
   workshop §4.3 已声明 domain-dependence 要在 **realized node count** 上说，不是 nominal budget。
   Q7 719-r1 实测 719 节点（已验证），但 300 档的 realized 数需对账后才能做干净的「同 realized 数跨域」对比。

## 下一步（r2/r3 落盘后）
- [ ] 重跑 `q7-719-replication-check.py`（机制复现判定）
- [ ] 重算 Q7 cov 轴 719 档 n=3 均值 + 区间
- [ ] 对账 300/719 档 realized node count（绕开 nominal budget 混淆）
- [ ] 决定是否落进 workshop §4.3（三域 cov 对比表 + domain-dependence 初读）
