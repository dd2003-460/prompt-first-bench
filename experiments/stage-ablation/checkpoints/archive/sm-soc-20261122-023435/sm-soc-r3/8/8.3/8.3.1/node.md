# N235: 流量损失量 ΔTraffic_loss 的计算公式：ΔTraffic_loss = T_base * (W_boost_high - W_boost_low) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

流量损失量 ΔTraffic_loss 的计算公式：ΔTraffic_loss = T_base * (W_boost_high - W_boost_low) * (1 - e^(-Δt/T_decay))，其中 T_base 为基准曝光量，W_boost_high/low 为高/低挂价下的流量加权系数，T_decay 为权重衰减时间常数（如 24h），Δt 为降价持续时间。

## Corrected Claim

流量损失量 ΔTraffic_loss 的计算公式：ΔTraffic_loss = T_base * (W_boost_high - W_boost_low) * (1 - e^(-Δt/T_decay))，其中 T_base 为基准曝光量，W_boost_high/low 为高/低挂价下的流量加权系数，T_decay 为权重衰减时间常数（如 24h），Δt 为降价持续时间。

## Evidence

先验知识/题面给定，逻辑校验通过
