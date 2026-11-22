# N119: 总请求字节数 Total_Bytes 的精确表达式为 Total_Bytes = Q_req * E[S|request]，其中 E[S|request] = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41, N42, N43

## Claim

总请求字节数 Total_Bytes 的精确表达式为 Total_Bytes = Q_req * E[S|request]，其中 E[S|request] = ∫ s * f_H(s) ds，f_H(s) 为按热度加权的对象大小分布；在 ρ=-0.3 负相关下，E[S|request] ≈ 0.85 MB（相比无相关时的 1 MB），导致 Total_Bytes ≈ 42.5 TB/天。

## Corrected Claim

总请求字节数 Total_Bytes 的精确表达式为 Total_Bytes = Q_req * E[S|request]，其中 E[S|request] = ∫ s * f_H(s) ds，f_H(s) 为按热度加权的对象大小分布；在 ρ=-0.3 负相关下，E[S|request] ≈ 0.85 MB（相比无相关时的 1 MB），导致 Total_Bytes ≈ 42.5 TB/天。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合概率论期望定义，数值计算（0.85 * 50 = 42.5）自洽，负相关导致均值降低符合直觉。

## Search Query

heat weighted average object size negative correlation CDN
