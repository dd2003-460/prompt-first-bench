# N175: 中热度对象的失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，若 T_resident 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

中热度对象的失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，若 T_resident = 1.5 天，则 P_invalid ≈ 1.49%；若 T_resident 修正为 0.5 天，则 P_invalid ≈ 0.5%，需确定 T_resident 的准确值以量化折损。

## Corrected Claim

中热度对象的失效概率 P_invalid 的精确计算：P_invalid = 1 - exp(-0.01 * T_resident)，若 T_resident = 1.5 天，则 P_invalid ≈ 1.49%；若 T_resident 修正为 0.5 天，则 P_invalid ≈ 0.5%，需确定 T_resident 的准确值以量化折损。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-λt) 在 λ=0.01, t=1.5 时计算结果约为 1.4888% (≈1.49%)，在 t=0.5 时约为 0.4988% (≈0.5%)，数值量级与逻辑自洽。

## Search Query

cache invalidation probability exponential decay formula
