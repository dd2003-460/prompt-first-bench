# N109: 中风险规避工作点（如中等价值品类，k≈0.2），P_markup_noise = 0.2 * σ²_pref，若 σ²_pref = 0.03，则 P_mark

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

中风险规避工作点（如中等价值品类，k≈0.2），P_markup_noise = 0.2 * σ²_pref，若 σ²_pref = 0.03，则 P_markup_noise ≈ 0.006，该工作点下噪声贡献与信号贡献比例约为 1:4，需通过方差分解验证。

## Corrected Claim

中风险规避工作点（如中等价值品类，k≈0.2），P_markup_noise = 0.2 * σ²_pref，若 σ²_pref = 0.03，则 P_markup_noise ≈ 0.006，该工作点下噪声贡献与信号贡献比例约为 1:4，需通过方差分解验证。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.2 * 0.03 = 0.006 正确；噪声(0.006)与信号(0.024)比例 1:4 推导自洽，符合方差分解逻辑。
