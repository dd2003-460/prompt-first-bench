# N248: 修正因子 κ 的定义式为 κ = H_LRU_actual / H_LRU_lower_bound，其中 H_LRU_lower_bound 来自 N68 (0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

修正因子 κ 的定义式为 κ = H_LRU_actual / H_LRU_lower_bound，其中 H_LRU_lower_bound 来自 N68 (0.65)，H_LRU_actual 来自 N98 (0.78)，因此 κ ≈ 0.78 / 0.65 ≈ 1.20。

## Corrected Claim

修正因子 κ 的定义式为 κ = H_LRU_actual / H_LRU_lower_bound，其中 H_LRU_lower_bound 来自 N68 (0.65)，H_LRU_actual 来自 N98 (0.78)，因此 κ ≈ 0.78 / 0.65 ≈ 1.20。

## Evidence

先验知识/题面给定，逻辑校验通过：0.78 / 0.65 ≈ 1.20 计算正确，定义式逻辑自洽
