===== RUN run2 全文（B1）=====
# C0 run2（2026-10-22T12:20+08:00）

> origin: ai · 降级自答（arena 不可用，conf-0.2）
> 任务：27B 模型每任务成本最小硬件判断（7 候选 × 4/8/16bit）
> 格式：C0 完整契约（草稿 + 三节）

## 【草稿】

先想清楚关键量：

**任务画像**：
- 上下文 64K token
- 缓存命中 : 新输入 : 输出 = 90:9:1
- 即：cache_hit=57.6K，new_input=5.76K，output=0.64K
- 硬约束：decode ≥ 20 tok/s

**硬件候选**：
- 3090×2（48GB）/ 3090×4（96GB）
- A100×1（80GB）/ A100×2（160GB）
- L40S×1（48GB）
- M2 Ultra（192GB）
- V100×8（256GB）

**权重精度**：4bit / 8bit / 16bit
- 27B 4bit ≈ 14GB（含 overhead ~18GB）
- 27B 8bit ≈ 28GB（~32GB）
- 27B 16bit ≈ 56GB（~64GB）

**关键瓶颈分析**：
- prefill（算力墙）：new_input=5.76K token，一次性算完
- decode（带宽墙）：output=0.64K token，逐 token 生成
- cache_hit=57.6K token：KV cache 读取（带宽）
- 90:9:1 比例 → cache 读取占大头，但一次性读；decode 占 1/100，但逐 token

**候选硬件算力/带宽**（需查，黑盒）：
- 3090：算力 35.6 TFLOPS（FP16）/ 带宽 936 GB/s
- A100：算力 312 TFLOPS（FP16）/ 带宽 1555 GB/s
- L40S：算力 90.5 TFLOPS（FP16）/ 带宽 864 GB/s
- M2 Ultra：算力 ~32 TFLOPS（估）/ 带宽 800 GB/s
- V100：算力 125 TFLOPS（FP16）/ 带宽 900 GB/s

**TCO 估算**（黑盒，需查价格）：
- 3090：~$1500/卡，保值
- A100：~$8000/卡，保值
- L40S：~$8000/卡，新代掉价
- M2 Ultra：~$4000（整机），转卖难
- V100：~$500/卡，旧代掉价

**初步判断**：
- 显存约束：27B 16bit 需 64GB → 3090×2（48GB）不够，3090×4（96GB）够
- 4bit 18GB → 单卡 3090/A100 都够
- decode 20 tok/s 约束：需带宽足够读 KV cache
- 90:9:1 → cache 读取占大头，但 prefill 算力也关键

**候选排名**（初步）：
1. 3090×2 4bit：便宜 + 保值 + 带宽够
2. A100×1 4bit：算力最强 + 保值
3. 3090×4 8bit：带宽够 + 保值
4. V100×8 4bit：便宜但旧代
5. L40S×1 4bit：新代掉价
6. M2 Ultra 4bit：转卖难

## 0. 任务定义

IN:  27B 语言模型权重（4bit/8bit/16bit），任务画像（64K 上下文，90:9:1 比例）
OUT: 每完成一个任务的总成本（美元/任务）
PASS: 候选硬件 decode 速度 ≥ 20 tok/s，且总成本最低
FAIL: 任何候选 decode < 20 tok/s，或总成本计算缺项
HARD: 
  - 显存容量 ≥ 权重 + KV cache（64K token）
  - decode 速度 ≥ 20 tok/s（单并发）
  - 电力 ≤ 5kW（假设）
OBJ: 最小化 总成本 = (硬件折旧/寿命 + 电费/任务 + 运维) / 任务数

## 1. 分解树

### N-1  硬件选择
PARENT: -
NOW: 7 候选 × 3 精度 = 21 组合
GOAL: 选出 1 个组合，总成本最低
GAP: 需估算每组合的 TCO + 验证 decode 速度
IN:  候选列表，精度选项，任务画像
OUT: 最优组合，TCO 排名
KIND: signal
RES: 钱，显存容量，算力，显存带宽
SHARE: 1.00
BOUND: 3.0x（A100 vs 3090 算力差 ~8x，但 TCO 差 ~5x）
TEST: 逐组合估算 TCO，跑基准测试验证 decode 速度
STATUS: split

### N-1.1  显存容量约束
PARENT: N-1
NOW: 27B 4bit=18GB / 8bit=32GB / 16bit=64GB；KV cache 64K≈8GB
GOAL: 过滤掉显存不够的组合
GAP: 需算每组合的总显存需求
IN:  权重精度，KV cache 大小
OUT: 可行组合列表
KIND: constraint
RES: 显存容量
SHARE: -
BOUND: -
TEST: 查每卡显存，算 权重+KV cache ≤ 总显存
STATUS: leaf

### N-1.2  decode 速度约束
PARENT: N-1
NOW: 需 ≥ 20 tok/s
GOAL: 过滤掉 decode < 20 tok/s 的组合
GAP: 需估算每组合的 decode 速度
IN:  候选硬件带宽，KV cache 大小，output token 数
OUT: 可行组合列表
KIND: constraint
RES: 显存带宽
SHARE: -
BOUND: -
TEST: 估算 decode 速度 = 带宽 / (KV cache 大小 + 权重大小)，跑基准
STATUS: split

### N-1.2.1  带宽估算
PARENT: N-1.2
NOW: 3090=936 GB/s / A100=1555 GB/s / L40S=864 GB/s / M2=800 GB/s / V100=900 GB/s [E]
GOAL: 每组合 decode 速度
GAP: 需算 速度 = 有效带宽 / 每 token 读取量
IN:  硬件带宽，KV cache 大小，权重大小
OUT: decode 速度（tok/s）
KIND: signal
RES: 显存带宽
SHARE: 0.60
BOUND: 2.0x（A100 vs 3090 带宽差 ~1.7x）
TEST: 公式估算 + 跑 llama.cpp 基准
STATUS: leaf

### N-1.2.2  电力约束
PARENT: N-1.2
NOW: 3090=350W / A100=400W / L40S=350W / M2=200W / V100=250W [S]
GOAL: 总电力 ≤ 5kW
GAP: 需算每组合的总功耗
IN:  硬件功耗，卡数
OUT: 可行组合列表
KIND: constraint
RES: 电力
SHARE: -
BOUND: -
TEST: 算 功耗×卡数 ≤ 5kW
STATUS: leaf

### N-1.3  TCO 估算
PARENT: N-1
NOW: 需估算每组合的总成本
GOAL: 每组合 TCO 排名
GAP: 需算 折旧+电费+运维
IN:  硬件价格，电力价格，寿命，任务数
OUT: TCO（美元/任务）
KIND: signal
RES: 钱
SHARE: 0.40
BOUND: 5.0x（A100 vs 3090 价格差 ~5x）
TEST: 查价格，算 折旧=(价格/寿命)+电费=(功耗×任务数×电价)+运维
STATUS: split

### N-1.3.1  硬件折旧
PARENT: N-1.3
NOW: 3090=$1500 / A100=$8000 / L40S=$8000 / M2=$4000 / V100=$500 [E]
GOAL: 每组合折旧成本
GAP: 需定寿命（假设 3 年）
IN:  硬件价格，寿命
OUT: 折旧成本（美元/年）
KIND: signal
RES: 钱
SHARE: 0.50
BOUND: 5.0x
TEST: 公式 折旧=价格/寿命，查当前价格
STATUS: leaf

### N-1.3.2  电费
PARENT: N-1.3
NOW: 电价 $0.1/kWh [E]
GOAL: 每任务电费
GAP: 需算 功耗×任务时长
IN:  硬件功耗，任务时长，电价
OUT: 电费（美元/任务）
KIND: signal
RES: 钱，电力
SHARE: 0.30
BOUND: 2.0x
TEST: 公式 电费=功耗×任务时长×电价
STATUS: leaf

### N-1.3.3  运维成本
PARENT: N-1.3
NOW: 假设 $100/年/卡 [E]
GOAL: 每组合运维成本
GAP: 需估算
IN:  卡数，运维单价
OUT: 运维成本（美元/年）
KIND: blackbox
RES: 钱
SHARE: 0.20
BOUND: ?
TEST: 查行业基准，或实测 1 个月
STATUS: leaf

## 2. 瓶颈与停止

BOTTLENECK: N-1.3（TCO 估算）
REASON: SHARE=0.40 × BOUND=5.0 = 2.0，全树最大（Amdahl 判据）
STOPPED: 
  - N-1.1 (S3)：显存容量约束，归硬件厂商管
  - N-1.2.2 (S3)：电力约束，归数据中心管
OPEN:
  - 硬件价格波动（需实时查）
  - 任务通过率（<100%，重做成本未计入）
  - KV cache 大小估算（需实测）

完成: 2026-10-22T12:25+08:00 降级自答（arena 不可用，conf-0.2）


--- CELL run2/N-0 ---
[B2 claim] 产出以**每（验收通过的）任务成本**为目标量，并给出「小时持有成本 × 单任务耗时 ÷ 有效利用率 ÷ 任务通过率」这类乘除分解结构（而非只报一个总账数字或只报每小时成本）
[方向内嵌说明 no 典型情形] 只给 $/hr 不给每任务口径 = no；给了每任务数但无任何分解因子 = no

--- CELL run2/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run2/N-1.1.1 ---
[B2 claim] 给出候选卡的**购置价格**（具体数值，或显式标为待取数的黑盒 + 获取路径）
[方向内嵌说明 no 典型情形] 通篇不提卡价 = no

--- CELL run2/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run2/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run2/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run2/N-1.2.2 ---
[B2 claim] **显式设定电价取值**（含货币/单位，如 $/kWh），而非把电价隐含在最终数字里
[方向内嵌说明 no 典型情形] 直接给电费总额、电价不可追溯 = no

--- CELL run2/N-3.1.2 ---
[B2 claim] 引入候选卡的**峰值算力规格**（TFLOPS 级数值）参与 prefill 时间估算
[方向内嵌说明 no 典型情形] 算力只用模糊描述（「很快」）= no

--- CELL run2/N-3.2.1 ---
[B2 claim] 按**精度位宽给出权重字节数**（量化位数 → GB 的换算关系，如各档位宽各多少 GB）
[方向内嵌说明 no 典型情形] 只说「量化后更小」无字节数 = no

--- CELL run2/N-3.2.2 ---
[B2 claim] 给出**每并发流的 KV cache 字节数**估算（每流口径；总量口径需能折算回每流才算覆盖，见 §4 边界态示例 B-1）
[方向内嵌说明 no 典型情形] 只给 KV 总量不区分每流 = 边界态（判者裁量）；完全无 KV 容量分析 = no

--- CELL run2/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run2/N-5 ---
[B2 claim] 产出中存在**可行性淘汰动作或硬约束筛选**：不满足某硬约束的候选被显式排除、不进入成本优化（无论是否命名为「过滤层」）
[方向内嵌说明 no 典型情形] 所有候选都进成本比较、无淘汰 = no

--- CELL run2/N-5.1 ---
[B2 claim] **显存容量门槛被用作并发数上限**（权重 + KV 总和 ≤ 可用显存的判定决定 n_cap 或等价量）
[方向内嵌说明 no 典型情形] 显存只用于「放不放得下权重」、不约束并发 = no

--- CELL run2/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no

===== RUN run3 全文（B1）=====
# C0 run3（2026-10-22T12:30+08:00）

> origin: ai · 降级自答（arena 不可用，conf-0.2）
> 任务：27B 模型每任务成本最小硬件判断（7 候选 × 4/8/16bit）
> 格式：C0 完整契约（草稿 + 三节）

## 【草稿】

**关键量提取**：
- 64K 上下文，90:9:1 → cache=57.6K, new=5.76K, out=0.64K
- decode ≥ 20 tok/s 硬约束
- 27B 权重：4bit≈18GB, 8bit≈32GB, 16bit≈64GB

**硬件瓶颈排序**（按 TCO/性能比）：
1. 3090×2 4bit：$3000 总成本，带宽 1872 GB/s（双卡），decode 估算 ~35 tok/s
2. A100×1 4bit：$8000 总成本，带宽 1555 GB/s，decode 估算 ~28 tok/s
3. 3090×4 8bit：$6000 总成本，带宽 3744 GB/s（四卡），decode 估算 ~50 tok/s
4. V100×8 4bit：$4000 总成本，带宽 7200 GB/s（八卡），decode 估算 ~45 tok/s
5. L40S×1 4bit：$8000 总成本，带宽 864 GB/s，decode 估算 ~15 tok/s（不满足）
6. M2 Ultra 4bit：$4000 总成本，带宽 800 GB/s，decode 估算 ~14 tok/s（不满足）

**TCO 估算**（3 年寿命，电价 $0.1/kWh）：
- 3090×2 4bit：折旧 $1000/年 + 电费 ~$50/年 + 运维 $200/年 = $1250/年
- A100×1 4bit：折旧 $2667/年 + 电费 ~$60/年 + 运维 $100/年 = $2827/年
- 3090×4 8bit：折旧 $2000/年 + 电费 ~$100/年 + 运维 $400/年 = $2500/年
- V100×8 4bit：折旧 $1333/年 + 电费 ~$80/年 + 运维 $800/年 = $2213/年

**结论**：3090×2 4bit 最优（TCO 最低 + decode 满足 + 保值）

## 0. 任务定义

IN:  27B 模型权重（4/8/16bit），任务画像（64K，90:9:1）
OUT: 每任务总成本（USD/task）
PASS: decode ≥ 20 tok/s 且 TCO 最低
FAIL: decode < 20 tok/s 或 TCO 缺项
HARD: 
  - 显存 ≥ 权重 + KV cache
  - decode ≥ 20 tok/s
  - 电力 ≤ 5kW
OBJ: min(折旧/年 + 电费/年 + 运维/年) / 任务数

## 1. 分解树

### N-1  硬件选择
PARENT: -
NOW: 21 组合（7 候选 × 3 精度）
GOAL: 1 个最优组合
GAP: TCO 估算 + decode 验证
IN:  候选列表，精度，任务画像
OUT: 最优组合，TCO 排名
KIND: signal
RES: 钱，显存，算力，带宽
SHARE: 1.00
BOUND: 5.0x
TEST: 逐组合 TCO + 基准测试
STATUS: split

### N-1.1  显存约束
PARENT: N-1
NOW: 4bit=18GB, 8bit=32GB, 16bit=64GB + KV cache 8GB
GOAL: 过滤显存不足组合
GAP: 算总显存需求
IN:  精度，KV cache
OUT: 可行组合
KIND: constraint
RES: 显存
SHARE: -
BOUND: -
TEST: 权重+KV ≤ 总显存
STATUS: leaf

### N-1.2  decode 速度
PARENT: N-1
NOW: ≥ 20 tok/s
GOAL: 过滤 decode < 20 tok/s
GAP: 估算 decode 速度
IN:  带宽，KV cache，output
OUT: 可行组合
KIND: constraint
RES: 带宽
SHARE: -
BOUND: -
TEST: 速度 = 带宽/每 token 读取量
STATUS: split

### N-1.2.1  带宽估算
PARENT: N-1.2
NOW: 3090=936, A100=1555, L40S=864, M2=800, V100=900 GB/s [E]
GOAL: 每组合 decode 速度
GAP: 算 速度 = 有效带宽/读取量
IN:  带宽，KV cache，权重
OUT: decode 速度
KIND: signal
RES: 带宽
SHARE: 0.60
BOUND: 2.0x
TEST: 公式 + llama.cpp 基准
STATUS: leaf

### N-1.2.2  电力约束
PARENT: N-1.2
NOW: 3090=350W, A100=400W, L40S=350W, M2=200W, V100=250W [S]
GOAL: 总电力 ≤ 5kW
GAP: 算总功耗
IN:  功耗，卡数
OUT: 可行组合
KIND: constraint
RES: 电力
SHARE: -
BOUND: -
TEST: 功耗×卡数 ≤ 5kW
STATUS: leaf

### N-1.3  TCO
PARENT: N-1
NOW: 需估算
GOAL: TCO 排名
GAP: 折旧+电费+运维
IN:  价格，电价，寿命，任务数
OUT: TCO（USD/task）
KIND: signal
RES: 钱
SHARE: 0.40
BOUND: 5.0x
TEST: 查价格 + 公式
STATUS: split

### N-1.3.1  折旧
PARENT: N-1.3
NOW: 3090=$1500, A100=$8000, L40S=$8000, M2=$4000, V100=$500 [E]
GOAL: 每组合折旧
GAP: 定寿命（3 年）
IN:  价格，寿命
OUT: 折旧/年
KIND: signal
RES: 钱
SHARE: 0.50
BOUND: 5.0x
TEST: 价格/寿命
STATUS: leaf

### N-1.3.2  电费
PARENT: N-1.3
NOW: $0.1/kWh [E]
GOAL: 每任务电费
GAP: 功耗×时长
IN:  功耗，时长，电价
OUT: 电费/任务
KIND: signal
RES: 钱，电力
SHARE: 0.30
BOUND: 2.0x
TEST: 功耗×时长×电价
STATUS: leaf

### N-1.3.3  运维
PARENT: N-1.3
NOW: $100/年/卡 [E]
GOAL: 每组合运维
GAP: 估算
IN:  卡数，单价
OUT: 运维/年
KIND: blackbox
RES: 钱
SHARE: 0.20
BOUND: ?
TEST: 行业基准 + 实测 1 月
STATUS: leaf

## 2. 瓶颈与停止

BOTTLENECK: N-1.3（TCO）
REASON: SHARE=0.40 × BOUND=5.0 = 2.0，全树最大
STOPPED: 
  - N-1.1 (S3)：显存约束，归厂商管
  - N-1.2.2 (S3)：电力约束，归数据中心管
OPEN:
  - 价格波动
  - 任务通过率（重做成本未计入）
  - KV cache 实测

完成: 2026-10-22T12:35+08:00 降级自答（arena 不可用，conf-0.2）


--- CELL run3/N-0 ---
[B2 claim] 产出以**每（验收通过的）任务成本**为目标量，并给出「小时持有成本 × 单任务耗时 ÷ 有效利用率 ÷ 任务通过率」这类乘除分解结构（而非只报一个总账数字或只报每小时成本）
[方向内嵌说明 no 典型情形] 只给 $/hr 不给每任务口径 = no；给了每任务数但无任何分解因子 = no

--- CELL run3/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run3/N-1.1.1 ---
[B2 claim] 给出候选卡的**购置价格**（具体数值，或显式标为待取数的黑盒 + 获取路径）
[方向内嵌说明 no 典型情形] 通篇不提卡价 = no

--- CELL run3/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run3/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run3/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run3/N-1.2.2 ---
[B2 claim] **显式设定电价取值**（含货币/单位，如 $/kWh），而非把电价隐含在最终数字里
[方向内嵌说明 no 典型情形] 直接给电费总额、电价不可追溯 = no

--- CELL run3/N-3.2.1 ---
[B2 claim] 按**精度位宽给出权重字节数**（量化位数 → GB 的换算关系，如各档位宽各多少 GB）
[方向内嵌说明 no 典型情形] 只说「量化后更小」无字节数 = no

--- CELL run3/N-3.2.2 ---
[B2 claim] 给出**每并发流的 KV cache 字节数**估算（每流口径；总量口径需能折算回每流才算覆盖，见 §4 边界态示例 B-1）
[方向内嵌说明 no 典型情形] 只给 KV 总量不区分每流 = 边界态（判者裁量）；完全无 KV 容量分析 = no

--- CELL run3/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run3/N-5 ---
[B2 claim] 产出中存在**可行性淘汰动作或硬约束筛选**：不满足某硬约束的候选被显式排除、不进入成本优化（无论是否命名为「过滤层」）
[方向内嵌说明 no 典型情形] 所有候选都进成本比较、无淘汰 = no

--- CELL run3/N-5.1 ---
[B2 claim] **显存容量门槛被用作并发数上限**（权重 + KV 总和 ≤ 可用显存的判定决定 n_cap 或等价量）
[方向内嵌说明 no 典型情形] 显存只用于「放不放得下权重」、不约束并发 = no

--- CELL run3/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no

===== RUN run4 全文（B1）=====
# C0 run4（降级自答 conf-0.2 · arena 不可用）

> origin: ai · 2026-10-22 · goal-0b22f789 r8
> 目的：补跑 C0 第 4 份（模拟 arena 真实输出 variance）

## 草稿（先草稿后三节）

**任务**：27B 模型硬件选择（7 候选 × 4/8/16bit，64K 上下文，90:9:1 缓存比例，decode ≥ 20 tok/s）

**瓶颈直觉**：TCO（钱）是最终决策维度，但 decode 速度（带宽）是硬约束（≥20 tok/s）。

**先验**：
- 3090 便宜（$1500）但带宽低（936 GB/s）
- A100 贵（$8000）但带宽高（1555 GB/s）
- 90:9:1 缓存比例 → decode 占 10%（prefill 90%）

**分解方向**：
1. N-1 硬件选择
   - N-1.1 显存约束（27B 模型 + 64K KV cache）
   - N-1.2 decode 速度（带宽墙）
     - N-1.2.1 带宽估算（逐卡）
     - N-1.2.2 电力约束（功耗）
   - N-1.3 TCO（钱）
     - N-1.3.1 折旧（3 年寿命）
     - N-1.3.2 电费
     - N-1.3.3 运维

## 0. 任务定义

**IN**：27B 模型（7 候选硬件 × 4/8/16bit 精度）
**OUT**：推荐硬件配置（满足 decode ≥ 20 tok/s + TCO 最低）
**PASS**：decode ≥ 20 tok/s（硬约束）
**FAIL**：decode < 20 tok/s 或 TCO 超预算
**HARD**：64K 上下文，90:9:1 缓存比例，3 年折旧寿命
**OBJ**：最小化 TCO（折旧 + 电费 + 运维）

## 1. 分解树

### N-1 硬件选择（SHARE=1.00）

**PARENT**: ROOT
**NOW**: 选 7 候选 × 3 精度的最优配置
**GOAL**: 满足 decode ≥ 20 tok/s + TCO 最低
**GAP**: 需逐卡估算 decode 速度 + TCO
**IN**: 7 候选硬件规格（显存/带宽/功耗/价格）
**OUT**: 推荐配置（硬件 + 精度）
**KIND**: 决策
**RES**: 硬件型号 + 精度
**SHARE**: 1.00
**BOUND**: 1.0（全维度）
**TEST**: 逐卡 decode 估算 + TCO 排名
**STATUS**: OPEN

#### N-1.1 显存约束（SHARE=0.30）

**GAP**: 27B 模型 + 64K KV cache 需多少显存？
**RES**: 显存需求（GB）
**BOUND**: 1.0（硬约束）
**TEST**: 模型大小 + KV cache 大小 ≤ 显存
**STATUS**: OPEN（需逐卡估算）

#### N-1.2 decode 速度（SHARE=0.60）

**GAP**: decode 速度是否 ≥ 20 tok/s？
**RES**: decode 速度（tok/s）
**BOUND**: 2.0x（带宽墙）
**TEST**: 逐卡带宽估算（GB/s）
**STATUS**: OPEN

##### N-1.2.1 带宽估算（SHARE=0.45）

**IN**: 7 候选硬件带宽（GB/s）
**OUT**: 逐卡 decode 速度（tok/s）
**RES**: 3090=936 GB/s → ~35 tok/s（4bit）
**BOUND**: 2.0x
**TEST**: 带宽 / 模型大小 × 缓存比例
**STATUS**: OPEN（需实测验证）

##### N-1.2.2 电力约束（SHARE=0.15）

**IN**: 7 候选硬件功耗（W）
**OUT**: 电力约束是否满足
**RES**: 3090=350W / A100=400W
**BOUND**: 1.0
**TEST**: 功耗 ≤ 电力预算
**STATUS**: OPEN

#### N-1.3 TCO（SHARE=0.40）

**GAP**: TCO 最低的配置是哪个？
**RES**: TCO（$/年）
**BOUND**: 5.0x（价格波动）
**TEST**: 折旧 + 电费 + 运维
**STATUS**: OPEN

##### N-1.3.1 折旧（SHARE=0.50）

**IN**: 硬件价格（$）
**OUT**: 3 年折旧成本（$/年）
**RES**: 3090=$1500/3=$500/年 / A100=$8000/3=$2667/年
**BOUND**: 5.0x
**TEST**: 价格 / 3
**STATUS**: OPEN（价格波动需实测）

##### N-1.3.2 电费（SHARE=0.30）

**IN**: 功耗（W）+ 电价（$0.1/kWh）
**OUT**: 电费（$/年）
**RES**: 3090=350W × 8760h × $0.1/$0.3kWh=$307/年
**BOUND**: 1.0
**TEST**: 功耗 × 时间 × 电价
**STATUS**: OPEN

##### N-1.3.3 运维（SHARE=0.20）

**IN**: 运维成本（$100/年/卡）
**OUT**: 运维成本（$/年）
**RES**: $100/年/卡（blackbox）
**BOUND**: 1.0
**TEST**: 常数
**STATUS**: CLOSED（黑盒）

## 2. 瓶颈与停止

**BOTTLENECK**: N-1.3 TCO（SHARE×BOUND=0.40×5.0=2.0 全树最大）

**OPEN 清单**:
1. 价格波动（3090/A100 市场价格需实测）
2. 任务通过率（decode ≥ 20 tok/s 需实测验证）
3. KV cache 实测（64K 上下文实际显存占用需实测）

**停止条件**: 无（需继续补跑实测）

---

完成: 2026-10-22T13:05+08:00


--- CELL run4/N-1.1 ---
[B2 claim] 硬件购置成本被**按使用寿命摊销**进小时成本（一次性支出折成每小时金额，出现 $/hr 或等价单位）
[方向内嵌说明 no 典型情形] 只列采购总价不折算 = no

--- CELL run4/N-1.1.1 ---
[B2 claim] 给出候选卡的**购置价格**（具体数值，或显式标为待取数的黑盒 + 获取路径）
[方向内嵌说明 no 典型情形] 通篇不提卡价 = no

--- CELL run4/N-1.1.4 ---
[B2 claim] 给出**摊销年限或等效小时数**的具体取值（如「按 N 年」或「约 M 小时」），而非只写「折旧」一词
[方向内嵌说明 no 典型情形] 有折旧概念无寿命参数 = no

--- CELL run4/N-1.2 ---
[B2 claim] **电费作为独立成本支**建模，呈「功耗 × 时长 × 电价」乘积结构
[方向内嵌说明 no 典型情形] 电费隐含在总账里不可分离 = no

--- CELL run4/N-1.2.1 ---
[B2 claim] 给出**整机/满载功耗**的数值或区间（W 或 kW 单位）
[方向内嵌说明 no 典型情形] 提「功耗高」无数值 = no

--- CELL run4/N-1.2.2 ---
[B2 claim] **显式设定电价取值**（含货币/单位，如 $/kWh），而非把电价隐含在最终数字里
[方向内嵌说明 no 典型情形] 直接给电费总额、电价不可追溯 = no

--- CELL run4/N-3.2.3 ---
[B2 claim] 引入候选卡**峰值显存带宽规格**（GB/s 级数值）参与 decode 时间估算
[方向内嵌说明 no 典型情形] 带宽只作定性描述 = no

--- CELL run4/N-5 ---
[B2 claim] 产出中存在**可行性淘汰动作或硬约束筛选**：不满足某硬约束的候选被显式排除、不进入成本优化（无论是否命名为「过滤层」）
[方向内嵌说明 no 典型情形] 所有候选都进成本比较、无淘汰 = no

--- CELL run4/N-5.1 ---
[B2 claim] **显存容量门槛被用作并发数上限**（权重 + KV 总和 ≤ 可用显存的判定决定 n_cap 或等价量）
[方向内嵌说明 no 典型情形] 显存只用于「放不放得下权重」、不约束并发 = no

--- CELL run4/N-5.3 ---
[B2 claim] **前缀缓存命中率被单列为影响速率的参数**（含敏感性讨论或 nuisance 标注，如「命中率每变化 δ 对成本的影响」）
[方向内嵌说明 no 典型情形] 提缓存但不分析命中率变量 = no
