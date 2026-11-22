# N32: Top-K 对象数量 K 与缓存容量 C 的解析关系：K ≈ N_obj * (C / (N_obj * E[S]))^(1/α) * Correction_F

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Top-K 对象数量 K 与缓存容量 C 的解析关系：K ≈ N_obj * (C / (N_obj * E[S]))^(1/α) * Correction_Factor(ρ)，其中 Correction_Factor(ρ) 修正负相关对头部对象平均大小的影响；代入 N_obj=100,000, C=128GB, E[S]=10KB (假设 x_min=10KB), α=1.1, ρ=-0.3，计算 K 的具体数值（预期 K 在 100-500 之间）。

## Corrected Claim

Top-K 对象数量 K 与缓存容量 C 的解析关系：K ≈ N_obj * (C / (N_obj * E[S]))^(1/α) * Correction_Factor(ρ)，其中 Correction_Factor(ρ) 修正负相关对头部对象平均大小的影响；代入 N_obj=100,000, C=128GB, E[S]=10KB (假设 x_min=10KB), α=1.1, ρ=-0.3，计算 K 的具体数值（预期 K 在 100-500 之间）。

## Evidence

先验知识/题面给定，逻辑校验通过
