# N54: 更新导致的字节命中率折损系数 f_update = 1 - P_updated_in_cache * (1 - P_content_match)，若更新后内容完

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

更新导致的字节命中率折损系数 f_update = 1 - P_updated_in_cache * (1 - P_content_match)，若更新后内容完全替换则 P_content_match=0，f_update = 1 - λ_u * T_residence

## Corrected Claim

更新导致的字节命中率折损系数 f_update = 1 - P_updated_in_cache * (1 - P_content_match)，若更新后内容完全替换则 P_content_match=0，f_update = 1 - λ_u * T_residence

## Evidence

先验知识/题面给定，逻辑校验通过
