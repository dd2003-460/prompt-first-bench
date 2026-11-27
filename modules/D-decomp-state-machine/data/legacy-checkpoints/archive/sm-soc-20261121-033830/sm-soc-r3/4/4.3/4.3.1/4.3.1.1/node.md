# N236: 工作点A（高溢价/低周转）：P_high = 1.25 * P_median，假设成交概率 P(Sale|P_high) = 0.15，上架成本 C_listi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

工作点A（高溢价/低周转）：P_high = 1.25 * P_median，假设成交概率 P(Sale|P_high) = 0.15，上架成本 C_listing = 0.05 * P_median，计算得 U_seller(A) = 0.15 * 1.25 * P_median - 0.05 * P_median = 0.1375 * P_median，代表卖家追求单次高利润但接受较长等待时间的策略。

## Corrected Claim

工作点A（高溢价/低周转）：P_high = 1.25 * P_median，假设成交概率 P(Sale|P_high) = 0.15，上架成本 C_listing = 0.05 * P_median，计算得 U_seller(A) = 0.15 * 1.25 * P_median - 0.05 * P_median = 0.1375 * P_median，代表卖家追求单次高利润但接受较长等待时间的策略。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.15 * 1.25 - 0.05 = 0.1875 - 0.05 = 0.1375 正确，量纲一致，符合高溢价低周转策略定义。
