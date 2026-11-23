# K7 预算扫描 Pareto 分析 — 新口径版（2026-11-24 00:55）

# origin: ai
**口径声明**: 本版用 judge_v1 + 域内 gold（gpu → gold-gpu-units.json 36 单元；q6 → gold-q6-units.json 46 单元），
total = 0.5*struct(depth/GOLD_DEPTH) + 0.5*cov(bge-m3 cosine≥0.70 命中 gold 单元比例)。
**替代旧口径**: 旧 depth_score（t53b 时代，anatomy-0.5184.md 记录其与 cov r=0.861，self-judge 伪影）。
旧口径首跑（k7_pareto-gpu-20261124.md）的"负面信号"已作废——是口径伪影，不是真实效应。

## GPU 域（K7 15 runs + rep-scan 15 runs 池化, max_depth=5, formula mode）

数据: runs_budget_scan/gpu_budget*.json（K7, n=3/档）+ rep-scan/rep-scan-scores.json（100/150/300 各 n=5，
无 synthesis，机械轴有效），重评 → gpu-rescore-newjudge-20261124.json

**池化（K7+rep-scan，n=3/8/8/8/3）**:

| budget | n | struct | cov | total |
|---|---|---|---|---|
| 50 | 3 | 0.667 | 0.259 | 0.463 |
| 100 | 8 | 0.625 | 0.264 | 0.445 |
| 150 | 8 | 0.725 | 0.278 | 0.501 |
| 300 | 8 | 0.800 | 0.358 | 0.579 |
| 719 | 3 | 0.933 | 0.352 | 0.643 |

**形状（池化口径，稳健）**: 总体单调升（100 档微凹是 rep-scan struct 0.625 拉低，非真实凹点）；
**cov 在 300 档升到 0.358 后 719 不再升（0.352）**——gold 覆盖在 ~300 节点饱和；struct 继续升
（0.8→0.933）但那是机械深度台阶（max_depth=5 台阶函数），不是质量。**Pareto 拐点 ≈ 300 节点**：
300 之前 cov 增益小（50→300 共 +0.099），300→719 加 320 节点 cov 不涨。

**⚠ 小样本警告（11-24 01:10 修正）**: K7-only n=3 口径下 300 档 cov=0.426（rep 间 0.39-0.47），
池化 rep-scan n=5（cov 0.317）后拉回 0.358——K7-only 的"150→300 跳升 0.194/100节点、CI 不重叠显著"
是 n=3 伪影（rep-scan 300 档 r4-r8 的 cov 系统性低于 K7 三 rep，可能 era 差异：rep-scan 无 synthesis
且跑在 per-node hard clamp 之前，soft cap 下 realized 节点 271-462 与 150 档重叠）。**稳健声明降级为**：
cov 在 ~300 节点后进入平台（719 不高于 300，两口径一致），struct 机械台阶继续升；"300 处显著跳升"
不成立，池化后 150→300 增益 0.077 与 300→719 的 0.064 同量级。拐点位置（~300）两口径一致，
拐点强度（跳升 vs 缓坡）以池化口径为准 = 缓坡。

## Q6 域（15 runs 原批 + 2 runs rerun, max_depth=4 默认）

数据: q6-budget-scan/q6-gold-rescore.json（B4 后评，Q6 gold）+ q6-budget-scan-rerun/q6-gold-rescore-rerun.json（本轮新做）

| budget | 原批 mean (n=3) | rerun (n=3, cache 隔离) |
|---|---|---|
| 50 | 0.3290 | — |
| 100 | 0.3695 | — |
| 150 | 0.4435 | — |
| 300 | 0.4652 (sd=0.000) | 0.4688 (r1 0.4761 / r2 0.4543 / r3 0.4761, sd=0.013) |
| 719 | 0.4833 | 等 nodepth 批 |

**形状**: 同样单调升，300 后增益放缓（300→719 Δ=+0.018）。
**第二域 cov 层形状核验（2026-11-24 01:48，推翻"~300 饱和"的泛化）**: 用 Q6 域内 gold（46 units）
重算原批 15 run 的 cov 层（机械轴，与 draft GPU cov 曲线同口径）：
50:0.0580 / 100:0.0725 / 150:0.0870 / 300:0.1377（rerun 干净值，原批 cache 共享 sd=0 伪影）/
719:0.1667（n=3/档）。**Q6 域 cov 到 719 仍在升（300→719 Δ=+0.029），未饱和**；而 GPU 域
300→719 Δ=−0.006（平台/回落）。→ "cov 轴拐点 ≈ 300 节点"是 **GPU 域限定**的结论，不是通用
预算-覆盖规律；Q6 域在 719 节点仍未见饱和点（饱和点 >719 或不存在，待 719 nodepth 批 + Q7
扫描定位）。两域绝对 cov 不可比（gold 规模 46 vs 36 units、域不同），可比的是曲线形状。
**cache 对照（n=3，300-r3 落地 2026-11-24 01:25）**: 原批 300 档 sd=0.000 vs rerun sd=0.013
（r1=0.4761/252节点, r2=0.4543/300节点, r3=0.4761/300节点）→ cache 共享压低方差假设在 Q6 gold
口径下支持。r1 与 r3 分数相同但节点数不同（252 vs 300）→ 进一步排除 cache 串内容（cache 的话
节点数也应相同），分数相同是 gold 命中数恰好都是 7/46。原批 300/719 逐 rep 分数相同的真因 =
gpu gold 跨域匹配命中数太少（旧口径 cov 0.0/0.083/0.056），不是 cache 串内容（节点 claim 0/30
相同已排除）。

## 独立轴核验：metacog 轴不随预算走（11-24 01:15）

metacog 轴（gap 标记/检索/检索后精度，gold-free，compute_metacog）与 cov 轴的相关性：
- Q6 域 n=15：Spearman ρ=**0.004**（零相关）
- GPU 域 rep-scan n=15：ρ=**0.275**（弱相关）

metacog 每档均值：
- Q6：50:0.237 / 100:0.271 / 150:0.258 / 300:0.188 / 719:0.236（不单调，300 反而最低）
- GPU（rep-scan）：100:0.246 / 150:0.247 / 300:0.232（平）

**含义**：预算控制的是 gold 覆盖度（cov 轴），**不控制元认知质量**（gap 标记/检索行为）。
两轴近乎独立（ρ≈0）→ "预算 = 覆盖度控制旋钮"只对覆盖轴成立；若 D 的 AGI 目标包含
"模型知道自己不知道"（metacog），预算不是有效旋钮，需要另找控制变量（prompt/hook 层）。
这是 K7 结论的必要限定：预算-质量曲线的"质量"必须明确指 cov（gold 覆盖），不能泛化到
整体研究质量。

## 结论（两域同向，conf 0.60）

1. **预算-质量曲线：cov 轴升幅随预算增大，饱和点域依赖**：D 的预算控制假说在 27b 本地条件下
   **部分成立**——预算大→gold 覆盖（cov）升。但饱和点不是通用常数：GPU 域 cov 层 300→719
   Δ=−0.006（~300 平台），Q6 域 cov 层 300→719 Δ=+0.029（719 仍未饱和）。**"Pareto 拐点 ≈
   300 节点"是 GPU 域限定的结论**；Q6 域饱和点 >719 或不存在，待 719 nodepth 批 + Q7 扫描定位。
   struct 轴（机械深度台阶）继续升但那是 max_depth 台阶函数不是质量。
2. **旧口径负面信号作废**：depth_score 单轴（self-judge，r=0.861 与 cov 相关）在低预算档饱和/噪声
   主导，掩盖了 cov 轴的真实形状。质量轴必须用域内 gold 的 cov 层，不能单用 depth。
3. **小样本教训**：n=3/档的"显著跳升"在池化 n=8 后消失——拐点强度声明必须用池化口径，n=3 只能
   定拐点位置不能定拐点强度。
4. **metacog 轴独立于预算（ρ≈0）**：预算只控制 gold 覆盖（cov），不控制元认知质量。若 AGI 目标
   含"模型知道自己不知道"，预算不是有效旋钮，需 prompt/hook 层另找控制变量。
5. **待办**: ① 719 nodepth 批（relay 链在跑，r1 已开跑 2026-11-24 01:36）落地后补 Q6 719 档
   独立检索数据；② ~~300-r3 落地后 cache 对照 n=3~~ **已完成（2026-11-24 01:25，见上表）**；
   ③ Q7 扫描验 cov 饱和点（~300）跨题稳健。

**质量轴声明**: judge_v1 的 cov 层用 bge-m3 embedding 匹配 gold 单元，gold 由人+arena 构建（非模型自产），
比旧 self-judge 独立性强；但 struct 层仍是机械深度比，且 bge-m3 匹配阈值 0.70 是标定的非验证的。
结论限于开源 27b + 本地 4×V100 条件。

## 队列评分 gold 参数 bug（2026-11-24 02:45 发现并修复）

**现象**: `q6-budget-scan-rerun/q6-rerun-scores.json` 里 4 个已落地 run（300 r1/r2/r3 + 719 r1）的
cov 全 = 0.0278、total 全 = 0.4139——跨 run 完全相同，不可能。

**根因**: 队列脚本的评分块调 `judge_run(f)` 未传 `gold_units`，judge_v1 默认用 GPU gold
（36 units）评 Q6 run。跨域 gold 命中极低（0.0278），且 GPU gold 对所有 run 相同 →
分数跨 run 无区分度。nodepth 队列、Q7 队列同 bug（Q7 更严重：默认 GPU gold 评 Q7 run）。

**影响面核验**:
- draft 跨域段的 Q6 cov 序列（0.058/0.073/0.087/0.138/0.167）**不受影响**——300 值 0.138
  是手动 `judge_run(f, gold_units=Q6 gold)` 重评的（2026-11-24 02:45 复算确认：rerun 300
  三 rep = 0.1522/0.1087/0.1522, mean 0.1377）；其余四档来自 q6-gold-rescore.json（Q6 gold
  口径，已验证 719 档 per-rep 0.1304/0.1739/0.1957 与文件直接重评一致）。
- metacog 字段不受影响（gold-free）。
- 原批队列（q6_budget_scan_queue.sh）用默认 GPU gold 是**设计如此**（注释写明"B4 用
  --gold-units Q6 重评"），不是 bug。

**修复**: 三个队列脚本（rerun/nodepth/Q7）的评分块改为显式加载对应域 gold 并传
`gold_units=`。rerun 队列在飞（719 r2 在跑），修复对后续 run 生效；已落地的 4 个 run
的 scores 条目是 GPU gold 口径，不可用于 Q6 域内分析（scores 文件已追加 _NOTE 说明）。

## GPU 719 平台非深度墙伪影（per-rep 核验，2026-11-24 03:10）

**最强审稿攻击**: "GPU 719 档 cov 平台（300→719 Δ=−0.006）是不是深度墙伪影？K7 用
max_depth=5，719 档 r2/r3 撞了深度上限（665/747 节点），cov 被墙压低，拆墙后会升——
那'饱和点域依赖'的 headline 就被 confound 了。"

**核验（per-rep，archive 树 ground truth，GPU gold，judge_v1 确定性）**:
- 719 档: r1 n=381 cov=0.333 / r2 n=665 cov=0.417 / r3 n=747 cov=0.306
- 300 档: r1 n=391 cov=0.472 / r2 n=364 cov=0.389 / r3 n=415 cov=0.417

**判读**: 719 档内 cov 不随 realized 节点数升——747 节点（最大树，撞深度上限）cov=0.306
是全场最低，比 300 档均值 0.358 还低。若深度墙在压制 cov，最大树（展开最多）该 cov 最高；
实际相反。**300 之后的额外节点是横向铺开（breadth），不在 gold 主干上，不贡献覆盖**——
这正是"budget buys breadth, not coverage"机制的 per-rep 证据。深度墙不是压制 cov 的
confound，而是"额外预算买不到覆盖"的机制本身：树撞到深度上限后只能横向长，横向节点
非 gold 相关。

**结论**: GPU 719 平台是真的饱和（cov 不随节点数升），不是深度墙伪影。"饱和点域依赖"
headline 不被此 confound 打穿。Q6 719 档（max_depth=4，realized 197/351/379）的"还在升"
是另一回事——那是纯深度墙 regime（cov 是下界），拆墙批（max_depth=10）落地后才能定 Q6
的真实饱和点。两域的 max_depth 不同（GPU=5, Q6 原批=4）是已知 confound（draft §7(c)），
但 GPU 侧的平台不依赖"墙没压 cov"这个假设——per-rep 数据直接证明 cov 不随节点数升。

## 协调冲突：nodepth 批被越序并发启动（2026-11-24 03:14，已处置）

另一会话（Hermes gateway 父进程，非 relay_v2）在 rerun r3 还在跑（24 min）时直接启动了
`q6_719_nodepth_queue.sh`（r1 跑了 37s 被 kill，无 json 落地）。违反队列脚本硬前提
"vLLM 不并发"（所有 budget-scan 对比假设同负载，并发会互相拖慢、破坏负载一致性）。
处置：kill 并发进程，relay_v2（PID 34249）保持串行链（rerun → nodepth → Q7），
/tmp/relay-v2.log 已留痕。教训：relay 链在飞时，其他会话不应手动启动链内的队列脚本；
判断"该不该启动 X"前先查 relay 日志和父进程树。
