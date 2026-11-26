# origin: ai
# nat 278 节点树失败模式分类：a（停止太早）vs b（维度盲区）

数据源：runs-s5-sm-nat.json · checkpoints/sm-nat-r0..r28.json · s5_state_machine.py · s5_pipeline.py（2026-11-26）

## TL;DR
- 停止原因 = **max_depth=4 硬顶**（s5_state_machine.py:1250-1252 结构性 break），不是 J_necessary 软判断（末轮 gain=0.898、low_gain_streak=0），不是 rounds 耗尽（主循环无 max_rounds；其后 24 个 ckpt 轮是 verify-only 批次）。
- gold 3（LFU 频率表老化机制）= **树内 0 节点** → b（维度没触发）；gold 5（1%/天 → 100 天 1/λ 量级）= **树内有节点**（N17/N247/N262 均 verified）但 P4 选错口径 → P4 综合丢失。
- 判定：**b 主导 + P4 丢失，a 被证据否定**。根因：frontier 只取最深层 + 逐层 prompt 父节点局部 → 机制维度（应挂 N3/N13/N14）在树到 L4 后结构性不可达。

## §1 树结构统计
- 总节点 278 · final_state=`verify`（非 `stop`）· decompose rounds_log=1 · leak_hits=0
- level 分布：**L1=5, L2=23, L3=71, L4=179**（lv_max=4 = cfg.max_depth 默认值，CLI 无 max_depth 覆盖入口）
- status 分布：verified=181, pending=70, degraded=25, failed=2
- source 分布：given=16, knowledge=225, search=37
- edge 分布：cartesian=158, quotient=113, stochastic=7
- rework_events=4：N18/N26/N27/N28（均 angle 模式，缺来源支持）· contradiction_events=5
- 末轮 decompose：n_new=179, gain=0.898, S_α'=233.59, frontier=71, verified=155, low_gain_streak=0, dropped_redundant=0
- L1 骨架（5）：N1 工作负载特征建模 / N2 LRU 稳态命中率推导 / N3 LFU 策略增益分析 / N4 对象失效影响评估 / N5 知识来源与置信度标注
- ckpt 序列：r0=62 → r3=244 → r4=278（r1/r2=17 节点为另一次早期尝试，L1=4）；r5..r28 全部 278 节点、state=verify = verify-only resume 批次（每批 3 节点落一次 ckpt），不是 decompose 轮

## §2 关键词命中节点清单
命中汇总（claim+corrected_claim）：stale=38 · 失效=47 · 更新率=31 · 衰减=13 · 累积=20 · 时间窗=3 · 「100 天」=1

**与 Lead 背景观察「树里只有 2 处 stale 提及」调和**：38 处 = 全部 stale 提及；Lead 的「2 处」= **LFU×stale 交叉节点仅 2 个（N172/N230）**。二者均 verified 但都**不含要点 3 的频率表/累积计数老化机制**——N172 是命中率↔T_res 稳态耦合（H↑→T_res 缩短），N230 是高更新率下 LFU 对「频繁更新但低频访问」对象的过滤增益（G_dynamic=λ 项）。即：stale 机制覆盖充分（反 a 证据），但 LFU×stale 交叉节点 0 个触及「频率表随时间老化」这一要点 3 核心机制（要点 3 盲区证据，强化 b 判定）。

| 节点 | 层 | 状态 | 命中 | 内容（摘） |
|---|---|---|---|---|
| N15 | L2 | verified | stale/失效 | ΔM = P(stale) × H(stale\|stale) miss overhead 公式 |
| N17 | L2 | verified | stale/衰减/更新率 | P(stale)=1-exp(-λ·T_res)，λ=0.01/day，泊松假设 |
| N18 | L2 | degraded | stale/失效 | 失效对象热度占比 H(stale\|stale) 近似（rework 过） |
| N262 | L4 | verified | stale | P(stale)∈[0.995%, 9.5%]（T_res∈[1,10] 天），典型 3-6.9% |
| N247 | L4 | verified | 衰减/100 天/更新率 | **u=1%/天 → 每个对象平均每 100 天被替换**；H_eff=H_LRU·(1-min(1,u·T_avg/T_refresh))；高频对象(T_avg<1 天)影响可忽略，中低频(T_avg>10 天)折扣 90%+ |
| N230 | L4 | verified | 更新率 | 高更新率下 LFU 优势放大（λ=0.05/day）：对「频繁更新但低频访问」对象的过滤能力——最接近 gold 3 但方向相反（讲 LFU 的优势，不是 LFU 的老化） |
| N255 | L4 | degraded | 失效 | LFU 频率锁定失效惩罚 P_inval_LFU（冷大文件占队列尾部，非频率计数器老化） |
| N139/N156/N215 | L4 | verified | 时间窗 | 均为 LRU 时间局部性/时间窗口语境，与 LFU 频率窗口无关 |

**LFU 频率表老化机制专项关键词扫描 = 0 命中**：频率表/频率统计/频率计数/频率老化/频率衰减/频率重置/频率窗/老化/陈旧热点/frequency aging/aging counter 全部缺席。树内 54 个 LFU 节点全部关于 LFU 静态优势（上限公式/阈值 θ/ρ 修正/工作点数值），无一提及「累积频率计数不衰减 → 陈旧热点 → 时间窗口重置/频率衰减」。
## §3 gold 6 点逐点对照
gold 源：s8b_pilot.py GOLD["nat"]（judge 用 6 要点）。

| # | gold 要点（摘） | 树内有节点？ | 判定 |
|---|---|---|---|
| 1 | Pareto 热度下 LRU 命中率可用累积质量估算（头部 k% 承载大部分请求） | ✅ N12（H_LRU≈1-(1/p)^(β-1)）/N168（Top 10%≈75.4%）等多个 | 过（judge 已给分） |
| 2 | α=1.1 接近临界 → 容量利用率对头部集中度敏感 | ✅ N6/N9（截断均值、p 比例）/N236-N238 工作点 | 过 |
| 3 | LFU 优势上限受更新/热度漂移限制：**1%/天更新 → LFU 频率表老化**，提升有限且需量化 | ❌ **0 节点**。54 个 LFU 节点全是静态优势；N230 方向相反（高更新率放大 LFU 优势）；N255 是冷大文件占队列尾，非计数器老化 | **树里根本没有 = 分解缺失（b）** |
| 4 | 大小-热度负相关 → 字节命中率 ≠ 请求命中率，口径分开 | ✅ N8（Copula）/N18/N263-N265（H(stale\|stale) 修正）/N204 | 过 |
| 5 | 更新率 1%/天 → 陈旧折扣 ≈ 1-exp(-T_res/100)，**100 天=1/λ 平均更新间隔**，幅度给推导 | ⚠️ **有节点但 P4 没用**：N17（1-exp(-λT_res) 公式）/N262（数值范围 3-6.9%）/**N247（verified，明确写了「u=1%/天 → 每 100 天替换一次」**）都在树里且 verified；但 P4 综合选了别的口径，judge 判 0 | **有节点、P4 没用 = 综合丢失（非 a 非 b，是 P4 问题）** |
| 6 | 明确标注哪些是估算/假设 | ✅ N5/N20/N21/N22 整支 | 过 |

要点 5 细节（一手核验 runs-s5-sm-nat-synth.json 的 P4 answer，5088 字）：N247 文本同时含「100 天」「1/λ 量级」「推导」三要素且 status=verified——树信息量足够。但 P4 answer 全文对 (c) 用的是 **T_res≈1.5 天** 口径（「典型对象平均驻留时间 1.5-4.0 天，取 T_res≈1.5 days」），得出折损 0.985-0.987，引用的节点是 [N182, N193, N260] 与 [N74, N192]；**N247 未被引用**（P4 answer 共引用 15 个节点 id：N2/N3/N13/N17/N26/N28/N74/N111/N112/N182/N192/N193/N256/N257/N260，无 N247），且 answer 全文「100 天」=0 命中、「1/λ」=0 命中。→ 失分点确凿在 P4 综合没把 N247 的 100 天口径选进答案（与 Lead 探针「P4 选错口径」一致，现为一手证据）。

## §4 停止原因判定
**结论：撞到 max_depth=4 硬顶停的（结构性 break），J_necessary 软判断与 rounds 耗尽均被证据否定。**

元字段证据链：
1. `final_state="verify"` 而非 `"stop"`：STOP 只在两处赋值（s5_state_machine.py:1547 J_stop 连续低增益 / :1552 无新节点饱和），都会打 `state=State.STOP` 后落盘；本树落盘 state=verify。
2. `rounds`（decompose 日志）只有 1 条：n_new=179、gain=0.898、low_gain_streak=0、dropped_redundant=0 —— 末轮增益极高、streak=0，**J_necessary 判据（pass_rate<0.3 才累加 streak，:1478）根本没触发**，不存在「J_necessary 判不需要再拆」。
3. ckpt 序列：r4 已达 278 节点且 lv_max=L4；r5..r28 节点数恒 278、state=verify —— 是 verify-only resume 的落盘批次（:1225-1233 每 3 节点一批），decompose 早已结束。
4. 代码逻辑：主循环顶部 `if lv_max >= self.cfg.max_depth: break`（:1250-1252，cfg.max_depth 默认 4，:119；CLI 只有 --max-nodes/--beta 覆盖入口，无 max_depth 覆盖）。r4 时 lv_max=4 → 下一轮循环顶部直接 break。max_nodes 默认 150 但 278>150 说明跑时带了 --max-nodes≥278 覆盖（同题族 /tmp/ablation-sm-matched/nat_formula_r06..r10 日志有 max_nodes=150 hit 先例，本树 278 节点完整落盘 = 覆盖值 ≥278）——**max_nodes 没撞**（278 < 覆盖值），撞的是 max_depth。
6. 关键结构性事实：frontier 只取最深层节点（:1254-1255 `level == lv_max`）。树到 L4 后，所有 L3 父节点（含 N3 LFU 支的 N13/N14/N48 等）永久离开 frontier——**即使 J_necessary 一直判「需要再拆」，机制维度也再没机会展开**。这不是停止判据软，是 frontier 选择把浅层父节点锁死了。
7. 旁证：/tmp/ablation-sm-matched/nat_formula_r09.sm.log 同题另一 rep 直接打出 `[SM] max_depth=4 hit`（138 节点即停），r06/r07/r08/r10 打出 `max_nodes=150 hit`——max_depth/max_nodes 硬顶在本题族是常态停止路径。

## §5 DECOMPOSE prompt 检查
两个 prompt（s5_pipeline.py）：L1 骨架 `P1_L1_SKELETON`（:63-85）+ 逐层 `P1H_INDEX`（:936-977）。

**有没有「枚举答案需要哪些维度/计算」的指令？有，但只在 L1 层，且产物不进后续 prompt。**

L1 prompt 原文（:65-72）：
> 「【第一步：估计并形式化终点目标函数】先不要拆维度……写出回答它所需的『终点目标函数』——即最终答案的好坏由哪些要素决定、各要素如何组合」
> 「【第二步：从目标函数导出顶层正交维度】把目标函数的每个要素展开成回答所需的顶层目录维度。维度数量 3-7 个封顶。」

另有规则 5（:82）：「题目显式列出的每个子问必须被某个顶层维度覆盖。」

逐层 prompt `P1H_INDEX` 也有泛化覆盖判据（:943）：「答案要覆盖的时间尺度和对比口径，树上必须有对应节点承载」，规则 4（:950）子问全覆盖，【何时停】（:962-964）逐父节点判「再往下拆一层还能产生新的具体数值/公式/可检索事实吗？」——但**输入只有【已确认事实】+【本轮要分解的父节点】（:975-976），没有全树、没有维度清单**，是纯局部视图。

**为什么 LFU 老化维度没长出来（b 的直接证据链）：**
1. 模型自己在 L1 就识别了机制维度：ckpt 存的 objective 原文（sm-nat-r28.json，verbatim）——composition=`Fidelity × Accuracy × Mechanism × Sourcing`，factors[2]=「机制解释力：是否清晰阐述了 LRU/LFU/失效对命中率影响的具体物理或算法机制（如缓存污染、**频率分布偏差**）」，rationale=「若机制不清则无法解释为何 LFU 优于 LRU……四者缺一不可」——模型知道要什么。
2. 但 objective 被记录后丢弃：全量 grep `objective`（s5_state_machine.py 共 18 处）证实 `self.objective` 只出现在声明(:421/:461)、L1 解析落盘(:512-520)、checkpoint 写入(:1009/:1817)、resume 恢复(:1742)、终盘落盘(:1843)——**从未进入任何 prompt 构造**（:510-511 注释「不进后续 prompt」得到代码级实证）。后续 28 轮 decompose 的 prompt 里机制要素从未出现过。
3. N3（LFU 支）在其 L2 父节点（N13/N14）处于 frontier 的窗口期（r2→r3，244→278 增长段）确实展开了 L3/L4：N48（θ 方程）/N88（稳态命中率）/N89（ρ 修正）/N110/N122/N146-N147/N158/N203-N204/N214/N241/N246/N252/N255/N257——**全部是静态上限公式机器**，无一是「频率计数器不衰减→陈旧热点→窗口重置/衰减」机制。即：分支可展开的时候，维度没被触发（局部 prompt 把模型带向公式细化，而非机制枚举）。
4. 逐层 prompt 无全维度清单输入 → 模型看不到「答案还需要 LFU 老化机制这个维度」，只能围绕父节点 claim 往下钻。

## §6 a/b 判定结论
**判定：b（维度盲区）主导；a（停止太早）被证据否定；要点 5 失分归 P4 综合丢失（a/b 之外的第三类）。**

证据链（按要点）：
- **要点 3（LFU 频率表老化）= b**。① 树内老化机制专项关键词 0 命中（频率表/频率计数/频率老化/aging counter 等全缺席），54 个 LFU 节点全为静态优势；② LFU×stale 交叉节点仅 2 个（N172/N230），均 verified 但都不触及「频率表随时间老化」机制（N172=命中率↔T_res 耦合、N230=高更新率过滤增益）；③ 模型 L1 自估 objective 已点名机制要素但被管线丢弃（:510-511「不进后续 prompt」）；④ N3 支在可展开窗口期内只长出静态公式机器，维度未触发；⑤ 逐层 prompt 局部视图、无维度清单。
- **停止原因不能归因 a**：撞的是 max_depth=4 硬顶（:1250-1252），不是 J_necessary 软判（末轮 gain=0.898、streak=0、dropped_redundant=0）也不是 rounds 耗尽。且即便不撞硬顶也救不了要点 3：frontier 只取最深层（:1254-1255），L4 之后只会深化既有分支的数值工作点，机制维度（应挂 N3/N13 的兄弟位）从未成为候选节点——硬顶砍掉的是「既有分支的深度」，不是「缺失维度的广度」。
- **要点 5（100 天=1/λ 量级）= P4 综合丢失**。N247（L4, verified）原文含「u=1%/天 → 每个对象平均每 100 天被替换一次新内容」+ 推导公式，N17/N262 提供 1-exp(-λT_res) 与数值范围——树信息量足够。一手核验 P4 answer（runs-s5-sm-nat-synth.json）：(c) 用 T_res≈1.5 天口径、引用 [N182,N193,N260]/[N74,N192]，**N247 未引用、全文「100 天」=0 命中** → P4 没选这个口径。
- **占比**：gold 失分 2 点中，1 点纯 b（要点 3），1 点 P4 丢失（要点 5）；a 贡献 ≈ 0。修复优先级：① 把 L1 objective factors 注入逐层 prompt（一行改动，直接补维度盲区）② frontier 允许浅层父节点按「未覆盖维度」重入（结构性）③ P4 综合对 verified 节点做口径召回（修要点 5 类失分）。
