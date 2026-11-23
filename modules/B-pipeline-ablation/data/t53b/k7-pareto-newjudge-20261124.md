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

### 分箱值修正（2026-11-24 04:52 · 数字审计）
draft §7 (d)(i) 的分箱值 0.261/0.317/0.361/0.361 与统一口径重算不符。重算（30 棵 GPU 树：K7 15 用 /tmp/cov-nn-verify.json（archive 树 judge_run 重算，同 36-unit gold），rep-scan 15 用 scores json cov + 真实树 len(nodes)（核验 scores n_nodes 与真实树节点数 15/15 完全一致，无 off-by-one））：
- 0-200: 0.2500 (n=12) / 200-400: 0.3248 (n=13) / 400-600: 0.3611 (n=3) / 600-800: 0.3611 (n=2)
- cor(cov, realized_nodes) = +0.5627 (t=3.60, df=28)
高两箱和 cor 与旧值一致；低两箱旧值（0.261/0.317）来自之前 cov 来源混源的算法，已修正。平台位置（~400 realized 节点）和 cor 不变。draft commit 9202a15d1。

### Q6 719 per-rep 映射重验（2026-11-24 04:54 · 正确解释器 /usr/bin/python3）
judge_run + Q6 gold（46 units）+ 真实树 len(nodes)：r1 n=351 cov=0.1739 / r2 n=379 cov=0.1957 / r3 n=197 cov=0.1304。
- 确认 draft 的节点数→cov 映射（197→0.130 / 351→0.174 / 379→0.196）正确（719 档内 cov 随 realized 节点数单调升）。
- 719 档 tier mean = (0.174+0.196+0.130)/3 = 0.167 ✓（与 draft 一致）。
- 注意：compaction 摘要里的 "r1=0.130, r2=0.174, r3=0.196" 是 rep 标签错位（按节点数顺序贴了 rep 号），实际 r1=351, r2=379, r3=197。draft 用的是节点数→cov 映射（非 rep 标签），所以 draft 本身正确。
- 第一次后台跑用错解释器（系统 python3 无 sentence_transformers），换 /usr/bin/python3（队列脚本同款）成功。

## 全文口径一致性扫描 (2026-11-24 05:05, commit 6d95ac20b)

era confound 降级后做全 draft 扫描 (nominal 档标注的 depth/cov 声明逐一核对上下文是否已口径化)。发现 3 处漏网:
1. abstract "719 buys ~700 nodes vs ~380 at 150" — nominal 档 max-rep 对比 (747 vs 392), pre-clamp 下 nominal 标签与 realized 不单调对应 (150 档 max 392 > 719 档 min 381), 且与同段已改好的 realized 轴声明矛盾 → 改为 "realized node count spans 103–747 across the GPU tiers (pre-clamp soft cap...)" (K7 ground truth: min 103 @50-r1, max 747 @719-r3)。
2. §4.3 provenance note "rises to 300 then plateaus" — nominal 档表述 → 改为 "rises toward the nominal-300 tier (where realized counts first reliably reach the ~400-realized-node plateau) then plateaus on the realized-node-count axis"。
3. §4.3 breadth-vs-depth "~700 nodes (tier 719) vs ~380 (tier 150)" — 同 1 的 nominal 对比 → 改为 103–747 span + pre-clamp 重叠标注。
另: 初版修复里 "~120–460 realized nodes" 的 nominal→realized 映射不干净 (pre-clamp 下 100 档 123–314 与 300 档 364–462 重叠, 区间端点混两批) → 删掉伪精确映射, 改标 pre-clamp 重叠。
扫描后: 括号差 0, 0 TODO, 98147 字符。draft 现无 nominal 档口径的承重声明残留。

## §4.4/§6 detector-robustness 数字独立重算 (2026-11-24 05:12)

gap-rate-anova-rep-scan.py + gap-detector-domain-bias.py 重跑 + 独立重算 ANOVA (per-run, n=5/档):
- 现用 8-pattern tier means: 0.0992/0.1001/0.1075 ✓ (draft 0.099/0.100/0.107)
- spread/pooled_sd = 0.15 = 6.5× ✓; ANOVA F(2,12)=0.0360 ✓ (draft 0.036)
- 扩展 22-pattern per-run: 0.3896/0.4151/0.4362 ✓ (draft 0.39/0.41/0.44); ANOVA F(2,12)=1.0175 ✓ (draft F=1.02)
- claim-field (监控轴) per-run: 现用 0.0896/0.0902/0.0961 ✓ (draft 0.090/0.090/0.096), F=0.021; 扩展 0.1051/0.1062/0.1139 ✓ (draft 0.105/0.106/0.114), F=0.0333 ✓ (draft F=0.033)
- **F=0.033 口径澄清**: 是 extended 检测器下 claim-field 的 ANOVA (0.0333); pooled 现用 = 0.036, pooled 扩展 = 1.02。draft 原文 "claim-field rate stays flat under both detectors (F=0.033)" 里 0.033 只对应 extended 侧, 现用侧 claim-field F=0.021 (同样 flat, 结论不变)。
- finding2-field-decomposition.py 重跑: nat 0.0162 ✓ / soc 0.0261 ✓ / gpu claim 0.0925 (draft 0.0921, 漂移 0.0004, 语料快照 n 19→18)
- 6 个 `research/*.py` 脚本引用全部解析到 modules/B-pipeline-ablation/research/ ✓
- 结论: detector-robustness 节全部承重数字对账通过, 无实质漂移。

## 剩余数字独立重算 (2026-11-24 05:15) — 数字审计真正全 draft 覆盖

- **r=0.98 (depth~node count)**: K7 15 棵口径 r=0.9812 ✓ (draft 未标 n, 现澄清 = K7 15; rep 15 单独 r=0.889, 30 棵合并 0.944)。depth 分布 12@0.6/16@0.8/2@1.0 ✓ 与 draft 一致。
- **2.2× 方差探针 (300 档)**: rerun sample sd=0.0673 ✓ / orig 0.0304 ✓ / ratio 2.21 ✓ (draft 用样本 sd, 总体 sd 会差 15%)。
- **2.2× (719 档)**: rerun sample sd=0.0648 ✓ / ratio vs 0.0290 = 2.23 ✓。
- **ρ=0.488 (soc 内 gap~node count, honest boundary)**: 83-run 语料 soc 27 run 重算 ρ=0.4939 (漂移 0.006), t=2.84 → p≈0.009 ✓ (draft p=0.010)。
- **r=0.861 (self-judge 旧 LLM-judge cov 轴)**: 历史轴, 旧 judge 已弃用, 不可重算 — draft 已标 "with an older LLM-judge cov axis", 口径正确。
- **0.8× (retrieval_rate 下界)**: 定性上界声明 (~20% 疑似误标), 非精确统计量, 无需重算。
- 结论: draft 全部承重数字 (核心曲线/cor/分箱/控制臂 9 统计量/difficulty 梯度/L4 0/21/detector-robustness F 值/方差探针/depth 相关/soc boundary) 全部对数据源独立重算通过; 唯一不可重算项 (r=0.861) 是已弃用历史轴且 draft 已正确标注。

## 红队复审 (era confound 降级后, 2026-11-24 05:15, commit ef3dba43f)

旧 red team (8 质询) 在 era confound 降级**之前**做的, headline 已变 (nominal ~300 平台 → realized ~400 平台 + pre-clamp caveat), 最狠一刀落在新口径上。聚焦重审降级后 headline:

**最狠质询**: "平台在 ~400, 但平台段 (400-600 箱 + 600-800 箱) 只有 n=3 + n=2 = 5 棵; 顶部两箱均值差恰好 0.0000, 而全 30 棵 run-to-run 噪声底 sd=0.078 —— 两箱相等在噪声范围内, 你的平台是 5 个点的形状声明, 不是受控估计。"

**核验 (source ①, /tmp/gpu30-unified.json)**:
- 平台段 5 棵: 415→0.4167 / 423→0.3611 / 462→0.3056 / 665→0.4167 / 747→0.3056
- 400-600: n=3 mean=0.3611 sd=0.0556; 600-800: n=2 mean=0.3611 sd=0.0786
- 两箱差 0.0000 vs 噪声底 0.0779 → 确实在噪声范围内
- cor=+0.563 (df=28) 用的是全部 30 棵, 承载"上升"部分; "走平"是弱的一半

**防御**: 诚实降级落盘 (draft §7 data note (d)(i) 补 plateau-segment caveat: "flat top is a shape statement at n=5, not a controlled estimate — the cor carries the rise, the plateau's flatness is the weaker, low-n half of the claim")。claim 本身没改 (平台位置 ~400 不变), 只把强度标清楚。
**abstract 检查**: abstract 说 "plateaus near the same ~400-realized-node point" 并指向 §7 data note (d) — caveat 在正文, abstract 不超正文强度, 通过。
**其余质询 (降级后口径)**: 数字全过 (本轮数字审计) / pre-clamp 已全 draft 口径化 (本轮 3 处修复 + 一致性扫描) / 跨域 confound 已标 "not a clean same-budget different-domains" / 决定性测试已排 (nodepth 在跑 + Q7) — 无新缺口。

## nodepth 分析脚本落地前验证 (2026-11-24 05:16)

r1 进度: total 661/719 节点 (round 4, gain=0.950, streak=0, 还在扩展) — max_depth=10 下深度墙未 binding, 大概率以 max_nodes=719 停止 (干净测试)。
脚本 q6_719_nodepth_analyze.py 落地前验证 (用原批 run json):
- run json 结构: 有 rounds key, rounds[-1] 含 gain/frontier/low_gain_streak ✓ (脚本 d["rounds"][-1] 访问路径不会崩)
- judge_run n_nodes_raw == 真实树 len(nodes) (351=351) ✓ (与之前 Q6 719 重验一致)
- budget binding 检查 (max realized < 700 → 非干净测试) 能处理 max_nodes hit 场景 ✓
- 跨域分箱用 q6-scan-scores.json 原批 cov (300 档是 cache-shared 0.1304, draft 用 rep-isolated 0.138 — provenance mix 已在 draft 标注, 形状结论 robust)
- 结论: 脚本就绪, r1 落地后直接跑, 不需要再摸索。

## nodepth 脚本 gold 标度 bug 修复 (2026-11-24 05:20, commit 见 git log)

**发现**: nodepth 分析脚本跨域分箱用 q6-scan-scores.json 的原批 cov — 其唯一值 {0.0, 0.0278, 0.0556, 0.0833} = {0/36, 1/36, 2/36, 3/36} = **36-unit 标度 (GPU gold 跨域打分)**, 不是 Q6 46-unit in-domain 标度。拆墙批 cov 是 judge_run(Q6 46-unit gold) — 两种标度混在一个分箱里, r1 一落地跨域形状对比 (平台 vs 上升) 直接报废。
**修复**: 数据源换成 q6-gold-rescore.json (46-unit in-domain 重评: 1/46=0.0217, 6/46=0.1304, 8/46=0.1739, 9/46=0.1957 干净整数), n_nodes 与真实树 15/15 一致 (无 off-by-one)。dry-run + 模拟分箱验证通过 (15 原批 46-unit + 3 假拆墙 → 400-800 箱正确出现, delta_xd 可算)。
**附带新信息 (46-unit 标度下 Q6 现有 15 棵树的 realized 轴)**:
- 分箱: 0-100: 0.058 (n=3) / 100-200: 0.087 (n=7) / 300-400: 0.1522 (n=5) / 400-800: 无数据 (nodepth 补)
- cor(cov46, realized) = 0.8423 (GPU 30 棵参照 0.563) — Q6 域内 cov 随 realized 的上升比 GPU 陡
- 注意 100-200 箱 n=7 含 719-r3 (197 节点, 撞深度墙) — 箱内混合 nominal 档, 形状结论 (仍升) robust, 精确箱均值待 nodepth 落地后重算
- 这是"Q6 到 719 仍升"声明在 realized 轴 + 正确 gold 标度下的第一次完整核验 (之前只有 tier-mean 口径)。

## 系统性 gold 标度审计 (2026-11-24 05:22) — nodepth bug 的模式排查

nodepth 脚本 36/46-unit 混箱 bug 是个模式, 系统性排查谁还在混:
- **引用 q6-scan-scores.json (36-unit 跨域标度) 的脚本**: q6_full_curve / a3_cross_domain_metacog / q6_rerun_variance_check / q6_rescore / rescore_q6 / q6_rerun_n3_verdict / q6_rerun_postlanding_analysis 等 — 逐一核用途, 这些脚本做的是跨域分析或 rescore 生成, 用 36-unit 是对的 (cross-domain 声明本来就该用 GPU gold)。
- **Q7 分析脚本**: judge_run 现算 (in_cov=Q7 52-unit, cross_cov=GPU 36-unit), 不读 scores 文件 — 无混淆 ✓。
- **draft 数字源核对**:
  - in-domain Q6 tier means (0.058/0.073/0.087/0.138/0.167): 46-unit, 源 q6-gold-rescore.json ✓ (300 档 0.138 = rep-isolated rerun 0.1377, 其余 4 档 = 原批, provenance mix 已在 draft 标注)
  - cross-domain near-zero (0.009/0.009/0.019/0.046 + 719 reps 0.0/0.083/0.056): 36-unit, 源 q6-scan-scores.json ✓ 重算全过 (0.0093/0.0093/0.0185/0.0463; 719 0.0/0.0833/0.0556)
- **结论**: 标度混淆只在 nodepth 脚本一处 (已修, commit f55a121ec), draft 和 Q7 脚本都干净。两个 scores 文件各用各的: q6-scan-scores.json = 36-unit 跨域打分, q6-gold-rescore.json = 46-unit in-domain 重评 — 名字相近但标度不同, 是这次 bug 的根因, 后续新脚本引用时注意区分。

## nodepth 脚本判定阈值修: 0.01 固定阈值 → 噪声底 (2026-11-24 05:24)

**发现**: 脚本两处判定 (墙对照 delta / 跨域 delta_xd) 用固定阈值 0.01, 但原批 15 棵 cov 的 pooled sd=0.0496 → delta 的 1×sd ≈ 0.031-0.035 (n=3 拆墙 vs n=15 原批)。0.01 < 噪声底 — r1 落地后若 delta 落在 (0.01, 0.031) 区间, 脚本会判"仍升/墙压制", 实际是噪声内的波动。
**修复**: 两处阈值都换成数据驱动的 1×sd (墙对照: 原批 719 三 rep [0.1304, 0.1739, 0.1957] 的 sd → 1×sd≈0.035; 跨域: low 段 cov 的 sd → 1×sd≈0.031), 判定文本带出实际阈值。
**影响**: 不影响数据, 只影响 r1 落地后的判定 robustness。若拆墙批 delta 真 > 0.035, 判定不变; 若在 (0.01, 0.035), 旧脚本误判"仍升", 新脚本正确归"噪声内/平台化"。

## D 方法论三问 (2026-11-24 05:25) — judge 客观性 / general 合法性 / 成本+信息获取

D 三问 (原文): ①机械 judge 域特定 (特殊化), 怎么保证客观, 给其他 AI 跑一遍吗? ②不 general 的 bench 能有什么 general 发现, 怎么证明? ③别的 workshop 都要跑不同 bench, DRB judge 付费 API, 深度推理和信息获取问题似乎没解决?

**回答落盘** (qanda-ledger 2026-11-24 节):
- Q1: judge 机制 general (embedding+确定性+无 self-bias), 域特定的是 gold。"给其他 AI 跑一遍"若指 LLM 交叉打分 = 降级回 LLM judge, 方向反。真 gap = 独立 gold 构建对照没做。
- Q2: general 发现 = 跨域复现的形状 (饱和点存在+域依赖), 不是单域绝对值; 合法性 = 同机制换 gold 比形状。潜台词成立: general 用人工 gold 劳动换来, 每域重建。
- Q3: 机械 judge 边际成本≈0 (judge_v1 只有 model.encode, 零 LLM/API, 已 grep 验证); gold 构建成本随域线性。信息获取 = 真 gap (judge 测输出树不测检索质量, retrieval_rate channel-outage 时盲)。

**实证补强 (进行中)**: judge_objectivity_perturbation.py — 不答"gold 对不对"(需独立 gold 对照), 答"给定 gold, cov 对 gold 扰动/阈值选择是否稳健":
- A. gold 随机删 10% (5 seeds) → |Δcov| vs 噪声底
- B. cos_threshold 0.75±0.05 → |Δcov|
- C. 承重 cor(cov, n_nodes) 在 gold 扰动下是否保持
- 对象: GPU K7 15 棵 archive 树。后台跑 (bge-m3 加载慢), 结果待回填。

## judge 扰动测试部分结果 (2026-11-24 05:42, B 段在跑, 全结果待回填)

**A 段 (gold 删 10%, 5 seeds) 完成**: max|Δcov| = 0.0173 vs 噪声底 0.0554 (1/3 sd) → cov 对 gold 构建细节 (删 10% unit) 不敏感。
**B 段 (阈值扫描) 第一个点**: thr=0.65 (比 0.75 低 0.10) → cov 0.0981→0.4963, **Δ=+0.398 (5 倍)**。
**关键发现**: 威胁机械 judge "客观性"的不是 gold 构建 (扰动只动 1/3 噪声底), 是 **cosine 阈值这个自由超参** (±0.10 动 7 倍噪声底)。D Q1 的答案重心因此移动:
- "机械 judge 客观" 的正确表述 = 给定 (gold, 阈值), 分数确定性+可复现+无 self-bias ✓
- 但阈值是设计者选的超参, 且 cov 对它极端敏感 → **阈值选择本身是新的 designer 自由度**, 和 gold 构建同级的潜在偏差点
- 防御: 阈值 0.75 不是拍的 — 需查它的 provenance (calibrate_cos 函数? 文献值? 网格搜索?), 若是有校准程序的, 客观性声明升级为 "阈值由校准程序固定, 非人工挑选"; 若是拍的, 必须补阈值敏感性分析进 draft
- 对承重结论的影响: 平台/上升是**形状**结论, 阈值变化会整体抬升 cov 但形状 (分箱单调性) 是否保持 = B 段全结果出来后才能判 (0.65 下若分箱仍单调升, 形状结论 robust; 若分箱乱序, 形状结论是阈值 artifact)

## 扰动测试基线 bug 修正 (2026-11-24 05:48, commit 77a0b163e)

**发现**: 首版扰动脚本基线误用 thr=0.75, 但 judge_v1 官方 COS_THRESHOLD=0.70 (注释: "标定: 0.80 覆盖塌(0.015), 0.70 覆盖 0.350 且 per-run 区分度好(0.11-0.56)")。0.75 基线 0.0981 vs 官方口径 0.3185 (cov-nn-verify.json, 独立重算 0.3185 复现 ✓) — 差 3.2 倍, **首版 A 段"gold 扰动不敏感"结论作废** (在 0.75 下算的, 0.75 本身已偏离标定值, 扰动叠加在错误基线上)。
**修正**: 基线 + A 段 + C 段全换 0.70; B 段阈值扫描改 0.70±0.05 (0.65/0.75/0.80/0.85)。重跑后台 (PID 95682)。
**已验证进 draft 的数字 (0.70 口径, 独立复现 ✓)**: 0.65→0.496 / 0.70→0.3185 / 0.80→0.015 (judge_v1 标定注释) — 阈值 0.15 窗口内 cov 摆 30 倍。这是 D Q1 的核心实证: 机械 judge 的客观性威胁不在 gold 构建, 在阈值这个标定超参; 0.70 有标定 provenance (单语料选择), 跨域/跨阈值绝对 cov 比较是 threshold-scoped。
**教训**: 扰动/敏感性测试的基线必须用生产口径 (judge_v1 默认参数), 不能随手取整 — 0.75 看着"差不多"实际差 3.2 倍, 因为 cov 在阈值上是悬崖不是斜坡。

## nodepth r1 拆墙 cov 初步信号 (2026-11-24 05:48, n=1 待 r2/r3)

r1 落地 (max_nodes=719 触发, round 5, gain 0.965, frontier 269 非空, streak=1):
- **cov=0.1304** (46-unit Q6 in-domain gold, judge_run 现算) / struct=1.0000 (depth 满分: 树实际 6 层 L1:6/L2:27/L3:88/L4:271/L5:269/L6:58, min(6/5,1.0)=1.0, GOLD_DEPTH=5; **不是**展开到 max_depth=10 — 上限没撞到, round 5 撞满 719 节点预算停止) / total=0.5652
- 对照原批 719 (被 max_depth=4 墙切断, realized 197/351/379): 均值 cov=0.1667, per-rep 0.1739/0.1957/0.1304
- **Δ vs 原批均值 = -0.0363** (拆墙 r1 低于原批均值); vs 原批 r1 (realized 351) = -0.0435
- realized 节点数: 原批 r1=351 (墙切) → r1 拆墙=719 (满预算), **节点翻倍 cov 反降**
- struct 满分 (1.0) 但 cov 没升 → 结构深度 ≠ 内容覆盖, 模型把树展开很深但没多覆盖 gold 内容

**初步判定 (n=1, 待 r2/r3 确认)**: 墙虽 actively binding (gain 高 + frontier 非空 + streak 低), 但深度展开对 cov 贡献小——原批 0.1667 近似真实值, 不是"被墙压制的下界"。这**修正** draft 跨域段"Q6 到 719 仍升 (墙切断下界)"的叙事: 拆墙后 cov 不升反落在原批下沿, 说明 719 档 cov 主要由内容命中 (检索/生成质量) 驱动, 非由 realized 节点数/深度驱动。
**噪声底对照**: 原批 3 rep cov [0.1739,0.1957,0.1304] sd≈0.034, Δ=-0.036 略超 1×sd 但单 rep 不定论。r2/r3 落地后看 3 rep 均值是否系统性低于 0.1667 (若 r2/r3 也 <0.1667 → 墙对 cov 贡献小的结论成立, draft 叙事需改; 若 r2/r3 回升 → r1 是离群, 维持原叙事)。

## nodepth r1 命中集分析 (2026-11-24 05:50, 离散标度 + 零和洗牌)

**cov 是离散量**: 1 unit = 1/46 = 0.0217。原批 719 三 rep = 6/46, 8/46, 9/46 (sd≈0.034 ≈ 1.5 unit)。
**命中集对照 (thr=0.70)**:
- 原批 r3 (realized 197, 墙切): 6/46 = [6,8,14,21,24,33]
- 拆墙 r1 (realized 719, 满预算): 6/46 = [0,8,9,14,21,25]
- 交集 3/6 ([8,14,21]); 拆墙新增 3 ([0,9,25]), 丢失 3 ([6,24,33])
**解读**: cov 数值相同 (0.1304) 是离散计数巧合, 内容不同。深度展开 3.7x 节点 → 净覆盖增益 = 0 (新增 3 - 丢失 3)。
丢失的 3 个 unit 可能是不同随机轨迹 (不同 cache key/seed) 的 run-to-run 方差, 也可能是深度展开挤占了广度探索。n=1 不能区分两者, r2/r3 落地后可看: 若拆墙批 3 rep 命中集系统性包含原批命中集超集 → 深度纯增益; 若继续零和洗牌 → 深度对 cov 无净贡献的结论成立。
**噪声底口径修正**: 原批 sd 0.034 应表述为 ≈1.5 unit (离散分辨率 0.0217), 不是连续量 sd。

## 阈值形状 robustness 全结果 (2026-11-24 05:54, threshold-shape-robustness-20261124.json)

K7 15 棵, 4 阈值:
| thr | mean | cor(cov,nn) | 0-200 | 200-400 | 400-600 | 600-800 |
|-----|------|------|-------|---------|---------|---------|
| 0.65 | 0.4963 | 0.802 | 0.407(n=6) | 0.544(n=5) | 0.528(n=2) | 0.611(n=2) |
| 0.70 | 0.3185 | 0.601 | 0.241(n=6) | 0.367(n=5) | 0.389(n=2) | 0.361(n=2) |
| 0.75 | 0.0981 | 0.388 | 0.069(n=6) | 0.133(n=5) | 0.083(n=2) | 0.111(n=2) |
| 0.80 | 0.0148 | 0.132 | 0.005(n=6) | 0.028(n=5) | 0.028(n=2) | 0.000(n=2) |

**结论**: cor 随阈值单调塌 (0.80→0.13, 6 倍); 低预算上升段 (前两箱) 4 阈值全单调升, 但**幅度超噪声底 (sd≈0.078, 30 树) 只在 0.65/0.70** (1.76×/1.62×), 0.75/0.80 下单调但**噪声内** (0.82×/0.30×) → 上升**单调**跨全阈值, **可检测**只在低阈值侧 (≤0.70); 高预算 top 段 (后两箱, n=2/2) 在**任何阈值下都不是稳定平台** — 0.65/0.75 还在升 (0.528→0.611 / 0.083→0.111), 0.70/0.80 在降 (0.389→0.361 / 0.028→0.000), 方向随阈值翻转, 平坦性在 3/4 阈值噪声内 (0.36×) → **平台 claim 任何阈值下都无显著性** (n=5 形状声明, 平坦性经不起噪声底, 更经不起 ±0.05 阈值移动)。draft §6 已写 (05:55 commit); 06:10 修"非单调"逻辑空话; 06:15 补噪声比 (skill 第 10 条: 统计声明带组内 sd + 显著性, "robust"不带噪声比正是它防的失败模式)。
**含义**: 若红队问"你的平台结论是不是阈值拍的"——答: 上升在单调性意义上守得住 (4 阈值全单调), 但可检测性只在低阈值侧 (≤0.70 超噪声底); 平台在**任何阈值下都无显著性** (n=2 箱 + 平坦性噪声内 + 方向随阈值翻转), 我们已把平台 claim 限定为 "no further measurable rise" 而非 "exact plateau at 400", 且该限定本身在 0.65 阈值下也不成立 (top 段还在升)。

## 命中集对照修正 (2026-11-24 05:58, nodepth-r1-vs-orig-hits-20261124.json)

**推翻上节"零和洗牌"机制解读** (那是拿最差一对 vs orig-r3 3/6 当代表):
- 原批 rep 间重叠: r1∩r2=6/8, r1∩r3=3/6, r2∩r3=5/6 (50-83%)
- nd-r1 vs 原批: vs r1=4/6 (67%), **vs r2=6/6 (100%, 严格子集!)**, vs r3=3/6 (50%)
- nd-r1 的 6 unit 全部 ⊂ orig-r2 的 9 unit → 719 节点展开没有产生 orig-r2 (379 节点) 之外的任何 gold unit
**修正后解读**: nd-r1 是 run-to-run 方差包络内的又一个 run (重叠率与原批 rep 间同量级), 不是"深度展开改变了覆盖内容"。主结论不变 (深度对 cov 无净增益: nd-r1 6/46 < 原批均值 8/46), 但机制表述从"零和洗牌"改为"方差包络内, 无超集新增"。
**丢失的 3 unit (vs orig-r3) 性质**: 缓存命中率 h / 电价 / 握手 RTT 数 — 都是具体参数值 unit; 新增 3 unit: P99 合规成本 / 计费模式 / 单 POP 最小带宽 — 也是参数值 unit。内容类型无系统性差异, 支持"方差"而非"深度偏好"。
**draft 已同步修正** (§4.3 机制段改为 subset + variance-envelope 表述)。

## Q7 分析脚本落地前验证 (2026-11-24 06:00)

q7_full_analysis.py 在 11h 长杆 (15 runs) 落地前 dry-run 验证:
- 假 run 文件 (真实 GPU run 改名 q7-50-r1 格式) → 脚本 exit 0, 全 guard 工作: 空箱→None / n=1→plateau+cor=None / stop 无 stdout→UNKNOWN / cross_cov 0.2222 (GPU 36 口径合理)
- 假文件已删, SCAN 目录空, 空目录时脚本干净退出 (exit 0, 无残留 json)
- 队列脚本核验: cache 隔离 ✓ (line 30 Q6_REP=$rep), gold 标度 ✓ (line 46 gold-q7-units.json 52-unit in-domain, judge_run 现算), 无 Q6 式混用
结论: 11h 落地后分析不会报废。

## 扰动测试全结果 (2026-11-24 06:02, judge-perturbation-20261124.json 最终版, 0.70 基线)

- 基线: mean cov 0.3185 (sd 0.0926, 15 树)
- A 段 (gold 删 10% × 5 seeds): max|Δ| = 0.0215 < 1×sd → 对 gold 构建不敏感
- B 段 (阈值 0.65/0.75/0.80/0.85): max|Δ| = 0.3185 = 3.4×sd; 0.85 → cov 0.0000 完全塌 → 阈值是承重超参
- C 段 (cor 在 gold 扰动下): 0.6011 → 0.6413 (Δ+0.040) → 形状结论对 gold 扰动 robust
- 综合: 威胁客观性的不是 gold 构建 (1/4 噪声底), 是阈值 (3.4× 噪声底 + 悬崖形状)
- draft §6 已更新为最终结论 (删 "is running; first pass void" 过时句)

## 数字口径审计 (2026-11-24 06:05, workshop-number-audit 16 条, 22 项核验)

本轮进 draft/K7 的新数字全部对数据源独立重算: **22/22 ✓** (唯一初判 ✗ 是核验脚本字段名笔误 mean vs mean_cov, 数据本身 0.85→0.0 ✓)。
- 扰动 A/B/C 段 + 基线 (judge-perturbation-20261124.json): 0.0215/0.3185/0.6011→0.6413/0.3185·0.0926·15 ✓
- 阈值悬崖 4 点 + cor 4 点 + 上升单调升/top 段方向翻转 (threshold-shape-robustness-20261124.json): 0.4963/0.3185/0.0981/0.0148 + 0.802/0.601/0.388/0.132 + 形状判定 ✓ (06:10 修正"非单调"逻辑空话表述)
- nodepth r1 命中集 (nodepth-r1-vs-orig-hits-20261124.json): 6/46·n=719, nd⊂orig-r2 (6⊆9 严格子集), 重叠 4/6·6/6·3/6, 原批 rep 间 6/8·3/6·5/6, r3 n=197 ✓
- 原批 719 三 rep (q6-gold-rescore.json 46-unit): cov {0.1304,0.1739,0.1957}, 均值 0.1667, n_units_hit 6/8/9 ✓
- 6/46=0.1304 算术 ✓; B 段 0.85→0.0000 ✓
- draft 括号差 0 (760/760) ✓
**skill 15/16 条 (gold 工件 + 官方口径)**: 本轮所有 cov 数字钉死工件 — 46-unit (q6-gold-rescore.json, nodepth/原批 719) vs 36-unit (GPU gold, 扰动/阈值悬崖 K7 15 树) vs 52-unit (Q7 gold, 队列脚本); 两套标度在 draft 里分属不同段 (K7 15 树 = 36-unit GPU gold, nodepth/原批 = 46-unit Q6 gold), 无混用。
**skill 8 条 (abstract 强度)**: abstract 的 domain-dependence 声明 scoped 到 "GPU gold" + "queued 719-nodepth batch" (未把 r1 n=1 结果说成定论), 强度 ≤ 正文 ✓。
