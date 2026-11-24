# N598: 合并后 List 操作耗时 T_list_new = T_list_old / 8，若 T_list_old=58.25h，则 T_list_new ≈ 7.2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N212

## Claim

合并后 List 操作耗时 T_list_new = T_list_old / 8，若 T_list_old=58.25h，则 T_list_new ≈ 7.28 小时，人力成本降低 87.5%

## Corrected Claim

合并后 List 操作耗时 T_list_new = T_list_old / 8，若 T_list_old=58.25h，则 T_list_new ≈ 7.28 小时，人力成本降低 87.5%

## Evidence

先验知识/题面给定，逻辑校验通过：58.25 / 8 = 7.28125 ≈ 7.28，成本降低比例 (1 - 1/8) * 100% = 87.5%，计算无误。
