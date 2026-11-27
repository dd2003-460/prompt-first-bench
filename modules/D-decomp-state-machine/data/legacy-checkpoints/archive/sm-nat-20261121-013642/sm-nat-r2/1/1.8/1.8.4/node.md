# N56: 最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9915，折损约为 0.85 个百分点，可忽略不计但需记录在推导链中

## Corrected Claim

最终折损计算：f_update = 1 - 0.01 * 0.85 ≈ 0.9915，即有效命中率 H_effective = H_byte_LRU * 0.9915，折损约为 0.85 个百分点，可忽略不计但需记录在推导链中

## Evidence

先验知识/题面给定，逻辑校验通过：1 - 0.01 * 0.85 = 0.9915，计算无误，折损比例 0.85% 符合数学推导。
