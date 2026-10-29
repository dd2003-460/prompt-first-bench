【草稿】

先把任务摆正：不是"哪块卡好"，而是"每完成一个（验收过的）任务花多少钱"。钱是 OBJ，硬件是决策变量。所以第一刀切在"成本从哪来"——本地跑模型，钱的来源只有两类：电力（运营）和卡的钱（资本）。卡的钱又分两条：买（一次性）和租（按小时）。这两条都进成本，但结构不同：买是固定投入摊销，租是可变。我先两条都建模，最后用同一口径（每验收任务 ¥）比较。

先列因素，再砍：
- 电力：每任务跑多少秒 × 整机功耗 / 通过率。功耗是 nuisance（只能测/估，不能调）。
- 卡的钱：买=价格×数量；租=时费×数量。价格/时费是 nuisance。
- 能不能跑：27B 权重在 4/8/16bit 下占多少 GB → 卡总容量必须装下 权重+KV cache+激活。这是准入（constraint），不满足直接淘汰，不进 OBJ。
- 快不快：解码 ≥20 tok/s/流（硬约束）。不满足→并发数掉到 0 或需要加卡/加时，影响成本和吞吐。
- 做不对要重做：通过率 p<1 → 有效成本 ÷ p。这是乘在分子上的系数，不是独立支。
- 前缀缓存 90:9:1、64K 上下文：影响单任务耗时（prefill 9K + decode 1K，90% 命中省掉 57.6K 的 prefill）。这是单任务耗时的主要决定因素之一。

草稿账（数量级，后面用 [S]/[E] 标）：
27B 参数量级 [S 参数量即任务给的 27B]。
- 4bit ≈ 27e9×0.5 byte ≈ 13.5 GB [F: 27e9×4/8]。8bit ≈ 27 GB。16bit ≈ 54 GB。
- KV cache（64K 上下文，单流，GQA 假设）：粗估 1.5–6 GB [E]（取决于层数/头数/GQA 比，27B 常见 GQA 让 KV 小）。留 8 GB 余量算。
- 整机容量门槛（4bit 单流）：13.5+8+激活(~4)≈ 26 GB → 需要 >26 GB。8bit 单流 ≈ 27+8+4 ≈ 39 GB。16bit ≈ 54+8+4 ≈ 66 GB。

逐个候选过准入（4bit / 8bit 单流能否装下）：
- 3090×2 = 48 GB：4bit 装得下(26)，8bit 勉强(39<48，KV 余量小)，16bit 不行。
- 3090×4 = 96 GB：8bit 轻松，16bit 勉强(66<96)。
- A100×1 = 80 GB：8bit 轻松，16bit 勉强。
- A100×2 = 160 GB：全精度都行。
- L40S×1 = 48 GB：同 3090×2。
- M2 Ultra 192 GB：全精度都行，但带宽/算力不同（统一内存 ~800 GB/s [E]）。
- V100×8 = 256 GB：容量够，但 V100 单卡带宽 900 GB/s [S 规格书]、FP16 算力低，且 2017 卡——8bit/4bit kernel 支持差（无 INT8 高效路径），prefill 算力是瓶颈。

解码速度直觉：decode 是 memory-bound，吞吐 ∝ 带宽 / 每 token 读量（≈ 权重字节）。
- 4bit 下每 token 读 ≈13.5 GB：
  - 3090×2 带宽 2×936=1872 GB/s [S] → 理论 ~139 tok/s（单流上限，实际并发会摊）。
  - A100×1 2039 GB/s → ~150。
  - L40S 864 GB/s → ~63。
  - M2 Ultra ~800 GB/s → ~58。
  - V100×8 7200 GB/s → 但 4bit 无高效 kernel，实际打 3–5 折。
- 20 tok/s 门槛在 4bit 下所有候选都轻松过（单流），瓶颈在 8/16bit 或高并发。
  - 8bit 每 token 读 ≈27 GB：L40S 864/27≈32 tok/s（单流，贴近 20，高并发会破线）。M2 800/27≈29。3090 单卡 936/27≈34。
  - 16bit 每 token 读 ≈54 GB：多数卡单流就贴线或破线，需要多卡带宽聚合。

所以精度选择本身就是决策：4bit 最省显存、decode 最快、最省钱，但任务通过率 p 可能因精度下降而掉（质量-成本耦合！）。这是关键 coupling：精度同时进"能否装下/够快"(准入)和"通过率 p"(成本分子)。我得把它当 blackbox 测：同一任务集在 4/8/16bit 各跑一遍，数通过率 p4/p8/p16。

成本口径（每验收任务）：
C = (E_per_task + Cap_per_task) / p
- E_per_task = 单任务耗时 T × 整机功率 P / p（重做也耗电）。
- Cap_per_task = 摊销的卡钱 / 总验收任务数。买：价格×卡数 / 任务总数（按使用寿命 N 年摊）。租：时费×卡数×T / p。
为公平，统一按"租"口径算每任务成本（本地自建则用买+电，但题目说"本地跑"，我两种都给，主口径用自建=买+电，因为题目强调本地）。
实际"本地跑"= 自己买卡。所以 Cap = 卡总价 / 寿命内任务总数，电 = T×P/寿命任务数×(1/p 已含)。

草稿结论方向：钱最省 ≈ 单任务耗时短 + 功耗低 + 卡便宜 + 通过率高。
- 3090×2：卡便宜(二手 ~¥8k/张 [E 2026 行情])、电低(350W×2 [S])、4bit decode 快 → 很可能最低，前提是 20 tok/s 在目标并发下过线且 p4 可接受。
- 风险：3090 单卡 24GB 跑 8bit 27B 要双卡张量并行，NVLink 没有（3090 无 NVLink，PCIe 互联 [S]）→ 多卡 decode 互联开销；4bit 单卡装不下(13.5+KV 超 24?) 13.5+8=21.5<24 勉强单卡，但激活会爆 → 实际要 2 卡。
- M2 Ultra 192GB：一次性能装 16bit，无多卡互联问题，电低(~300W [S])，但卡贵(整机 ~¥3w+ [E])、decode 带宽 800GB/s 在 8/16bit 贴线。
- A100 贵、V100 老且 4bit 弱、L40S 带宽低且贵。

BOTTLENECK 预判：SHARE×BOUND 最大的一支。电力支 SHARE 小（电便宜），卡钱支 SHARE 大（卡是大头），通过率支 BOUND 大（p 从 0.5→0.9 是 1.8×）。我算：卡钱支占成本 ~60–70% [E]，其 BOUND（换最便宜可行卡 vs 最贵）~3–5×；通过率支占 ~30%，BOUND 1/p 范围 1.0–2×。卡钱支连乘更大 → 瓶颈在"选哪张卡/几张"(N 卡钱支)。但这要先算出来，不能靠直觉，所以树里把每支的 SHARE/BOUND 都算到可判。

STOP 预判：
- 电力支：S5？电成本占比小，但测功耗很便宜（功率计 ¥0 / 10min），给三个数：成本≈0.02 人时，收益=OBJ 改善 ~5%（电占成本 ~5% [E]），比=0.02/0.05 → 不满足 S5（收益>成本），所以要测，不停。或若占比<1% 才 S5。
- 16bit 支：若 4/8bit 已满足 20tok/s 且 p 够，16bit 对 OBJ 影响小 → 可能 S1（连乘×BOUND<1.05）。
- V100 4bit kernel 支：blackbox，测 kernel 实际速度。
- 通过率 p 支：blackbox，必须测（给任务集跑三档精度）。

矛盾预判（OPEN 候选）：3090 双卡无 NVLink 的 decode 实际速度 vs 理论带宽折算——若实测破 20 tok/s 线，与"4bit 快"矛盾 → 复测（测真实 tok/s），换来源（实测），找机制（PCIe 同步开销）。

现成系统模型对照（规则 6）：LLM 推理成本分解有现成框架——"memory-bound decode + compute-bound prefill" 二分 + Amdahl 式瓶颈判定 + 单位成本 = (capex+opex)/throughput。vLLM/SGLang 的 serving 成本模型、Epoch AI 的 inference cost 模型都把这个拆成：容量准入 → decode 带宽 → prefill 算力 → 利用率 → 电力。我的树用这个对照：N-1 成本(买+电) / N-2 准入(容量) / N-3 速度(decode+prefill) / N-4 质量(通过率)。检查：我的树覆盖了 容量/带宽/算力/电力/质量 五块，与现成模型一致，无遗漏。OK。

草稿写完。下面输出三节。

## 0. 任务定义

IN:    候选硬件集 {3090×2, 3090×4, A100×1, A100×2, L40S×1, M2U-192GB, V100×8}；权重精度 ∈ {4,8,16}bit；任务画像（前缀命中:新输入:输出 = 90:9:1，单上下文 64K token [F: 0.9×64K=57.6K 命中, 0.09×64K=5.76K 新输入≈取 9K 含命中外, 0.01×64K=640 输出≈取 1K]，任务给的比例按 64K 总长折算）；判定通过率 p∈(0,1)（nuisance，待测）；卡价/时费/电单价（nuisance，待取数）
OUT:   每完成一个验收通过任务的最低成本，单位 ¥/任务（含电力 + 资本摊销）
PASS:  选出硬件+精度组合后：(a) 该组合在 20 tok/s/流 下可支撑的并发流数 ≥1（可观察：实测 tok/s ≥20）；(b) 该组合每验收任务成本数值可被独立复算（给出公式与代入值）；(c) 与次优组合的差距 > 0 且方向可解释
FAIL:  无任何候选同时满足"容量装得下 + 20 tok/s 过线"；或成本排序在 4/8bit 间翻转且无法用通过率解释
HARD:  H1: 每并发流解码 ≥ 20 token/s（可判：实测 tok/s ≥ 20 为真）
       H2: 总显存 ≥ 权重(精度对应 GB) + KV cache(64K 单流) + 激活余量（可判：容量求和 ≤ 总显存为真）
       H3: 本地部署（买卡+自供电，不自用云 GPU 时费）（可判：成本公式含资本摊销且不含云时费为真）
       H4: 重做机制存在：不通过任务按通过率 p 重做，成本 = 单次成本 / p（可判：分子含 1/p 项为真）
OBJ:   最小化 C = 每验收任务总成本（¥/任务）= [电力成本 + 资本摊销成本] / p

## 1. 分解树

### N-1  每验收任务成本
PARENT:  -
NOW:     未算（待各子支代入），单位 ¥/任务
GOAL:    算出每个候选组合的 C 值并排序，单位 ¥/任务
GAP:     缺电力支、资本支、通过率 p 三个数的实测/取值
IN:      N-2.OUT, N-3.OUT, N-4.OUT, N-5.OUT
OUT:     C_per_accepted_task
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   3.0x [E: 最省可行组合 vs 最贵可行组合的成本比，区间 2.5–4.0x]
TEST:    -
STATUS:  split

### N-1.1  电力成本支
PARENT:  N-1
NOW:     未算，¥/任务
GOAL:    每验收任务耗电成本，¥/任务
GAP:     缺整机实测功率与单任务耗时
IN:      N-3.1.OUT, N-5.OUT
OUT:     E_cost_per_task
KIND:    signal
RES:     电力, 钱
SHARE:   0.10 [E: 电占本地成本 ~10%，区间 0.05–0.20，因 27B 单机功率 ~300–700W 而卡价占大头]
BOUND:   1.5x [E: 最低功耗候选 vs 最高功耗候选在相同任务量下的电费比，区间 1.2–1.8x]
TEST:    -
STATUS:  split

### N-1.1.1  整机功耗
PARENT:  N-1.1
NOW:     未测，W
GOAL:    每个候选配置满载功率，W
GAP:     缺功率计实测
IN:      候选硬件集
OUT:     P_rack_W
KIND:    nuisance
RES:     电力
SHARE:   1.00
BOUND:   2.2x [E: 3090×2(~700W) vs V100×8(~2000W+) 功率比，区间 1.8–2.5x]
TEST:    -
STATUS:  stopped:S5

### N-1.1.2  单任务耗时
PARENT:  N-1.1
NOW:     未算，s/任务
GOAL:    每个候选 4bit 下单验收任务耗时，s
GAP:     缺 decode 实测 tok/s（见 N-3.1）
IN:      N-3.1.OUT, N-5.OUT
OUT:     T_task_s
KIND:    nuisance
RES:     钱
SHARE:   1.00
BOUND:   3.0x [E: 最快候选 vs 最慢可行候选的单任务耗时比，区间 2–4x]
TEST:    -
STATUS:  split

### N-1.2  资本摊销成本支
PARENT:  N-1
NOW:     未算，¥/任务
GOAL:    每验收任务摊到的卡钱，¥/任务
GAP:     缺各卡 2026 二手/现货价与寿命内总任务数
IN:      候选硬件集, N-4.OUT
OUT:     Cap_cost_per_task
KIND:    signal
RES:     钱
SHARE:   0.90 [E: 卡价占本地成本 ~90%，区间 0.70–0.95]
BOUND:   3.5x [E: 最便宜可行配置总价 vs 最贵可行配置总价比，3090×2 vs A100×2 等，区间 2.5–5x]
TEST:    -
STATUS:  split

### N-1.2.1  卡总价
PARENT:  N-1.2
NOW:     未取数，¥
GOAL:    每个候选配置购卡总价（含数量），¥
GAP:     缺 2026 行情价
IN:      候选硬件集
OUT:     Cap_total_yuan
KIND:    nuisance
RES:     钱
SHARE:   1.00
BOUND:   4.0x [E: 3090×2(~1.6万二手) vs A100×2(~15万+) 总价比，区间 3–6x]
TEST:    -
STATUS:  stopped:S5

### N-1.2.2  寿命内任务总数
PARENT:  N-1.2
NOW:     未定，个
GOAL:    卡寿命内可完成的验收任务总数
GAP:     缺寿命假设与吞吐
IN:      N-3.2.OUT, N-5.OUT
OUT:     N_tasks_life
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   2.0x [E: 寿命 3y vs 5y 及吞吐差异，区间 1.5–3x]
TEST:    -
STATUS:  split

### N-1.3  通过率放大支
PARENT:  N-1
NOW:     p 未知，无量纲
GOAL:    4/8/16bit 各自的任务通过率 p，无量纲
GAP:     缺同一任务集在三档精度下的通过率实测
IN:      N-3.3.OUT
OUT:     pass_rate_p
KIND:    blackbox
RES:     钱, 人的时间
SHARE:   0.00 [constraint-like 乘子，不入 SHARE 加和，见 COUPLE 声明]
BOUND:   2.0x [E: p 区间 0.5–0.9 → 1/p 区间 1.1–2.0x，取 2.0x]
TEST:    取 ≥100 个固定任务，分别在 4bit/8bit/16bit 上各跑一遍（同 prompt 同种子），数通过数/100 得 p4/p8/p16；每档跑 3 次取均值以去随机
STATUS:  split

### N-2  容量准入（constraint）
PARENT:  -
NOW:     未判，bool
GOAL:    每个候选×精度 是否装得下，bool
GAP:     缺 KV cache 与激活的准确 GB
IN:      候选硬件集, 权重精度
OUT:     fit_ok
KIND:    constraint
RES:     显存容量
SHARE:   -
BOUND:   -
TEST:    -
STATUS:  split

### N-2.1  权重占用
PARENT:  N-2
NOW:     4bit=13.5GB [F: 27e9×4/8=13.5e9 B]；8bit=27GB [F: 27e9×8/8]；16bit=54GB [F: 27e9×16/8]
GOAL:    每精度权重 GB
GAP:     无（参数量 27B 任务给定 [S: 任务书]）
IN:      权重精度
OUT:     W_weight_GB
KIND:    signal
RES:     显存容量
SHARE:   0.55 [E: 权重占所需显存 ~55%（4bit 单流 13.5/(13.5+8+4)≈0.55），区间 0.4–0.7]
BOUND:   4.0x [F: 16bit/4bit = 54/13.5 = 4.0x]
TEST:    -
STATUS:  leaf

### N-2.2  KV cache 占用
PARENT:  N-2
NOW:     未精算，GB
GOAL:    64K 单流 KV cache GB
GAP:     缺模型层数/头数/GQA 比
IN:      上下文长64K
OUT:     W_kv_GB
KIND:    blackbox
RES:     显存容量
SHARE:   0.30 [E: KV 占所需显存 ~30%，区间 0.2–0.45，GQA 模型偏下]
BOUND:   2.0x [E: GQA 比 4:1 vs MHA 的 KV 量比，区间 1.5–4x]
TEST:    读目标模型 config.json 的 num_layers/num_kv_heads/head_dim，按 KV = 2×layers×kv_heads×head_dim×bytes×64K 算（公式：每 token KV 字节 = 2·L·H_kv·d·b，乘 64K）
STATUS:  leaf

### N-2.3  激活与框架余量
PARENT:  N-2
NOW:     取 4GB
GOAL:    激活+框架+碎片的固定余量 GB
GAP:     无（经验余量）
IN:      -
OUT:     W_act_GB
KIND:    nuisance
RES:     显存容量
SHARE:   0.15 [E: 余量占 ~15%，区间 0.10–0.25]
BOUND:   1.5x [E: 不同框架(vLLM vs llama.cpp)余量差，区间 1.2–2x]
TEST:    -
STATUS:  leaf

### N-3  速度准入（constraint，H1）
PARENT:  -
NOW:     未判，bool/tok·s⁻¹
GOAL:    每个候选×精度 解码 tok/s 及可支撑并发流数，bool
GAP:     缺各配置实测 decode 速度
IN:      候选硬件集, 权重精度, W_weight_GB
OUT:     speed_ok
KIND:    constraint
RES:     显存带宽, 机间互联, 算力
SHARE:   -
BOUND:   -
TEST:    -
STATUS:  split

### N-3.1  解码带宽支（memory-bound）
PARENT:  N-3
NOW:     未测，tok/s
GOAL:    每个候选×精度 单流 decode tok/s
GAP:     缺实测 tok/s（理论带宽折算只作初筛）
IN:      W_weight_GB, 候选硬件集
OUT:     tok_s_decode
KIND:    blackbox
RES:     显存带宽
SHARE:   1.00
BOUND:   5.0x [E: 最高带宽可行配置 vs 最低带宽可行配置 decode 比，A100/V100 vs M2，区间 3–8x]
TEST:    固定 1 个 64K 前缀 + 9K 新输入任务，单流跑，测输出阶段（前 100 token 后稳定段）的 tok/s，跑 3 次取均值；分别测 4/8bit
STATUS:  split

### N-3.1.1  多卡互联开销
PARENT:  N-3.1
NOW:     未测，倍率
GOAL:    多卡张量并行的 decode 实际/单卡理论 倍率
GAP:     3090 无 NVLink（PCIe 互联 [S: NVIDIA 规格]），V100 有 NVLink，A100 有 NVLink
IN:      候选硬件集
OUT:     link_eff
KIND:    blackbox
RES:     机间互联
SHARE:   0.40 [E: 互联开销占多卡 decode 损失 ~40%（无 NVLink 时），区间 0.2–0.6]
BOUND:   2.0x [E: 有 NVLink vs 无 NVLink 的多卡 decode 效率比，区间 1.5–3x]
TEST:    同一模型 3090×2（PCIe）vs 3090×2+NVLink 桥（若有）vs A100×2（NVLink），各测 decode tok/s，比实测/理论带宽折算值
STATUS:  split

### N-3.2  并发吞吐支
PARENT:  N-3
NOW:     未测，流
GOAL:    在 ≥20 tok/s/流 约束下可跑的最大并发流数
GAP:     缺多流实测（单流 tok/s 高不代表多流每流还 ≥20）
IN:      tok_s_decode
OUT:     max_concurrent
KIND:    blackbox
RES:     显存带宽, 显存容量
SHARE:   0.60 [E: 并发支占速度支 60%（KV 随流数线性涨吃显存+带宽摊薄），区间 0.4–0.8]
BOUND:   3.0x [E: 最大并发可行 vs 最小(=1) 的吞吐比，区间 1.5–5x]
TEST:    逐步加并发流（1,2,4,8…），测每流 tok/s，找到"每流 ≥20 tok/s"的最大流数；记录 KV 显存占用随流数曲线
STATUS:  split

### N-3.3  prefill 算力支
PARENT:  N-3
NOW:     未测，ms
GOAL:    9K 新输入 token 的 prefill 耗时，ms
GAP:     缺 prefill 实测（compute-bound，与 decode 不同瓶颈）
IN:      候选硬件集, 权重精度
OUT:     prefill_ms
KIND:    blackbox
RES:     算力
SHARE:   0.30 [E: prefill 占单任务耗时 ~30%（9K prefill vs 1K decode，90% 命中省了 57.6K），区间 0.1–0.5]
BOUND:   4.0x [E: 高算力(A100) vs 低算力(V100/3090) 的 9K prefill 耗时比，区间 2–6x]
TEST:    固定 9K 新输入，测从喂入到首 token 的 prefill 墙钟，跑 3 次取均值
STATUS:  split

### N-3.4  低精度 kernel 可用性支
PARENT:  N-3
NOW:     未测，可用/降级
GOAL:    4/8bit 量化 kernel 在各候选上是否高效可用
GAP:     V100 无 INT8/4bit 高效 kernel（2017 架构），3090 有 INT8 但 4bit 靠 llama.cpp/GGUF
IN:      候选硬件集, 权重精度
OUT:     kernel_ok
KIND:    blackbox
RES:     算力
SHARE:   0.10 [E: kernel 缺失时性能降级占 ~10%（否则为 0），区间 0–0.3]
BOUND:   3.0x [E: 高效 kernel vs 软件降级 的 decode 比，区间 2–5x]
TEST:    在 V100 与 3090 上分别用 vLLM(AWQ/GPTQ 4bit) 与 llama.cpp(GGUF Q4) 跑同一任务，对比 tok/s，确认无 >2× 异常降级
STATUS:  split

### N-4  质量-精度耦合支（nuisance，供 N-1.3 与 N-2/N-3 共用）
PARENT:  -
NOW:     未测
GOAL:    建立 精度→(通过率 p, 显存, 速度) 的对照表
GAP:     缺三档精度同任务集的对照实测
IN:      权重精度
OUT:     accuracy_table
KIND:    blackbox
RES:     人的时间, 钱
SHARE:   1.00
BOUND:   2.0x [E: p 区间导致的成本放大，同 N-1.3]
TEST:    同一 ≥100 任务集，4/8/16bit 各跑，记录 (p, 显存 GB, decode tok/s, prefill ms) 四元组，成表
STATUS:  split

### N-5  重做机制支
PARENT:  -
NOW:     p 未知
GOAL:    把 1/p 乘进成本分子
GAP:     依赖 N-1.3 的 p
IN:      pass_rate_p
OUT:     retry_factor
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   2.0x [E: 1/p 区间 1.1–2.0x]
TEST:    -
STATUS:  leaf

COUPLE: N-2 × N-4 | 共享资源: 显存容量 | 杀伤实验: 把精度从 8bit 降到 4bit，若耦合成立应同时观察到 (a) N-2 容量从"勉强"变"宽松"、(b) N-4 的 p 下降——若只看到 (a) 而 p 不变，则精度-质量解耦，N-4 可标 S4；若 p 跌 >10% 而容量收益 <1 个候选翻转，则容量支不是真约束，应把 N-2 降为 leaf 并把精度选择权交给 N-4。

## 2. 瓶颈与停止

BOTTLENECK: N-1.2
REASON: SHARE 连乘 = N-1(1.00) × N-1.2(0.90) = 0.90；× BOUND(3.5x) = 3.15，是全树最大。对照次大支 N-1.3：SHARE 作为乘子不占加和（见 COUPLE），其 1/p 的 BOUND=2.0x，等效连乘 1.00×2.0=2.0 < 3.15；N-1.1 电力支 1.00×0.10×1.5=0.15。故按 Amdahl 判据（占比×局部最大改善倍数），资本摊销支 N-1.2（选哪张卡/几张）是瓶颈。[E: SHARE/BOUND 均为估计，区间已标；p 实测后 N-1.3 若 p<0.6 则 1/p>1.67，等效 1.67 仍 < 3.15，排序不翻转]
STOPPED: N-1.1.1 (S5) | N-1.2.1 (S5)
  - N-1.1.1 整机功耗 (S5): (a) 测量成本 ≈ 0.02 人时（功率计夹表 10min，¥0）；(b) 收益 = 电占成本 ~10% [E]，测准可把电支误差从 ±50% 降到 ±5%，对 OBJ 改善 ≈ 10%×45% ≈ 4.5%（换算 ¥/任务，按 C~¥1 量级即 ~0.045¥/任务）；(c) 比 = 0.02人时 / 4.5%OBJ ≈ 0.44（人时/百分点）。三数齐 → 满足 S5 形式，但比 < 1 说明实测更划算——故此处 S5 仅豁免"逐候选精测"，保留 3090×2 与 A100×1 两个代表配置的粗测（功率计一次读满载 W 即可，不逐任务）。
  - N-1.2.1 卡总价 (S5): (a) 测量成本 ≈ 0.1 人时（查 3 个二手平台 2026-10 行情取中位）；(b) 收益 = 卡价是 OBJ 主项（SHARE 0.90），行情波动 ±20% 直接影响排序，测准收益 ≈ OBJ 改善 ~10%；(c) 比 = 0.1人时/10%OBJ = 1.0（人时/百分点）。三数齐 → S5 豁免"逐卡逐精度精算摊销"，保留 3090/A100/M2U 三个代表配置的中位价即可，V100/L40S 仅在容量或速度入围时才取价。
OPEN:
  1. N-3.1.1 多卡互联开销：3090×2 无 NVLink，理论带宽折算 ~139 tok/s（4bit）但 PCIe 同步实际可能打 5–7 折。若实测单流 <20 tok/s（8bit 下尤其），与"4bit 最省"草稿结论矛盾——需复测真实 tok/s + 换来源（实测替代带宽折算）+ 找机制（PCIe 张量并行每层 all-reduce 开销）。当前无法在纸面定论，留 OPEN。
  2. N-1.3 / N-4 通过率 p4：4bit 相对 8/16bit 的通过率跌幅未知。若 p4 < 0.7（1/p4>1.43），则 4bit 的"省钱"被重做吃掉，BOTTLENECK 可能从 N-1.2 翻转到 N-1.3。必须跑 N-4 的 TEST 才能定，当前留 OPEN，不给最终"选 4bit"结论。
  3. N-2.2 KV cache 准确 GB：依赖目标模型 config（层数/GQA 比），任务未给具体模型名，只能用公式 TEST 在拿到 config 后算。若目标模型是 MHA（非 GQA），KV 可达 20GB+，3090×2 的 8bit 单流可能装不下 → 影响 N-2 准入判定，留 OPEN。
