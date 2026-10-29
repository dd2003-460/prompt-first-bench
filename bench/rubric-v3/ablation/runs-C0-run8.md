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
