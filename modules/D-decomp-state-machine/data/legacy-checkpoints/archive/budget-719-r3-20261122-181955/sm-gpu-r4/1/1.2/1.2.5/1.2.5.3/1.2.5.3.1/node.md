# N487: A6000 在 32K 上下文 BF16 精度下，修正后的理论 ITL 为 1 / 12.2 ≈ 82.0 ms/token，而非原 N165 的 112.9 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N165

## Claim

A6000 在 32K 上下文 BF16 精度下，修正后的理论 ITL 为 1 / 12.2 ≈ 82.0 ms/token，而非原 N165 的 112.9 ms/token

## Corrected Claim

A6000 在 32K 上下文 BF16 精度下，修正后的理论 ITL 为 1 / 12.2 ≈ 82.0 ms/token，而非原 N165 的 112.9 ms/token

## Evidence

先验知识/题面给定，逻辑校验通过：1/12.2 ≈ 0.081967，换算为毫秒即 81.97 ms，四舍五入为 82.0 ms，数值计算准确且量级合理。
