# N98: 请求命中率上界 H_req 的数值计算：代入 N29 求解得到的 k_max 到公式 H_req = 1 - (k_max/100000)^0.1，得到具体的百

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28

## Claim

请求命中率上界 H_req 的数值计算：代入 N29 求解得到的 k_max 到公式 H_req = 1 - (k_max/100000)^0.1，得到具体的百分比数值（例如若 k_max=1000，则 H_req ≈ 1 - (0.01)^0.1 ≈ 0.63）。

## Corrected Claim

请求命中率上界 H_req 的数值计算：代入 N29 求解得到的 k_max 到公式 H_req = 1 - (k_max/100000)^0.1，得到具体的百分比数值（例如若 k_max=1000，则 H_req ≈ 1 - (0.01)^0.1 ≈ 0.63）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 H_req = 1 - (k_max/100000)^0.1 在 k_max=1000 时，(0.01)^0.1 ≈ 0.3695，1 - 0.3695 ≈ 0.6305，数值计算正确且量级合理。
