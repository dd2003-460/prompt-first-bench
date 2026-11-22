# N36: 共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_bu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N6

## Claim

共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_buyer 独立同分布（i.i.d.）N(0, σ²)，但卖家无法直接观测 ε_buyer，仅能观测成交结果，导致信息滞后。

## Corrected Claim

共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_buyer 独立同分布（i.i.d.）N(0, σ²)，但卖家无法直接观测 ε_buyer，仅能观测成交结果，导致信息滞后。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller buyer information asymmetry used market independent noise
