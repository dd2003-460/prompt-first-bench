# N289: 流量权重 α 对成交概率 Q 的弹性系数 ε_Qα = (∂Q/∂α) * (α/Q) 的基准值：在 α∈[0.8, 1.2] 区间内，假设 ε_Qα ≈ 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N98

## Claim

流量权重 α 对成交概率 Q 的弹性系数 ε_Qα = (∂Q/∂α) * (α/Q) 的基准值：在 α∈[0.8, 1.2] 区间内，假设 ε_Qα ≈ 0.5，即 α 每增加 1%，Q 增加 0.5%；该线性假设在极端高溢价（δ>25%）时的失效边界需通过 A/B 测试数据验证。

## Corrected Claim

流量权重 α 对成交概率 Q 的弹性系数 ε_Qα = (∂Q/∂α) * (α/Q) 的基准值：在 α∈[0.8, 1.2] 区间内，假设 ε_Qα ≈ 0.5，即 α 每增加 1%，Q 增加 0.5%；该线性假设在极端高溢价（δ>25%）时的失效边界需通过 A/B 测试数据验证。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

elasticity of conversion rate to traffic weight in recommendation algorithms
