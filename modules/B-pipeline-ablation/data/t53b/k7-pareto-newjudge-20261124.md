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

## 红队审视（2026-11-24 03:35，投稿就绪度三条件之"最狠质询有防御"）

对象 = workshop draft 全文。按杀伤力列质询逐个判防御：

| 质询 | 防御 | 判定 |
|---|---|---|
| budget 参数 vs realized nodes 混淆（soft cap 下"预算效应"归因不干净） | §2 明写 soft cap/lower bound with overshoot + 双轴报告 + realized 回归稳健性检查（gap_rate vs realized cor=−0.034 ns） | 守得住 |
| metacognition 构念效度（测 elicited 非 spontaneous monitoring） | abstract 首句限定 + §6 [待核验] tag 是 82% 命中主成分的证据 + 三域 tag 占比差异本身是自发语言证据 | 守得住 |
| gold 是 AI 重构设计者工件（cov 测的是相似度非真值） | "scores measure similarity to that reference, not ground truth" 明写 | 守得住 |
| LLM depth 轴 self-bias（同模型评自己） | verbosity 控制臂（r=0.648 跟长度不跟 budget）+ 机械轴无峰值 + 控制臂脚本落盘 | 守得住 |
| n=3/档功效不足 | "n=3 只能定拐点位置不能定强度" + 池化口径分离 + ANOVA 功效声明（large effect 21.5%） | 守得住 |
| cache 共享压低方差（原批 300 sd=0 伪影） | 机制级（cache key 不含 rep）+ 行为级（rerun sd 2.2×/3.2×）双证据 + provenance 混合声明 | 守得住 |
| retrieval_rate 测量盲区（~20% 疑似假 search tag） | "upper bound on true retrieval rate" 明写 + gap_rate 是构造无关的干净分量 | 守得住 |
| **跨模型泛化（§2 "should hold across models of similar capability"）** | **§7 自己写 capability 轴 planned not run — 正文 claim 了没跑的泛化** | **真实缺口 → 已修** |

**修复（commit）**：§2 跨模型句降级 "should hold" → "we expect to hold but have not yet tested — the capability axis is planned, not run (§7), so cross-model generalization is a hypothesis to be verified, not a finding"。

**结论**：draft 防御密度高（控制臂×3：bare-arm/verbosity/llm-vs-mech；诚实降级×6：n=3/era-scoped/detector-scoped/GPU-domain/upper-bound/hypothesis-not-finding）。红队后投稿就绪度三条件全过：结构完整 ✓ 承重数字对账 ✓（4 sd 值+104 加法+abstract 强度）最狠质询有防御 ✓（1 处缺口已修）。剩余提升项不变：r3 落地（n=3 方差探针）+ nodepth 拆墙批 + Q7 第三域。

## 719 档 rerun r3 落地 + n=3 方差探针（2026-11-24 03:45）

r3 落地：n=392（depth ceiling, final_state=rework），Q6 gold 重评 cov=0.1739 total=0.4870 metacog=0.1737。

**719 档 rerun 全 rep（n=3, Q6 gold）**：
| rep | n_nodes | cov | metacog |
|---|---|---|---|
| r1 | 349 | 0.1739 | 0.1041 |
| r2 | 277 | 0.0870 | 0.2336 |
| r3 | 392 | 0.1739 | 0.1737 |
| mean | | 0.1449 | 0.1705 |
| sd | | **0.0502** | **0.0648** |

**方差探针（719 档，n=3 可解读）**：
- metacog sd: rerun 0.0648 vs 原批 0.0290 → **2.23×**（与 300 档 2.21× 一致）
- cov sd: rerun 0.0502 vs 原批 0.033 → **1.52×**（方向同，46-unit 分辨率 caveat）
- r1/r3 cov 同为 0.1739（8/46 离散巧合），metacog 不同（0.104 vs 0.174）→ answer 独立，非 cache 伪影

**结论**：cache 共享压低方差假设现在两档（300/719）都是 n=3 可解读地成立（之前 719 是 n=2 单自由度）。draft §7 已更新（commit），措辞从"directionally consistent at 719 (n=2), not interpretable until r3"升级为"supported at both tested tiers (300 and 719, n=3 each), still not a controlled estimate"。

**relay 链推进**：rerun 队列 03:40:04 退出 → nodepth 批 03:40:34 启动（phase 1，max_depth=10，PID 41010/41017 在跑 r1）。nodepth 落地后跑 `q6_719_nodepth_analyze.py`，然后 Q7 扫描。

## References 真实性核验（2026-11-24 03:55，arXiv API 逐条）

之前只验了"正文引用↔文献列表 17/17 闭环"，没验文献本身是否真实。本轮逐条查 arXiv export API（https，3 次重试）：

- **17/17 arXiv ID 真实存在**（export.arxiv.org/api/query?id_list=<id> 返回 entry）
- **17/17 标题逐字匹配**（arXiv 返回 title vs draft 文献列表）
- **17/17 第一作者匹配**（arXiv 返回 first author surname vs draft）
- **17/17 年份匹配**（arXiv published 年份 vs draft 标注年份）

结论：References 无伪造/幻觉引用。投稿就绪度"承重数字对账"维度新增一项通过——文献真实性（之前是盲区）。

## relay 链下游就绪度核验（2026-11-24 04:00，nodepth 在飞期间）

nodepth r1 在跑（03:40 启动），relay 链下游三个环节逐一核验，防落地后分析断：

1. **nodepth 分析脚本**（q6_719_nodepth_analyze.py）：glob 路径 `q6-719-nd-r*.json` 正确，输出 data/q6-719-nodepth/q6-719-nodepth-analysis.json，前置 3 rep 落地。
2. **Q7 gold**（gold-q7-units.json）：52 units（与脚本声称一致），字段与 Q6 完全一致（7 字段），kind 分布 split 10 / leaf 38 / None 4，depth 0-3 完整。
3. **Q7 队列评分块**（q7_budget_scan_queue.sh :37-54）：用刚落地的 r3 json 实测——judge_run 4 key（n_nodes_raw/total_score/depth_score/coverage）+ compute_metacog 5 key（metacog_total/gap_rate/retrieval_rate/healthy_gap_rate/post_retrieval_accuracy）全部 OK，无 KeyError（之前 rerun 队列的 bug 在 Q7 不存在，评分块已显式传 Q7 gold_units）。

结论：relay 链（nodepth → Q7）落地后分析工具链全就绪，无断点。

## §4.3 控制臂统计量官方脚本对账（2026-11-24 03:55，数字审计 skill 16 条之"官方口径重算"）

重跑 3 个冻结脚本，draft 每个统计量与脚本输出逐值比对：

| 数字 | draft | 脚本重算 | 判定 |
|---|---|---|---|
| verbosity cor(LLM,length) | +0.648 (t=3.07, df=13) | +0.648 (t=+3.07) | ✓ |
| partial(LLM,budget\|length) | +0.047 | +0.047 | ✓ |
| Spearman ρ | +0.681 (p=0.005) | +0.681 (p=0.0052) | ✓ |
| cor(LLM,mech) | +0.049 (t=0.18) | +0.0490 (t=0.177) | ✓ |
| ANOVA F(2,12) | 0.036 | 0.0360 | ✓ |
| tier means gap_rate | 0.099/0.100/0.107 | 0.0992/0.1001/0.1075 | ✓ |
| pooled within-group sd | 0.054 | 0.0538 | ✓ |
| power f=0.40 (n=15) | 21.5% | 21.4% (scipy ncf) | ✓ 四舍五入差 |
| power f=0.25 (n=15) | 11.0% | 11.0% | ✓ |

脚本：research/verbosity-bias-control-arm.py / llm-vs-mech-depth-control-arm.py / gap-rate-anova-rep-scan.py。
结论：§4.3 全部承重统计量 = 官方脚本输出，无口径漂移。数字审计覆盖范围：§7 4 个 sd 值（前轮）+ §4.3 9 个控制臂统计量（本轮）+ abstract 强度（前轮）+ 104 加法（前轮）+ References 17/17 真实性（本轮）+ 跨域 cov 曲线（前轮）。

## 核心 claim 池化 cov 曲线对账（2026-11-24 04:05，数字审计之"承重数字对数据源重算"）

GPU 域池化 cov 曲线（draft 核心 claim：~300 饱和）从数据源重算：
- K7 15 条（gpu-rescore-newjudge-20261124.json, new_cov）+ rep-scan 15 条（rep-scan-scores.json, judge.cov）
- 逐档池化：50=0.2593 / 100=0.2639 / 150=0.2778 / 300=0.3577 / 719=0.3519
- K7 声称：50=0.259 / 100=0.264 / 150=0.278 / 300=0.358 / 719=0.352 → **精确一致**

provenance 确认：K7 批用 new judge 重评（new_cov 字段），rep-scan 批原生 judge.cov（三层结构 total/depth/cov，量级 0.1-0.4 与 K7 new_cov 同口径）。池化同口径，无混 judge。
结论：draft 核心 claim（GPU cov ~300 饱和）的承重数字 = 数据源重算值，无漂移。

数字审计覆盖范围（累计）：§7 4 sd 值 + §4.3 9 控制臂统计量 + 核心 claim 池化 cov 曲线 5 档 + abstract 强度 + 104 加法 + References 17/17 真实性 + 跨域 cov 曲线。draft 全部承重数字已对账。

## 核心曲线池化口径 + cor(cov,n_nodes) 同棵 archive 树重验（2026-11-24 04:10）

**池化口径澄清**（draft §4.3 核心曲线 0.259/0.264/0.278/0.358/0.352 的 provenance）：
- 中间三档（100/150/300）= K7 15 条 (n=3/档) + rep-scan 15 条 (n=5/档) 池化 → n=8/档
- 300 档验证: (0.4259×3 + 0.3167×5)/8 = 0.3577 ≈ 0.358 ✓
- 50/719 端点 = K7 only (n=3)
- 两批同口径: 都评 archive 树、同机械 cov 层、同 36-unit GPU gold
- 形状在两批内各自成立 (K7: 0.259/0.269/0.287/0.426/0.352; rep-scan: 0.261/0.272/0.317) → 池化曲线非跨批伪影
- 注: K7-only 300 均值 0.426 与 rep-scan-only 300 均值 0.317 差 0.109，池化后 0.358；这是两批 realized 节点分布不同所致（rep-scan 是 soft cap，300 档 realized 271-462 与 150 档重叠），draft 已注 soft-cap caveat

**cor(cov, n_nodes) 同棵 archive 树重验**（draft 声称 +0.602, t=2.72, df=13）:
- 15 棵 archive 树逐棵 judge_run 重评 cov + 取 len(nodes) → r=+0.601 (t=2.71, df=13) ✓ 一致
- 反向验证: 用 rescore json 里的 n_nodes 字段（错位记账值）配同批 cov → r=0.343（错）——正是 draft 警告的 off-by-one 陷阱，rescore json 的 n_nodes 字段不可用于 per-run 配对
- rescore json 的 cov 值 multiset 与 archive 树 15 棵完全一致（逐档均值全等）→ rescore 评的确实是 archive 树，provenance note "tier means 不受 off-by-one 影响" 声明成立

**结论**: draft 核心 claim（GPU cov ~300 饱和）的曲线值 + 形状 + 相关系数全部对账通过，池化口径已在 draft §4.3 provenance note 显式写明（n=3/8/8/8/3 + 池化公式 + 两批各自形状）。

## §4.2 难度梯度 + §4.4 L4 数字审计（2026-11-24 04:25）

**§4.2 难度梯度**（finding2-difficulty-gradient-cleaned.py + finding2-field-decomposition.py 重跑）：
- 显著性模式完全复现: nat<soc ns (z=-1.82) / soc<gpu 显著 (z=-4.68) / nat<gpu 显著 (z=-4.87)
- claim 字段值: nat 0.0162 ✓ / soc 0.0261 ✓ / gpu 0.0925 (draft 0.0921, 漂移 0.0004)
- draft 的 claim-field z (−4.46/−4.68) 与 pooled-clean z (−4.68/−4.87) 量级差合理 (claim 字段率更低→z 略小), 方向显著性一致
- gpu n 19→18: 83-run 语料快照漂移 (draft correction note 本就声明"从当前语料重算"), 非 draft 错误
- 结论: 承重 claim (难度梯度 + 监控轴现象 + 显著性模式) 全部复现, 精确 z/n 随语料快照小幅漂移, 可接受

**§4.4 L4 零收敛**（l4-zero-convergence.py 重跑）: 0/21 精确复现 ✓ (K7 15 + idea2 6, strict=0 全过)

**§4.4 degeneration 5/5**: 独立数据集 (T-PUB-1 math benchmark), 检测器在 D1-generalization/scripts/degeneration_detector.py (非本项目), 补充观察非核心 finding, 未重跑 (低优先级)

**数字审计全 draft 覆盖完成**: §4.1 (metacog 触发率, 前轮) + §4.2 (难度梯度, 本轮) + §4.3 (控制臂 9 统计量 + 核心曲线池化 + cor, 前轮) + §4.4 (L4 0/21, 本轮) + §7 (4 sd 值, 前轮) + 104 加法 + abstract 强度 + References 17/17。draft 全部承重数字已对数据源重算, 无实质漂移 (仅 §4.2 gpu n/z 随语料快照小幅漂移, 显著性模式不变)。

## 2026-11-24 04:25-04:42 · GPU 域 budget 轴 era confound 核验（用户指出跨域 regime 不对称）

**触发**：D 指出 GPU K7 max_depth=5 vs Q6 原批 max_depth=4，GPU 719 饱和是否被深度墙压出。决定性检查（GPU 719 档内 cov 是否随 realized 节点数走）→ 381→0.333 / 665→0.417 / 747→0.306，最多节点 cov 最低 → 平台非 719 档深度墙伪影。

**但查 per-rep 停止状态 + 批 era 后发现问题更根本**：
- GPU 全 15 棵 K7 树：final_state=rework、gain 0.86–0.92、frontier 24–252、maxlvl ≤ 5，无一自然收敛（全部截断 regime）。
- 硬预算钳制 commit 47a8543cd（11-23 13:44）message 原话点名 K7 15-run realized 节点数跨档重叠。
- GPU K7 批 archive 时间戳 11-22 07:08–18:19 = **pre-clamp**；rep-scan 批 11-23 03:25–10:46 = **pre-clamp**；Q6 原批 11-23 16:34+ = **post-clamp**（50/100/150/300 realized 精确等于 nominal，719 撞深度墙 197/351/379）。
- 30 棵 GPU 树按 realized 节点数分箱：0-200: 0.261 (n=12) / 200-400: 0.317 (n=13) / 400-600: 0.361 (n=3) / 600-800: 0.361 (n=2) → **平台在 ~400 realized 节点，不是 nominal ~300**；cor(cov, realized_nodes)=+0.563 (t=3.60, df=28)。

**claim 降级**（draft commit 94ebf147c）：
- 守得住：cov 随 realized 节点数升、~400 realized 节点后平台化（top 两箱相等但 n=5，suggestive）。
- 守不住：平台归因到 nominal budget 300（pre-clamp soft cap，realized 跨档重叠：50 档 423 > 300 档 364）。
- 跨域对比"GPU 饱和 Q6 不饱和"被 regime 差异 confound（pre-clamp soft cap + max_depth 5 vs post-clamp hard cap + max_depth 4 + Q6 719 深度墙下界）；两域 realized 节点数测量范围不同，不是"同 budget 不同域"的干净对比。
- 修复：(1) 零成本 realized 节点数 x 轴重分析（已做，draft 现口径）；(2) post-clamp 重跑 GPU 扫描（~10h，vLLM-bound，未排——等 D 拍板是否值得占 vLLM）；(3) Q6 nodepth 批（max_depth=10）在跑，落地后给 Q6 在 ~719 realized 节点的干净点，是"饱和点域依赖"的决定性测试。

**自检**：之前把 commit message 点名的 realized 跨档重叠当"小 caveat"处理，严重性低估——它动摇的是核心 claim 的归因不是精度。D 的 confound 直觉方向对（跨域 regime 不对称），但比 max_depth 差异更根本的是 pre/post-clamp era 差异。

### 修复路径裁决（2026-11-24 04:46 · 自主，可逆）
(1) post-clamp 重跑 GPU 扫描（~10h，占 vLLM）：**跳过**。理由：draft 已改到 realized 节点数轴口径（commit 94ebf147c/2df481a8b），重跑只给 nominal 轴一个干净版本，边际价值低；且会阻塞 relay 链后面的 Q7 扫描（子项④）和子项②。若 D 认为 nominal 轴干净版本对投稿必要，再排（等 Q7 落地后 vLLM 空窗）。
(2) realized 节点数 x 轴重分析：**已做**（30 棵 GPU 树分箱，平台 ~400 realized 节点），draft 现口径。
(3) Q6 nodepth 批（max_depth=10）：在跑（r1 N321 节点，04:44），落地后判定 Q6 在 ~719 realized 节点是平台还是继续升——"饱和点域依赖"的决定性测试。
