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
