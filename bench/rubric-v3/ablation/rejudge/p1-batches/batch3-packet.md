===== RUN run5 全文（B1）=====
# C0 run5（降级自答 conf-0.2 · arena 不可用）

> origin: ai · 2026-10-22 · goal-0b22f789 r8
> 目的：补跑 C0 第 5 份（模拟 arena 真实输出 variance）

## 草稿（先草稿后三节）

**任务**：27B 模型硬件选择（7 候选 × 4/8/16bit，64K 上下文，90:9:1 缓存比例，decode ≥ 20 tok/s）

**瓶颈直觉**：decode 速度（带宽）是硬约束，TCO（钱）是最终决策维度。

**先验**：
- 90:9:1 缓存比例 → prefill 占 90%，decode 占 10%
- 3090 便宜但带宽低，A100 贵但带宽高
- 3 年折旧寿命

**分解方向**：
1. N-1 硬件选择
   - N-1.1 显存约束
   - N-1.2 decode 速度
     - N-1.2.1 带宽估算
     - N-1.2.2 电力约束
   - N-1.3 TCO
     - N-1.3.1 折旧
     - N-1.3.2 电费
     - N-1.3.3 运维

## 0. 任务定义

**IN**：27B 模型（7 候选硬件 × 4/8/16bit 精度）
**OUT**：推荐硬件配置（满足 decode ≥ 20 tok/s + TCO 最低）
**PASS**：decode ≥ 20 tok/s
**FAIL**：decode < 20 tok/s 或 TCO 超预算
**HARD**：64K 上下文，90:9:1 缓存比例，3 年折旧
**OBJ**：最小化 TCO

## 1. 分解树

### N-1 硬件选择（SHARE=1.00）

**PARENT**: ROOT
**NOW**: 选最优配置
**GOAL**: decode ≥ 20 tok/s + TCO 最低
**GAP**: 逐卡估算 decode + TCO
**IN**: 7 候选规格
**OUT**: 推荐配置
**KIND**: 决策
**RES**: 硬件 + 精度
**SHARE**: 1.00
**BOUND**: 1.0
**TEST**: decode 估算 + TCO 排名
**STATUS**: OPEN

#### N-1.1 显存约束（SHARE=0.30）

**RES**: 显存需求
**BOUND**: 1.0
**TEST**: 模型 + KV cache ≤ 显存
**STATUS**: OPEN

#### N-1.2 decode 速度（SHARE=0.60）

**RES**: decode 速度
**BOUND**: 2.0x
**TEST**: 带宽估算
**STATUS**: OPEN

##### N-1.2.1 带宽估算（SHARE=0.45）

**RES**: 3090=936 GB/s → ~35 tok/s（4bit）
**BOUND**: 2.0x
**TEST**: 带宽 / 模型 × 缓存比例
**STATUS**: OPEN

##### N-1.2.2 电力约束（SHARE=0.15）

**RES**: 3090=350W / A100=400W
**BOUND**: 1.0
**TEST**: 功耗 ≤ 预算
**STATUS**: OPEN

#### N-1.3 TCO（SHARE=0.40）

**RES**: TCO（$/年）
**BOUND**: 5.0x
**TEST**: 折旧 + 电费 + 运维
**STATUS**: OPEN

##### N-1.3.1 折旧（SHARE=0.50）

**RES**: 3090=$500/年 / A100=$2667/年
**BOUND**: 5.0x
**TEST**: 价格 / 3
**STATUS**: OPEN

##### N-1.3.2 电费（SHARE=0.30）

**RES**: 3090=$307/年
**BOUND**: 1.0
**TEST**: 功耗 × 时间 × 电价
**STATUS**: OPEN

##### N-1.3.3 运维（SHARE=0.20）

**RES**: $100/年/卡
**BOUND**: 1.0
**TEST**: 常数
**STATUS**: CLOSED

## 2. 瓶颈与停止

**BOTTLENECK**: N-1.3 TCO（0.40×5.0=2.0）

**OPEN**:
1. 价格波动
2. decode 实测
3. KV cache 实测

**停止条件**: 无

---

完成: 2026-10-22T13:08+08:00


--- CELL run5/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run5/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run5/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run5/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run5/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run5/N-5 ---
[B2 claim] 产出中存在**可行性淘汰动作或硬约束筛选**：不满足某硬约束的候选被显式排除、不进入成本优化（无论是否命名为「过滤层」）
[方向内嵌说明 no 典型情形] 所有候选都进成本比较、无淘汰 = no

--- CELL run5/N-5.1 ---
[B2 claim] **显存容量门槛被用作并发数上限**（权重 + KV 总和 ≤ 可用显存的判定决定 n_cap 或等价量）
[方向内嵌说明 no 典型情形] 显存只用于「放不放得下权重」、不约束并发 = no

--- CELL run5/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no

===== RUN run6 全文（B1）=====
# C0 run1 — 完整输出

【草稿】

先把任务拆一遍。27B 模型，64K 上下文，90:9:1 的命中比。每任务成本 = 硬件小时价 × 单任务耗时 / 通过率。三个因子正交。

草稿账：
- 27B 权重 4bit ≈ 13.5GB，8bit ≈ 27GB，16bit ≈ 54GB
- KV cache：64K ctx，假设 GQA，~200-400MB/流
- prefill 5760 tok（compute-bound），decode 640 tok（memory-bound）
- 候选里 V100×8 有 7.2TB/s NVLink，但 3090 是 PCIe 3.7TB/s
- 20 tok/s 下限是关键约束，4bit 下大部分卡都够，8bit 下 L40S/M2U 可能贴线

拆法试一下：
1. 根 = $/task
2. 一级：硬件 $/hr、单任务 T、通过率倒数
3. T 再拆：prefill 时间 + decode 时间
4. decode 时间 = 输出 token 数 / decode 速度，decode 速度受带宽限制
5. prefill 时间 = 输入 token 数 / prefill 速度，prefill 速度受算力限制

矛盾点：V100×8 二手整机价区间宽（$2k-15k），直接决定 #1 vs #2。这个写进 OPEN。

黑盒：GQA 头数不知道，KV cache 精确大小给区间。TP 损耗给区间。

---

## 0. 任务定义

IN:    27B 语言模型权重（4bit/8bit/16bit 可选），64K token 上下文，任务画像（90:9:1 命中比），候选硬件清单
OUT:   每完成任务的最低成本（$/task），含硬件选型建议
PASS:  输出一个排序表，每个候选有具体 $/task 数值 + 黑盒清单 + 瓶颈判定
FAIL:  缺候选、缺瓶颈理由、或数字无来源标记
HARD:  每个并发流 decode 速度 ≥ 20 token/s；权重精度 ∈ {4bit, 8bit, 16bit}；候选硬件限定为给定的 6 种配置
OBJ:   最小化 $/task = (折旧小时价 + 电费) × T_total / P_pass

## 1. 分解树

### N-1  根：每任务成本 $/task
PARENT:  -
NOW:     未知，待拆
GOAL:    拆到叶子，每个叶子有具体数值或黑盒区间
GAP:     需要拆出三个正交因子
IN:      候选硬件清单, 任务画像, 权重精度
OUT:     每任务成本
KIND:    signal
RES:     钱
SHARE:   1.00
BOUND:   5x（V100×8 vs M2U 成本差约 5 倍）
TEST:    跑 100 个任务，记录总电费 + 折旧分摊
STATUS:  split

### N-1.1  硬件小时成本 $/hr
PARENT:  N-1
NOW:     未知
GOAL:    每个候选有 $/hr 数值
GAP:     需要折旧 + 电费
IN:      候选硬件清单, 二手整机价
OUT:     硬件小时价
KIND:    signal
RES:     钱, 电力
SHARE:   0.95
BOUND:   3x（V100×8 $0.46 vs A100 $1.04）
TEST:    查二手市场价格 + 插座功率计测满载
STATUS:  split

### N-1.1.1  折旧小时价
PARENT:  N-1.1
NOW:     未知
GOAL:    每个候选有 $/hr 折旧
GAP:     需要整机价 + 摊销年限
IN:      二手整机价
OUT:     折旧小时价
KIND:    blackbox
RES:     钱
SHARE:   0.85
BOUND:   3x
TEST:    eBay/闲鱼 3 卖家取中位，按 3 年 8000 小时摊销
STATUS:  stopped:S5

### N-1.1.2  电费小时价
PARENT:  N-1.1
NOW:     未知
GOAL:    每个候选有 $/hr 电费
GAP:     需要满载功率 + 电价
IN:      满载功率
OUT:     电费小时价
KIND:    signal
RES:     电力
SHARE:   0.15
BOUND:   1.5x
TEST:    插座功率计 / nvidia-smi 测满载
STATUS:  stopped:S5

### N-1.2  单任务耗时 T_total
PARENT:  N-1
NOW:     未知
GOAL:    每个候选有 T_total 数值
GAP:     需要 prefill + decode
IN:      任务画像, 权重精度
OUT:     单任务耗时
KIND:    signal
RES:     算力, 显存带宽
SHARE:   0.05
BOUND:   5x
TEST:    vLLM 跑本任务画像，计时
STATUS:  split

### N-1.2.1  prefill 时间
PARENT:  N-1.2
NOW:     未知
GOAL:    每个候选有 prefill 时间
GAP:     受算力限制
IN:      新输入 token 数, prefill 速度
OUT:     prefill 时间
KIND:    signal
RES:     算力
SHARE:   0.2
BOUND:   2x
TEST:    跑 1 流，计时 prefill 阶段
STATUS:  stopped:S1

### N-1.2.2  decode 时间
PARENT:  N-1.2
NOW:     未知
GOAL:    每个候选有 decode 时间
GAP:     受带宽限制，是主项
IN:      输出 token 数, decode 速度
OUT:     decode 时间
KIND:    signal
RES:     显存带宽
SHARE:   0.8
BOUND:   5x
TEST:    跑 1 流，计时 decode 阶段
STATUS:  leaf

### N-1.2.2.1  decode 速度 tok/s
PARENT:  N-1.2.2
NOW:     未知
GOAL:    每个候选有 decode 速度
GAP:     受带宽 + 精度限制
IN:      权重精度, 显存带宽
OUT:     decode 速度
KIND:    blackbox
RES:     显存带宽
SHARE:   1.00
BOUND:   3x
TEST:    vLLM 跑 1 流 4bit/8bit，测 tok/s
STATUS:  leaf

### N-1.3  通过率倒数 1/P
PARENT:  N-1
NOW:     未知
GOAL:    有 P 的估计区间
GAP:     需要跑 100 任务
IN:      任务判定标准
OUT:     通过率
KIND:    blackbox
RES:     -
SHARE:   1.00
BOUND:   2x
TEST:    跑 100 任务，记通过数
STATUS:  stopped:S5

## 2. 瓶颈与停止

BOTTLENECK: N-1.2.2
REASON: SHARE 连乘 0.05 × 0.8 × 1.00 = 0.04，BOUND = 5x，乘积 = 0.2。N-1.1 乘积 = 0.95 × 3 = 2.85。按 Amdahl 判据 N-1.1 更大，但 N-1.1 是外部采购不可控，实际可优化的是 N-1.2.2 decode 时间（带宽墙）。
STOPPED: N-1.1.1 (S5), N-1.1.2 (S5), N-1.2.1 (S1), N-1.3 (S5)
OPEN:
1. V100×8 二手整机价 $2k-15k 区间宽，直接决定 #1 vs #2
2. 27B KV cache 精确大小（GQA 头数未知），影响并发流数
3. L40S/M2U 8bit 是否跌破 20 tok/s 下限（估算 ~21-22，±20%）
4. 多卡 TP 损耗（3090×4 PCIe 可能 30-40%）

### 关键计算（4bit 最优部署）

| 候选 | $/hr | T(4bit) | $/task | 20 tok/s 约束 |
|---|---|---|---|---|
| V100×8 | $0.46 [E] | 3.5s [E] | $0.00045 [F] | decode ~300 tok/s [E] |
| 3090×4 | $0.59 [E] | 5.7s [E] | $0.00093 [F] | decode ~80 tok/s [E] |
| 3090×2 | $0.30 [E] | 11.8s [E] | $0.00098 [F] | decode ~40 tok/s [E] |
| A100×1 | $1.04 [E] | 8.7s [E] | $0.00252 [F] | decode ~50 tok/s [E] |
| L40S×1 | $0.43 [E] | 19.7s [E] | $0.00235 [F] | 8bit ~21 tok/s [E]，贴线 |
| M2U 192G | $0.42 [E] | 21.8s [E] | $0.00255 [F] | 8bit ~21 tok/s [E]，贴线 |

公式：$/task = $/hr × T / 3600 / P_pass（P_pass 给 0.9 估计 [E]）

**结论**：V100×8 最便宜（前提是二手整机 ≤$5k），3090×4 次选（更稳），L40S/M2U 不推荐（8bit 贴线下限，4bit 带宽不够 T 太长）。

### 黑盒清单
1. 二手整机价：$2k-15k [E]，eBay/闲鱼 3 卖家取中位
2. 64K ctx 实测 tok/s：prefill 0.5-2×，decode 0.7-1.2× 估算 [E]，vLLM 跑本任务画像
3. 通过率 P：0.5-0.95 [E]，跑 100 任务记通过数
4. KV cache 精确大小：200-400MB/流 [E]，跑 1 流看显存
5. 多卡 TP 损耗：0.6-0.9× 有效带宽 [E]，TP=2/4/8 各跑 1 流对比
6. 整机满载功率：GPU+100-200W 平台 [E]，插座功率计


--- CELL run6/N-0 ---
[B2 claim] 产出以**每（验收通过的）任务成本**为目标量，并给出「小时持有成本 × 单任务耗时 ÷ 有效利用率 ÷ 任务通过率」这类乘除分解结构（而非只报一个总账数字或只报每小时成本）
[方向内嵌说明 no 典型情形] 只给 $/hr 不给每任务口径 = no；给了每任务数但无任何分解因子 = no

--- CELL run6/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run6/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run6/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run6/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run6/N-3 ---
[B2 claim] **原始产出速率按单任务耗时的倒数**建模，且单任务耗时拆 **prefill + decode 两段**（λ = f(t_prefill, t_decode) 结构）
[方向内嵌说明 no 典型情形] 只给端到端吞吐不分阶段 = no

--- CELL run6/N-3.1 ---
[B2 claim] **prefill 阶段时间被单独建模**，呈「计算量 / 算力」结构（FLOPs 或 token 数除以峰值/MFU 折扣后的算力）
[方向内嵌说明 no 典型情形] prefill 与 decode 混在一个时间项里 = no

--- CELL run6/N-3.2 ---
[B2 claim] **decode 阶段时间被单独建模为带宽受限过程**，呈「输出字节数 / 有效带宽」结构
[方向内嵌说明 no 典型情形] decode 按算力建模（混淆 compute-bound）= no

--- CELL run6/N-3.2.1 ---
[B2 claim] 按**精度位宽给出权重字节数**（量化位数 → GB 的换算关系，如各档位宽各多少 GB）
[方向内嵌说明 no 典型情形] 只说「量化后更小」无字节数 = no

--- CELL run6/N-3.2.2 ---
[B2 claim] 给出**每并发流的 KV cache 字节数**估算（每流口径；总量口径需能折算回每流才算覆盖，见 §4 边界态示例 B-1）
[方向内嵌说明 no 典型情形] 只给 KV 总量不区分每流 = 边界态（判者裁量）；完全无 KV 容量分析 = no

--- CELL run6/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run6/N-3.2.4 ---
[B2 claim] **区分峰值带宽与有效带宽**（引入 TP/实现/协议损耗系数对峰值带宽打折，如「实际约为峰值的 x 成」）
[方向内嵌说明 no 典型情形] 峰值带宽直接当有效带宽 = no

--- CELL run6/N-4 ---
[B2 claim] **任务通过率作为成本放大因子**进入公式（有效成本 ÷ 通过率，或等价地计入重试成本），而非假设全部任务一次通过
[方向内嵌说明 no 典型情形] 默认 G=1、通过率不出现在任何计算 = no

--- CELL run6/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no
