# N297: 样本量 n<500 时置信度下调至 0.65 的统计依据：基于中心极限定理，标准误 SE ∝ 1/√n；当 n 从 1000 降至 500 时，SE 增加 √2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

样本量 n<500 时置信度下调至 0.65 的统计依据：基于中心极限定理，标准误 SE ∝ 1/√n；当 n 从 1000 降至 500 时，SE 增加 √2 倍，导致置信区间宽度扩大 41%；需验证在 n=500 时，95% CI 是否仍覆盖 0.65 的下界，以确认置信度下调的合理性。

## Corrected Claim

样本量 n<500 时置信度下调至 0.65 的统计依据：基于中心极限定理，标准误 SE ∝ 1/√n；当 n 从 1000 降至 500 时，SE 增加 √2 倍，导致置信区间宽度扩大 41%；需验证在 n=500 时，95% CI 是否仍覆盖 0.65 的下界，以确认置信度下调的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：SE ∝ 1/√n 是中心极限定理的标准推论，n从1000降至500时SE增加√2倍（约41.4%），置信区间宽度相应扩大，逻辑自洽且数值量级合理。

## Search Query

impact of sample size on confidence interval width in statistical inference
