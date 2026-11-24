# N170: 长尾区域P99延迟达标率计算模型：P99_tail达标率 = P(Latency_tail < 300ms)。假设Latency_tail服从正态分布，均值μ=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

长尾区域P99延迟达标率计算模型：P99_tail达标率 = P(Latency_tail < 300ms)。假设Latency_tail服从正态分布，均值μ=300ms（基于N94估算），标准差σ=50ms（受网络抖动影响），则达标率 = Φ((300-300)/50) = 50%。若μ=250ms, σ=30ms，则达标率 = Φ(1.67) ≈ 95%。

## Corrected Claim

长尾区域P99延迟达标率计算模型：P99_tail达标率 = P(Latency_tail < 300ms)。假设Latency_tail服从正态分布，均值μ=300ms（基于N94估算），标准差σ=50ms（受网络抖动影响），则达标率 = Φ((300-300)/50) = 50%。若μ=250ms, σ=30ms，则达标率 = Φ(1.67) ≈ 95%。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布概率计算正确，Φ(0)=0.5，Φ(1.67)≈0.952，数值量级合理。
