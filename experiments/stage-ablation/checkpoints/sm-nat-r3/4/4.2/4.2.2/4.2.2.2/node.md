# N146: 各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的更新失效率 R_inv_k 的计算式：R_inv_k = 1 - exp(-u

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的更新失效率 R_inv_k 的计算式：R_inv_k = 1 - exp(-u * T_k)，其中 u = 0.01/day，T_k 为第 k 层对象的平均驻留时间，需基于各层的访问频率和大小分布进行数值计算。

## Corrected Claim

各热度分层（Top-1%, 1%-10%, 10%-90%, 90%-100%）的更新失效率 R_inv_k 的计算式：R_inv_k = 1 - exp(-u * T_k)，其中 u = 0.01/day，T_k 为第 k 层对象的平均驻留时间，需基于各层的访问频率和大小分布进行数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
