# N385: 视觉显著性参数 η_display 的工程映射公式：η_display = 0.4 * (Font_Size_Ratio) + 0.6 * (Contrast_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

视觉显著性参数 η_display 的工程映射公式：η_display = 0.4 * (Font_Size_Ratio) + 0.6 * (Contrast_Ratio)，其中 Font_Size_Ratio = F_tag / F_baseline (F_baseline为列表页默认字号)，Contrast_Ratio = (L_tag - L_bg) / 255 (L为亮度值)。需确定 F_tag 和 L_tag 的具体像素/亮度值以计算 η_display。

## Corrected Claim

视觉显著性参数 η_display 的工程映射公式：η_display = 0.4 * (Font_Size_Ratio) + 0.6 * (Contrast_Ratio)，其中 Font_Size_Ratio = F_tag / F_baseline (F_baseline为列表页默认字号)，Contrast_Ratio = (L_tag - L_bg) / 255 (L为亮度值)。需确定 F_tag 和 L_tag 的具体像素/亮度值以计算 η_display。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

UI design contrast ratio WCAG formula font size ratio accessibility
