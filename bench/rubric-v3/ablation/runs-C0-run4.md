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
