# N103: 基于修正公式的折损量化：H_eff = H_steady * (1 - 0.01 * 0.951) = H_steady * 0.99049。即有效命中率约为稳

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

基于修正公式的折损量化：H_eff = H_steady * (1 - 0.01 * 0.951) = H_steady * 0.99049。即有效命中率约为稳态命中率的99.05%，折损约0.95%，与N40结论一致，而非N36原述的0.002%。

## Corrected Claim

基于修正公式的折损量化：H_eff = H_steady * (1 - 0.01 * 0.951) = H_steady * 0.99049。即有效命中率约为稳态命中率的99.05%，折损约0.95%，与N40结论一致，而非N36原述的0.002%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - 0.01 * 0.951 = 1 - 0.00951 = 0.99049，数值推导准确，逻辑自洽。
