# N57: 工作点1（高命中率场景）：当 H_byte_LRU=0.8 时，T_cold ≈ 128 / (500 * 0.2) = 1.28 天，C_steady = 1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

工作点1（高命中率场景）：当 H_byte_LRU=0.8 时，T_cold ≈ 128 / (500 * 0.2) = 1.28 天，C_steady = 1 - exp(-0.01 * 1.28) ≈ 0.0127，陈旧对象占比约 1.27%

## Corrected Claim

工作点1（高命中率场景）：当 H_byte_LRU=0.8 时，T_cold ≈ 128 / (500 * 0.2) = 1.28 天，C_steady = 1 - exp(-0.01 * 1.28) ≈ 0.0127，陈旧对象占比约 1.27%

## Evidence

先验知识/题面给定，逻辑校验通过：128/(500*0.2)=1.28，1-exp(-0.0128)≈0.0127，计算无误
