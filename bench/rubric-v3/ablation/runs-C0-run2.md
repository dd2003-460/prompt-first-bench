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
