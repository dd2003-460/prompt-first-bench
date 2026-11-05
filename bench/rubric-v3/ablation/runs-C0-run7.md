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
