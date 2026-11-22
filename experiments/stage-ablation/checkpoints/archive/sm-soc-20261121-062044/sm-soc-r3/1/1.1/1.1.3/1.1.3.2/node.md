# N108: 高风险规避工作点（如低频高价值品类，k≈0.3），P_markup_noise = 0.3 * σ²_pref，若 σ²_pref = 0.05，则 P_mar

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

高风险规避工作点（如低频高价值品类，k≈0.3），P_markup_noise = 0.3 * σ²_pref，若 σ²_pref = 0.05，则 P_markup_noise ≈ 0.015，需通过回归分析确认 k 值是否显著高于 0.1，以判断噪声是否主导溢价。

## Corrected Claim

高风险规避工作点（如低频高价值品类，k≈0.3），P_markup_noise = 0.3 * σ²_pref，若 σ²_pref = 0.05，则 P_markup_noise ≈ 0.015，需通过回归分析确认 k 值是否显著高于 0.1，以判断噪声是否主导溢价。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.3 * 0.05 = 0.015 准确，量纲与逻辑自洽，符合噪声主导溢价的判断逻辑。
