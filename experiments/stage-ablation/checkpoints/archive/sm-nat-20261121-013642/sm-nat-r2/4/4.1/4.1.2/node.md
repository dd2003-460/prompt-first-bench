# N58: 工作点2（中等命中率场景）：当 H_byte_LRU=0.6 时，T_cold ≈ 128 / (500 * 0.4) = 0.64 天，C_steady = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

工作点2（中等命中率场景）：当 H_byte_LRU=0.6 时，T_cold ≈ 128 / (500 * 0.4) = 0.64 天，C_steady = 1 - exp(-0.01 * 0.64) ≈ 0.0064，陈旧对象占比约 0.64%

## Corrected Claim

工作点2（中等命中率场景）：当 H_byte_LRU=0.6 时，T_cold ≈ 128 / (500 * 0.4) = 0.64 天，C_steady = 1 - exp(-0.01 * 0.64) ≈ 0.0064，陈旧对象占比约 0.64%

## Evidence

先验知识/题面给定，逻辑校验通过：128/(500*0.4)=0.64，1-exp(-0.0064)≈0.00637≈0.64%，计算无误
