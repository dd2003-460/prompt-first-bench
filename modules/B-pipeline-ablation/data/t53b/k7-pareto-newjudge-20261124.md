# K7 预算扫描 Pareto 分析 — 新口径版（2026-11-24 00:55）

# origin: ai
**口径声明**: 本版用 judge_v1 + 域内 gold（gpu → gold-gpu-units.json 36 单元；q6 → gold-q6-units.json 46 单元），
total = 0.5*struct(depth/GOLD_DEPTH) + 0.5*cov(bge-m3 cosine≥0.70 命中 gold 单元比例)。
**替代旧口径**: 旧 depth_score（t53b 时代，anatomy-0.5184.md 记录其与 cov r=0.861，self-judge 伪影）。
旧口径首跑（k7_pareto-gpu-20261124.md）的"负面信号"已作废——是口径伪影，不是真实效应。

## GPU 域（15 runs, max_depth=5, formula mode）

数据: runs_budget_scan/gpu_budget*.json，重评 → gpu-rescore-newjudge-20261124.json

| budget | n | mean total | CI95 | 边际/100节点 |
|---|---|---|---|---|
| 50 | 3 | 0.4630 | [0.3556, 0.5806] | — |
| 100 | 3 | 0.4676 | [0.4111, 0.5528] | 0.0095 |
| 150 | 3 | 0.4769 | [0.3972, 0.5667] | 0.0071 |
| 300 | 3 | 0.6129 | [0.5944, 0.6361] | **0.1944** |
| 719 | 3 | 0.6426 | [0.5667, 0.7083] | 0.0093 |

**形状**: 单调升 + 拐点。150→300 跳升 Δ=+0.136（CI 不重叠: 150 上界 0.567 < 300 下界 0.594，显著）；
300→719 Δ=+0.030（CI 重叠，不显著）。**Pareto 拐点 ≈ 300 节点**。
跳升主要由 cov 贡献（300 档 cov 0.39-0.47 vs 150 档 0.19-0.33）：~300 节点前树覆盖不到 gold 的
大部分单元，过了 300 节点后覆盖饱和。struct 轴 300 档已全 0.8（depth 饱和），无额外贡献。

## Q6 域（15 runs 原批 + 2 runs rerun, max_depth=4 默认）

数据: q6-budget-scan/q6-gold-rescore.json（B4 后评，Q6 gold）+ q6-budget-scan-rerun/q6-gold-rescore-rerun.json（本轮新做）

| budget | 原批 mean (n=3) | rerun (n=2, cache 隔离) |
|---|---|---|
| 50 | 0.3290 | — |
| 100 | 0.3695 | — |
| 150 | 0.4435 | — |
| 300 | 0.4652 (sd=0.000) | 0.4652 (r1 0.4761 / r2 0.4543, sd=0.011) |
| 719 | 0.4833 | 等 nodepth 批 |

**形状**: 同样单调升，300 后增益放缓（300→719 Δ=+0.018）。
**cache 对照**: 原批 300 档 sd=0.000 vs rerun sd=0.011 → cache 共享压低方差假设在 Q6 gold 口径下
初步支持（n=2，等 300-r3 + 719 nodepth 批）。原批 300/719 逐 rep 分数相同的真因 = gpu gold 跨域
匹配命中数太少（旧口径 cov 0.0/0.083/0.056），不是 cache 串内容（节点 claim 0/30 相同已排除）。

## 结论（两域同向，conf 0.7）

1. **预算-质量曲线单调升 + 拐点**：D 的预算控制假说在 27b 本地条件下成立——预算大→覆盖 gold
   贡献因子全→质量升；但边际收益在 ~300 节点后趋零，300 节点是性价比拐点。
2. **旧口径负面信号作废**：depth_score 单轴（self-judge）在低预算档饱和/噪声主导，掩盖了 cov 轴的
   真实跳升。质量轴必须用域内 gold 的 cov 层，不能单用 depth。
3. **待办**: ① 719 nodepth 批（relay 链在跑）落地后补 Q6 719 档独立检索数据；② 300-r3 落地后
   cache 对照 n=3；③ 拐点 300 是否跨题稳健（Q7 扫描在 relay 链 phase 2）。

**质量轴声明**: judge_v1 的 cov 层用 bge-m3 embedding 匹配 gold 单元，gold 由人+arena 构建（非模型自产），
比旧 self-judge 独立性强；但 struct 层仍是机械深度比，且 bge-m3 匹配阈值 0.70 是标定的非验证的。
结论限于开源 27b + 本地 4×V100 条件。
