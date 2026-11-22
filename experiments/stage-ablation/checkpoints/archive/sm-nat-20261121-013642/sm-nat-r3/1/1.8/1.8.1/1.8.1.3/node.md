# N160: 工作点3（高驻留时间）：当 T_residence > 500 天时，P_updated_in_cache ≈ 1 - exp(-5) ≈ 0.993，缓存中几

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点3（高驻留时间）：当 T_residence > 500 天时，P_updated_in_cache ≈ 1 - exp(-5) ≈ 0.993，缓存中几乎全为陈旧对象，更新惩罚趋近于 1 - P_content_match

## Corrected Claim

工作点3（高驻留时间）：当 T_residence > 500 天时，P_updated_in_cache ≈ 1 - exp(-5) ≈ 0.993，缓存中几乎全为陈旧对象，更新惩罚趋近于 1 - P_content_match

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - exp(-5) ≈ 0.9932 正确，且符合指数衰减模型在高时间常数下的极限行为。
