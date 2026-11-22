# N17: 最小干预策略量化：平台打破均衡的最小干预为‘透明化近期成交均价’（Transparency Intervention），通过展示‘同类商品近7天成交均价 P_a

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

最小干预策略量化：平台打破均衡的最小干预为‘透明化近期成交均价’（Transparency Intervention），通过展示‘同类商品近7天成交均价 P_avg_7d’，降低买家信息不对称度 I_asym，预期将卖家高挂价幅度 ΔP_high 压缩至 5-10%，但会伤害卖家短期利润（ΔProfit_seller < 0）并可能降低平台短期佣金收入（ΔCommission < 0），量化为 ΔP_high_new = ΔP_high_old * (1 - η_transparency)，η_transparency ∈ [0.5, 0.8]。

## Corrected Claim

最小干预策略量化：平台打破均衡的最小干预为‘透明化近期成交均价’（Transparency Intervention），通过展示‘同类商品近7天成交均价 P_avg_7d’，降低买家信息不对称度 I_asym，预期将卖家高挂价幅度 ΔP_high 压缩至 5-10%，但会伤害卖家短期利润（ΔProfit_seller < 0）并可能降低平台短期佣金收入（ΔCommission < 0），量化为 ΔP_high_new = ΔP_high_old * (1 - η_transparency)，η_transparency ∈ [0.5, 0.8]。

## Evidence

先验知识/题面给定，逻辑校验通过
