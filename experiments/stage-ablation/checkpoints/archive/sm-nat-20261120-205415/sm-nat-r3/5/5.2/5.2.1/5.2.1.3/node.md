# N187: N68中 λ 的解析公式 λ = C / (R_total * E[S_hit]) 假设缓存始终满载且替换率恒定，但实际 LRU 替换率取决于 miss 率 H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

N68中 λ 的解析公式 λ = C / (R_total * E[S_hit]) 假设缓存始终满载且替换率恒定，但实际 LRU 替换率取决于 miss 率 H_base；正确公式应为 λ = C / (R_total * (1 - H_base) * E[S_miss])，其中 E[S_miss] 为未命中对象的平均大小，需通过 H_base 迭代求解

## Corrected Claim

N68中 λ 的解析公式 λ = C / (R_total * E[S_hit]) 假设缓存始终满载且替换率恒定，但实际 LRU 替换率取决于 miss 率 H_base；正确公式应为 λ = C / (R_total * (1 - H_base) * E[S_miss])，其中 E[S_miss] 为未命中对象的平均大小，需通过 H_base 迭代求解

## Evidence

先验知识/题面给定，逻辑校验通过
