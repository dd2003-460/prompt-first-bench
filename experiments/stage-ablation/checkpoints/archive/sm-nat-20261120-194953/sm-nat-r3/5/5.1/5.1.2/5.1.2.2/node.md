# N138: N62 中 '修正因子 1/(1+ρ_auto)' 的适用性边界：该线性修正仅在 ρ_auto < 0.3 时有效；当 β=0.9 导致极端热点集中时，实际自相

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

N62 中 '修正因子 1/(1+ρ_auto)' 的适用性边界：该线性修正仅在 ρ_auto < 0.3 时有效；当 β=0.9 导致极端热点集中时，实际自相关结构是非线性的，需使用 Hurst 指数 H 或长程相关分形维度 D 来描述，修正公式应为 H_LRU_corrected = H_LRU_base * (1 - k * (H - 0.5)^m)，其中 k, m 为经验参数，需通过仿真获取，N62 的线性假设在重尾分布下不成立。

## Corrected Claim

N62 中 '修正因子 1/(1+ρ_auto)' 的适用性边界：该线性修正仅在 ρ_auto < 0.3 时有效；当 β=0.9 导致极端热点集中时，实际自相关结构是非线性的，需使用 Hurst 指数 H 或长程相关分形维度 D 来描述，修正公式应为 H_LRU_corrected = H_LRU_base * (1 - k * (H - 0.5)^m)，其中 k, m 为经验参数，需通过仿真获取，N62 的线性假设在重尾分布下不成立。

## Evidence

先验知识/题面给定，逻辑校验通过
