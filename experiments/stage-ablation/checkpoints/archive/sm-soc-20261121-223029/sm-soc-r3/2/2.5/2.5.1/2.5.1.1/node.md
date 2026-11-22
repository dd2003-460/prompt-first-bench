# N192: Price_Competitiveness (PC) 指标的边界条件修正：当 P_ask < P_ref 时，PC 公式需引入下限保护机制 PC_floor =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Price_Competitiveness (PC) 指标的边界条件修正：当 P_ask < P_ref 时，PC 公式需引入下限保护机制 PC_floor = 0.8，防止过度低价商品获得异常高的竞争力得分；需验证在 δ_max = 0.5 设定下，PC 值域是否严格限制在 [0, 1]，并计算 P_ask = P_ref * 1.25 时的 PC 具体数值（预期 PC ≈ 0.5）。

## Corrected Claim

Price_Competitiveness (PC) 指标的边界条件修正：当 P_ask < P_ref 时，PC 公式需引入下限保护机制 PC_floor = 0.8，防止过度低价商品获得异常高的竞争力得分；需验证在 δ_max = 0.5 设定下，PC 值域是否严格限制在 [0, 1]，并计算 P_ask = P_ref * 1.25 时的 PC 具体数值（预期 PC ≈ 0.5）。

## Evidence

先验知识/题面给定，逻辑校验通过
