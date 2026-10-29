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
