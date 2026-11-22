# N168: 买家点击分布噪声投影 ΔCTR_noise：ε_traffic 对买家点击率的影响 ΔCTR = ε_traffic * β_click，假设点击率对流量变化的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N56

## Claim

买家点击分布噪声投影 ΔCTR_noise：ε_traffic 对买家点击率的影响 ΔCTR = ε_traffic * β_click，假设点击率对流量变化的弹性 β_click ≈ 1.0（线性近似），则 ΔCTR 的标准差为 σ_traffic_abs * CTR_base，需检索基准 CTR_base（如 5%）以计算点击率波动的 95% 置信区间。

## Corrected Claim

买家点击分布噪声投影 ΔCTR_noise：ε_traffic 对买家点击率的影响 ΔCTR = ε_traffic * β_click，假设点击率对流量变化的弹性 β_click ≈ 1.0（线性近似），则 ΔCTR 的标准差为 σ_traffic_abs * CTR_base，需检索基准 CTR_base（如 5%）以计算点击率波动的 95% 置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

click through rate elasticity to traffic volume change marketplace
