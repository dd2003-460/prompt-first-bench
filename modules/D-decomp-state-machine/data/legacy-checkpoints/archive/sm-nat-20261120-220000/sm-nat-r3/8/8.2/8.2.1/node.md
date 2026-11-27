# N138: 逻辑失效折损系数的精确计算：折损系数 = 1 - p_invalid * P_verify_miss，其中 p_invalid = 0.01，P_verify_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

逻辑失效折损系数的精确计算：折损系数 = 1 - p_invalid * P_verify_miss，其中 p_invalid = 0.01，P_verify_miss = P(验证请求未命中) = 1 - H_LRU(C)，若 H_LRU ≈ 0.95，则 P_verify_miss ≈ 0.05，折损系数 ≈ 1 - 0.01 * 0.05 = 0.9995。

## Corrected Claim

逻辑失效折损系数的精确计算：折损系数 = 1 - p_invalid * P_verify_miss，其中 p_invalid = 0.01，P_verify_miss = P(验证请求未命中) = 1 - H_LRU(C)，若 H_LRU ≈ 0.95，则 P_verify_miss ≈ 0.05，折损系数 ≈ 1 - 0.01 * 0.05 = 0.9995。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值代入计算正确（1 - 0.01 * 0.05 = 0.9995），量级合理。
