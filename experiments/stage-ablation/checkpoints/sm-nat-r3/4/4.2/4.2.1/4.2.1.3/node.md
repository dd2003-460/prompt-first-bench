# N142: 工作点 B 对象（热度排名 90%-100%）的更新失效率 R_inv_B 的解析表达式：R_inv_B = 1 - exp(-u * T_B)，其中 u = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

工作点 B 对象（热度排名 90%-100%）的更新失效率 R_inv_B 的解析表达式：R_inv_B = 1 - exp(-u * T_B)，其中 u = 0.01/day，T_B 为 N90 计算出的平均驻留时间；当 u * T_B < 0.1 时，可近似为 R_inv_B ≈ u * T_B。

## Corrected Claim

工作点 B 对象（热度排名 90%-100%）的更新失效率 R_inv_B 的解析表达式：R_inv_B = 1 - exp(-u * T_B)，其中 u = 0.01/day，T_B 为 N90 计算出的平均驻留时间；当 u * T_B < 0.1 时，可近似为 R_inv_B ≈ u * T_B。

## Evidence

先验知识/题面给定，逻辑校验通过
