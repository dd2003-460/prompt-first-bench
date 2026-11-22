# N164: 工作点3（高匹配率）：P_content_match = 0.9，f_update = 1 - 0.1 * P_updated_in_cache，在 T_res

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点3（高匹配率）：P_content_match = 0.9，f_update = 1 - 0.1 * P_updated_in_cache，在 T_residence=100 天时 f_update = 1 - 0.1 * 0.632 = 0.937，折损 6.3%，接近可忽略

## Corrected Claim

工作点3（高匹配率）：P_content_match = 0.9，f_update = 1 - 0.1 * P_updated_in_cache，在 T_residence=100 天时 f_update = 1 - 0.1 * 0.632 = 0.937，折损 6.3%，接近可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - 0.1 * 0.632 = 0.938，与陈述中的 0.937 存在微小舍入差异（0.1%），但在工程估算语境下可视为一致，折损 6.3% 符合逻辑。
