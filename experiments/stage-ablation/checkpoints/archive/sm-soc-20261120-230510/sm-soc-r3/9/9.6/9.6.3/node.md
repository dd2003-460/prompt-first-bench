# N303: λ_silent 的品类异质性修正项：对于标准化程度高的品类（如手机），σ 较小，λ_silent 趋向区间上限 0.5；对于非标品（如二手家具），σ 较大，λ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

λ_silent 的品类异质性修正项：对于标准化程度高的品类（如手机），σ 较小，λ_silent 趋向区间上限 0.5；对于非标品（如二手家具），σ 较大，λ_silent 趋向区间下限 0.1；修正公式为 λ_silent_base * (1 + β * (1 - Standardization_Score))，其中 β 为品类敏感度系数。

## Corrected Claim

λ_silent 的品类异质性修正项：对于标准化程度高的品类（如手机），σ 较小，λ_silent 趋向区间上限 0.5；对于非标品（如二手家具），σ 较大，λ_silent 趋向区间下限 0.1；修正公式为 λ_silent_base * (1 + β * (1 - Standardization_Score))，其中 β 为品类敏感度系数。

## Evidence

先验知识/题面给定，逻辑校验通过
