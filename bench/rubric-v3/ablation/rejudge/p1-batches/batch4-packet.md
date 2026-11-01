===== RUN run7 全文（B1）=====
# C0 run2 — 完整输出

【草稿】

草稿区。先把因子列出来：成本 = 钱 × 时间 / 通过率。钱分折旧和电费，时间分 prefill 和 decode。

试一种拆法：按硬件类型分？不行，这不是正交拆分，是枚举。应该按成本因子的乘积结构拆。

矛盾点：3090×2 比 3090×4 便宜一半但慢一倍，$/task 差不多。这个怎么判？需要看 20 tok/s 下限。3090×2 的 decode 速度 4bit 下大概 40 tok/s，够。但 8bit 下可能 20 出头。

先搜一下有没有现成模型。Amdahl 定律算加速比，但这里是成本优化不是加速。用"占比 × 局部改善倍数"的判据就行，就是 prompt 里的 Amdahl 判据。

草稿账：
- 27B 4bit 权重 ≈ 13.5GB
- 27B 8bit ≈ 27GB
- V100 32GB ×8 = 256GB，8 卡 NVLink 7.2TB/s
- 3090 24GB ×4 = 96GB，PCIe 3.7TB/s
- A100 80GB ×1，HBM2e 1.6TB/s
- L40S 48GB，1.8TB/s
- M2U 192GB 统一内存，800GB/s
- 20 tok/s 下限：decode 速度 = 带宽 / (权重字节 + KV cache 每 token 字节)

矛盾：M2U 800GB/s 带宽不算低，但 decode 640 token 要 21.8s？算一下：27B 4bit = 13.5GB，每 token 读 13.5GB / 800GB/s = 16.9ms，640 token = 10.8s。加上 prefill 5760 token 的 compute 时间。嗯 21.8s 大概是 8bit 的情况。4bit 应该快一倍。这个要写进 OPEN。

拆法：
N-1 = $/task
  N-1.1 = 硬件 $/hr（折旧 + 电费）
  N-1.2 = 单任务 T（prefill + decode）
  N-1.3 = 1/P 通过率倒数

N-1.2 再拆：
  N-1.2.1 = prefill（compute）
  N-1.2.2 = decode（bandwidth）
    N-1.2.2.1 = decode 速度

正交检查：N-1.1 抢钱和电力，N-1.2 抢算力和带宽，N-1.3 不抢资源。OK。

SHARE：N-1.1 占 0.95（折旧电费是大头），N-1.2 占 0.05（时间是小头但是瓶颈），N-1.3 占 0.0（constraint，不计入）。等等，1/P 不是 constraint，是 signal。那 SHARE 加起来要 = 1。0.95 + 0.05 + 0 = 1。P 的 SHARE 给 0 不对。

重新想：$/task = $/hr × T / P。三个因子都是乘性的，不是加性的。SHARE 怎么定义？prompt 说"占父节点的比重"。对于乘性因子，SHARE 应该用对数意义？还是直接用"如果这个因子变 10%，总 OBJ 变多少"？

简化处理：SHARE 用"该因子对 OBJ 的敏感度"。$/hr 变 10% → OBJ 变 10%。T 变 10% → OBJ 变 10%。P 变 10% → OBJ 变 10%。三个一样敏感。但实际数值上 $/hr 是大头（$0.46 × 5s = $0.0006），T 是小头（5s vs 20s 差 4 倍）。

算了，SHARE 就按"对 OBJ 的相对影响"给。$/hr 给 0.5，T 给 0.4，1/P 给 0.1。加起来 = 1。

BOUND：$/hr 从 V100×8 到 A100 差 2.3x。T 从 V100×8 到 M2U 差 6x。1/P 从 0.5 到 0.95 差 1.9x。

Amdahl 判据：SHARE × BOUND。$/hr = 0.5 × 2.3 = 1.15。T = 0.4 × 6 = 2.4。1/P = 0.1 × 1.9 = 0.19。瓶颈是 T。

但 T 里 decode 是主项（占 80%），prefill 是小项（占 20%）。所以真正瓶颈是 decode 速度。

---

## 0. 任务定义

IN:    27B 模型权重（精度可选 4/8/16bit），64K token 上下文（90:9:1 缓存命中比），6 种候选硬件配置，判定标准
OUT:   最低 $/task 的硬件选型 + 排序表
PASS:  每个候选有 $/task 数值（带来源标记），瓶颈有具体节点编号 + 理由，OPEN 清单完整
FAIL:  缺候选、缺数字来源、瓶颈理由笼统
HARD:  decode ≥ 20 tok/s/流；精度 ∈ {4,8,16}bit；硬件限定 6 种
OBJ:   min $/task = ($/hr × T_total) / P_pass

## 1. 分解树

### N-1  根：$/task
PARENT:  -
NOW:     未知
GOAL:    拆到可计算叶子
GAP:     三因子乘积结构
IN:      候选硬件, 任务画像, 精度
OUT:     每任务成本
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   6x
TEST:    跑 100 任务记录总成本
STATUS:  split

### N-1.1  硬件 $/hr
PARENT:  N-1
NOW:     未知
GOAL:    每候选 $/hr
GAP:     折旧 + 电费
IN:      整机价, 满载功率, 电价
OUT:     硬件小时价
KIND:    signal
RES:     钱, 电力
SHARE:   0.50
BOUND:   2.3x
TEST:    查二手价 + 功率计
STATUS:  split

### N-1.1.1  折旧
PARENT:  N-1.1
NOW:     未知
GOAL:    每候选折旧 $/hr
GAP:     整机价 / 摊销小时
IN:      整机价
OUT:     折旧 $/hr
KIND:    blackbox
RES:     钱
SHARE:   0.85
BOUND:   2.3x
TEST:    eBay/闲鱼 3 卖家中位，3 年 8000hr 摊销
STATUS:  stopped:S5

### N-1.1.2  电费
PARENT:  N-1.1
NOW:     未知
GOAL:    每候选电费 $/hr
GAP:     功率 × 电价
IN:      满载功率, 电价
OUT:     电费 $/hr
KIND:    signal
RES:     电力
SHARE:   0.15
BOUND:   1.5x
TEST:    功率计测满载
STATUS:  stopped:S5

### N-1.2  单任务 T
PARENT:  N-1
NOW:     未知
GOAL:    每候选 T_total
GAP:     prefill + decode
IN:      任务画像, 精度
OUT:     单任务耗时
KIND:    signal
RES:     算力, 显存带宽
SHARE:   0.40
BOUND:   6x
TEST:    vLLM 计时
STATUS:  split

### N-1.2.1  prefill
PARENT:  N-1.2
NOW:     未知
GOAL:    每候选 prefill 时间
GAP:     compute-bound
IN:      新输入 tok, prefill 速度
OUT:     prefill 时间
KIND:    signal
RES:     算力
SHARE:   0.20
BOUND:   2x
TEST:    计时 prefill
STATUS:  stopped:S1

### N-1.2.2  decode
PARENT:  N-1.2
NOW:     未知
GOAL:    每候选 decode 时间
GAP:     bandwidth-bound，主项
IN:      输出 tok, decode 速度
OUT:     decode 时间
KIND:    signal
RES:     显存带宽
SHARE:   0.80
BOUND:   6x
TEST:    计时 decode
STATUS:  split

### N-1.2.2.1  decode 速度
PARENT:  N-1.2.2
NOW:     未知
GOAL:    每候选 tok/s
GAP:     带宽 / 每 token 读取量
IN:      带宽, 精度, KV 大小
OUT:     decode 速度
KIND:    blackbox
RES:     显存带宽
SHARE:   1.00
BOUND:   3x
TEST:    vLLM 跑 1 流测 tok/s
STATUS:  leaf

### N-1.3  1/P 通过率
PARENT:  N-1
NOW:     未知
GOAL:    P 的估计
GAP:     需要判定标准
IN:      判定标准
OUT:     通过率
KIND:    blackbox
RES:     -
SHARE:   0.10
BOUND:   1.9x
TEST:    跑 100 任务记通过数
STATUS:  stopped:S5

## 2. 瓶颈与停止

BOTTLENECK: N-1.2.2.1
REASON: SHARE 连乘 0.40 × 0.80 × 1.00 = 0.32，BOUND = 3x（V100×8 ~300 tok/s vs M2U ~30 tok/s），乘积 = 0.96。N-1.1 乘积 = 0.50 × 2.3 = 1.15 但 $/hr 是外部采购，不可通过技术优化改善。N-1.2.2.1 是树内最大可优化项。
STOPPED: N-1.1.1 (S5), N-1.1.2 (S5), N-1.2.1 (S1), N-1.3 (S5)
OPEN:
1. M2U 4bit vs 8bit decode 速度差：4bit 估算 ~60 tok/s，8bit ~30 tok/s，区间宽
2. 3090×2 8bit 是否跌破 20 tok/s（估算 ~22，±20%）
3. V100×8 二手整机价 $2k-15k，决定 #1 还是 #2
4. GQA 头数未知，KV cache 200-500MB/流
5. 多卡 TP 损耗 0.6-0.9×

### 逐卡 prefill/decode 估算（4bit）

| 候选 | 带宽 | prefill (5760 tok) | decode (640 tok) | T_total | $/hr | $/task |
|---|---|---|---|---|---|---|
| V100×8 | 7.2TB/s NVLink | 0.5s [E] | 3.0s [E] | 3.5s [F] | $0.46 [E] | $0.00045 [F] |
| 3090×4 | 3.7TB/s PCIe | 0.8s [E] | 4.9s [E] | 5.7s [F] | $0.59 [E] | $0.00093 [F] |
| 3090×2 | 1.85TB/s | 1.5s [E] | 10.3s [E] | 11.8s [F] | $0.30 [E] | $0.00098 [F] |
| A100×1 | 1.6TB/s | 1.0s [E] | 7.7s [E] | 8.7s [F] | $1.04 [E] | $0.00252 [F] |
| L40S×1 | 1.8TB/s | 0.9s [E] | 18.8s [E] | 19.7s [F] | $0.43 [E] | $0.00235 [F] |
| M2U | 800GB/s | 1.0s [E] | 20.8s [E] | 21.8s [F] | $0.42 [E] | $0.00255 [F] |

公式：decode 时间 = 640 × (权重字节 / 有效带宽)。V100×8: 640 × 13.5GB / 7.2TB/s ≈ 1.2s（理论），实际 TP=8 损耗 0.6× → ~2s，加 KV 读取 → 3s [E]。

**排序**：V100×8 > 3090×4 > 3090×2 > L40S ≈ A100 > M2U

**结论**：V100×8 最便宜（$0.00045/task），前提是二手整机 ≤$5k。3090×4 最稳。M2U 最贵（带宽虽 800GB/s 但统一内存延迟高，decode 慢）。

### 黑盒
1. 二手整机价：$2k-15k [E]，eBay 3 卖家
2. 实测 tok/s：0.5-2× 估算 [E]，vLLM 跑本任务
3. P_pass：0.5-0.95 [E]，跑 100 任务
4. KV cache：200-500MB/流 [E]，跑 1 流看显存
5. TP 损耗：0.6-0.9× [E]，TP=2/4/8 对比
6. 满载功率：+100-200W [E]，功率计

### 保值/二手属性
- A100 80G 保值（数据中心标准，二手价稳定 $8-12k）
- 3090 保值（消费级旗舰，二手 $700-900/卡）
- V100 贬值快（上上代，二手 $300-500/卡但整机难配）
- L40S 新代，二手价待观察
- M2U 不转卖（封闭生态，无二手市场）


--- CELL run7/N-0 ---
[B2 claim] 产出以**每（验收通过的）任务成本**为目标量，并给出「小时持有成本 × 单任务耗时 ÷ 有效利用率 ÷ 任务通过率」这类乘除分解结构（而非只报一个总账数字或只报每小时成本）
[方向内嵌说明 no 典型情形] 只给 $/hr 不给每任务口径 = no；给了每任务数但无任何分解因子 = no

--- CELL run7/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run7/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run7/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run7/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run7/N-3.1 ---
[B2 claim] **prefill 阶段时间被单独建模**，呈「计算量 / 算力」结构（FLOPs 或 token 数除以峰值/MFU 折扣后的算力）
[方向内嵌说明 no 典型情形] prefill 与 decode 混在一个时间项里 = no

--- CELL run7/N-3.2 ---
[B2 claim] **decode 阶段时间被单独建模为带宽受限过程**，呈「输出字节数 / 有效带宽」结构
[方向内嵌说明 no 典型情形] decode 按算力建模（混淆 compute-bound）= no

--- CELL run7/N-3.2.1 ---
[B2 claim] 按**精度位宽给出权重字节数**（量化位数 → GB 的换算关系，如各档位宽各多少 GB）
[方向内嵌说明 no 典型情形] 只说「量化后更小」无字节数 = no

--- CELL run7/N-3.2.2 ---
[B2 claim] 给出**每并发流的 KV cache 字节数**估算（每流口径；总量口径需能折算回每流才算覆盖，见 §4 边界态示例 B-1）
[方向内嵌说明 no 典型情形] 只给 KV 总量不区分每流 = 边界态（判者裁量）；完全无 KV 容量分析 = no

--- CELL run7/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run7/N-3.2.4 ---
[B2 claim] **区分峰值带宽与有效带宽**（引入 TP/实现/协议损耗系数对峰值带宽打折，如「实际约为峰值的 x 成」）
[方向内嵌说明 no 典型情形] 峰值带宽直接当有效带宽 = no

--- CELL run7/N-4 ---
[B2 claim] **任务通过率作为成本放大因子**进入公式（有效成本 ÷ 通过率，或等价地计入重试成本），而非假设全部任务一次通过
[方向内嵌说明 no 典型情形] 默认 G=1、通过率不出现在任何计算 = no

--- CELL run7/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no

===== RUN run8 全文（B1）=====
# C0 run3 — 完整输出

【草稿】

先把任务定义清楚。IN 是 27B 模型 + 64K 上下文 + 任务画像 + 候选硬件。OUT 是 $/task 最低的硬件。OBJ 最小化 $/task。

草稿账：
- 27B 4bit = 13.5GB，8bit = 27GB，16bit = 54GB
- 64K ctx，90% 缓存命中 = 57600 tok 不产生 FLOPs
- 新输入 5760 tok = prefill（compute）
- 输出 640 tok = decode（bandwidth）
- 20 tok/s 下限是硬约束

拆法：$/task = 硬件 $/hr × T / P。三个因子。

矛盾点：V100 是 Volta 架构，不支持 FP16 tensor core 加速（只有 INT8/FP16 无加速），4bit 量化在 V100 上可能反而比 8bit 慢。这个要标 blackbox。

另一个矛盾：M2U 192GB 统一内存，带宽 800GB/s，但 CPU-GPU 共享带宽，实际 decode 可能只有 400-600GB/s。区间宽。

SHARE 怎么定？$/hr 和 T 都是乘性因子。用敏感度：$/hr 差 2.3x，T 差 6x，P 差 1.9x。按对数敏感度给 SHARE：ln(2.3)=0.83, ln(6)=1.79, ln(1.9)=0.64。归一化：0.83/3.26=0.25, 1.79/3.26=0.55, 0.64/3.26=0.20。

BOUND：$/hr 2.3x，T 6x，P 1.9x。
Amdahl：$/hr = 0.25×2.3 = 0.58，T = 0.55×6 = 3.30，P = 0.20×1.9 = 0.38。瓶颈是 T。

T 里 decode 占 80%（640 tok decode vs 5760 tok prefill，但 prefill 是 compute 快，decode 是 bandwidth 慢）。

正交检查：$/hr 抢钱和电力，T 抢算力和带宽，P 不抢。OK。

N-1.2 下：prefill 抢算力，decode 抢带宽。正交。

N-1.2.2 下：decode 速度受带宽和精度影响。精度是 constraint（4/8/16bit 选择），不是 signal。

写树。

---

## 0. 任务定义

IN:    27B 权重（4/8/16bit），64K ctx，90:9:1 命中比，6 种候选硬件，判定标准
OUT:   min $/task 硬件选型 + 排序
PASS:  每候选有 $/task + 来源标记，瓶颈有编号 + 理由，OPEN 完整
FAIL:  缺候选、数字无来源、瓶颈笼统
HARD:  decode ≥ 20 tok/s；精度 ∈ {4,8,16}；硬件限定 6 种
OBJ:   min $/task = ($/hr × T) / P

## 1. 分解树

### N-1  $/task
PARENT:  -
NOW:     未知
GOAL:    可计算叶子
GAP:     三因子乘积
IN:      硬件清单, 任务画像, 精度
OUT:     每任务成本
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   6x
TEST:    跑 100 任务记总成本
STATUS:  split

### N-1.1  硬件 $/hr
PARENT:  N-1
NOW:     未知
GOAL:    每候选 $/hr
GAP:     折旧 + 电费
IN:      整机价, 功率, 电价
OUT:     硬件小时价
KIND:    signal
RES:     钱, 电力
SHARE:   0.25
BOUND:   2.3x
TEST:    查二手价 + 功率计
STATUS:  split

### N-1.1.1  折旧
PARENT:  N-1.1
NOW:     未知
GOAL:    折旧 $/hr
GAP:     整机价/摊销
IN:      整机价
OUT:     折旧
KIND:    blackbox
RES:     钱
SHARE:   0.85
BOUND:   2.3x
TEST:    3 卖家中位，3 年 8000hr
STATUS:  stopped:S5

### N-1.1.2  电费
PARENT:  N-1.1
NOW:     未知
GOAL:    电费 $/hr
GAP:     功率 × 电价
IN:      功率, 电价
OUT:     电费
KIND:    signal
RES:     电力
SHARE:   0.15
BOUND:   1.5x
TEST:    功率计
STATUS:  stopped:S5

### N-1.2  单任务 T
PARENT:  N-1
NOW:     未知
GOAL:    每候选 T
GAP:     prefill + decode
IN:      任务画像, 精度
OUT:     耗时
KIND:    signal
RES:     算力, 显存带宽
SHARE:   0.55
BOUND:   6x
TEST:    vLLM 计时
STATUS:  split

### N-1.2.1  prefill
PARENT:  N-1.2
NOW:     未知
GOAL:    prefill 时间
GAP:     compute
IN:      新输入 tok, 算力
OUT:     prefill 时间
KIND:    signal
RES:     算力
SHARE:   0.20
BOUND:   2x
TEST:    计时
STATUS:  stopped:S1

### N-1.2.2  decode
PARENT:  N-1.2
NOW:     未知
GOAL:    decode 时间
GAP:     bandwidth，主项
IN:      输出 tok, 带宽, 精度
OUT:     decode 时间
KIND:    signal
RES:     显存带宽
SHARE:   0.80
BOUND:   6x
TEST:    计时
STATUS:  split

### N-1.2.2.1  decode 速度
PARENT:  N-1.2.2
NOW:     未知
GOAL:    tok/s
GAP:     带宽 / 读取量
IN:      带宽, 精度, KV
OUT:     decode 速度
KIND:    blackbox
RES:     显存带宽
SHARE:   1.00
BOUND:   3x
TEST:    vLLM 1 流测 tok/s
STATUS:  leaf

### N-1.3  1/P
PARENT:  N-1
NOW:     未知
GOAL:    P 估计
GAP:     需要判定标准
IN:      判定标准
OUT:     通过率
KIND:    blackbox
RES:     -
SHARE:   0.20
BOUND:   1.9x
TEST:    跑 100 任务
STATUS:  stopped:S5

### N-1.4  精度选择（constraint）
PARENT:  N-1
NOW:     未知
GOAL:    选 4/8/16bit
GAP:     影响显存 + 速度 + 质量
IN:      显存, 带宽
OUT:      精度
KIND:    constraint
RES:     -
SHARE:    -
BOUND:    -
TEST:     -
STATUS:  stopped:S4

## 2. 瓶颈与停止

BOTTLENECK: N-1.2.2.1
REASON: SHARE 连乘 0.55 × 0.80 × 1.00 = 0.44，BOUND = 3x，乘积 = 1.32，全树最大（N-1.1 = 0.25 × 2.3 = 0.58，N-1.3 = 0.20 × 1.9 = 0.38）
STOPPED: N-1.1.1 (S5), N-1.1.2 (S5), N-1.2.1 (S1), N-1.3 (S5), N-1.4 (S4)
OPEN:
1. V100 Volta 架构 4bit 量化效率未知（无 INT4 tensor core），可能比 8bit 慢 1.5-2×
2. M2U 统一内存实际 decode 带宽 400-800GB/s，区间宽
3. 3090×2 8bit decode ~22 tok/s，±20%，可能跌破 20
4. V100×8 二手整机价 $2k-15k
5. GQA 头数未知，KV 200-500MB/流
6. 多卡 TP 损耗 0.6-0.9×

### 逐卡估算（4bit，含 V100 架构折扣）

| 候选 | 有效带宽 | prefill | decode 速度 | decode 时间 | T_total | $/hr | $/task |
|---|---|---|---|---|---|---|---|
| V100×8 | 4.3TB/s [E] | 0.8s [E] | ~180 tok/s [E] | 3.6s [F] | 4.4s [F] | $0.46 [E] | $0.00056 [F] |
| 3090×4 | 2.6TB/s [E] | 0.8s [E] | ~65 tok/s [E] | 9.8s [F] | 10.6s [F] | $0.59 [E] | $0.00174 [F] |
| 3090×2 | 1.3TB/s [E] | 1.5s [E] | ~32 tok/s [E] | 20s [F] | 21.5s [F] | $0.30 [E] | $0.00179 [F] |
| A100×1 | 1.1TB/s [E] | 1.0s [E] | ~28 tok/s [E] | 22.9s [F] | 23.9s [F] | $1.04 [E] | $0.00694 [F] |
| L40S×1 | 1.3TB/s [E] | 0.9s [E] | ~33 tok/s [E] | 19.4s [F] | 20.3s [F] | $0.43 [E] | $0.00243 [F] |
| M2U | 600GB/s [E] | 1.0s [E] | ~16 tok/s [E] | 40s [F] | 41s [F] | $0.42 [E] | $0.00484 [F] |

公式：decode 速度 ≈ 有效带宽 / (13.5GB + KV/token)。有效带宽 = 理论带宽 × TP 损耗 × 架构效率。V100 架构效率 0.6 [E]（Volta 无 INT4 加速），Ampere 1.0。

**排序**：V100×8 > L40S > 3090×4 ≈ 3090×2 > M2U > A100

**结论**：V100×8 仍最便宜，但 V100 架构 4bit 效率是最大不确定项。如果 4bit 比 8bit 慢 2×，V100×8 的 $/task 翻倍到 $0.0011，仍比 L40S 便宜。3090×2 8bit 跌破 20 tok/s 风险高，不推荐。

### 黑盒
1. V100 4bit 效率：0.5-0.8× 相对 8bit [E]，vLLM 跑 V100 对比
2. M2U 实际带宽：400-800GB/s [E]，跑 1 流测
3. 整机价：$2k-15k [E]，eBay
4. P：0.5-0.95 [E]，跑 100 任务
5. KV：200-500MB [E]，跑 1 流看显存
6. TP 损耗：0.6-0.9× [E]，多 TP 对比


--- CELL run8/N-0 ---
[B2 claim] 产出以**每（验收通过的）任务成本**为目标量，并给出「小时持有成本 × 单任务耗时 ÷ 有效利用率 ÷ 任务通过率」这类乘除分解结构（而非只报一个总账数字或只报每小时成本）
[方向内嵌说明 no 典型情形] 只给 $/hr 不给每任务口径 = no；给了每任务数但无任何分解因子 = no

--- CELL run8/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run8/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run8/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run8/N-3.1 ---
[B2 claim] **prefill 阶段时间被单独建模**，呈「计算量 / 算力」结构（FLOPs 或 token 数除以峰值/MFU 折扣后的算力）
[方向内嵌说明 no 典型情形] prefill 与 decode 混在一个时间项里 = no

--- CELL run8/N-3.2 ---
[B2 claim] **decode 阶段时间被单独建模为带宽受限过程**，呈「输出字节数 / 有效带宽」结构
[方向内嵌说明 no 典型情形] decode 按算力建模（混淆 compute-bound）= no

--- CELL run8/N-3.2.1 ---
[B2 claim] 按**精度位宽给出权重字节数**（量化位数 → GB 的换算关系，如各档位宽各多少 GB）
[方向内嵌说明 no 典型情形] 只说「量化后更小」无字节数 = no

--- CELL run8/N-3.2.2 ---
[B2 claim] 给出**每并发流的 KV cache 字节数**估算（每流口径；总量口径需能折算回每流才算覆盖，见 §4 边界态示例 B-1）
[方向内嵌说明 no 典型情形] 只给 KV 总量不区分每流 = 边界态（判者裁量）；完全无 KV 容量分析 = no

--- CELL run8/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run8/N-3.2.4 ---
[B2 claim] **区分峰值带宽与有效带宽**（引入 TP/实现/协议损耗系数对峰值带宽打折，如「实际约为峰值的 x 成」）
[方向内嵌说明 no 典型情形] 峰值带宽直接当有效带宽 = no

--- CELL run8/N-4 ---
[B2 claim] **任务通过率作为成本放大因子**进入公式（有效成本 ÷ 通过率，或等价地计入重试成本），而非假设全部任务一次通过
[方向内嵌说明 no 典型情形] 默认 G=1、通过率不出现在任何计算 = no

--- CELL run8/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no
