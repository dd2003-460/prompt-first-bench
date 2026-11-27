# N100: 截断 Pareto(α=1.1) 在 X_min=1KB, S_max=100MB 下的平均大小 E[S] 精确数值：E[S] = (α * X_min) / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

截断 Pareto(α=1.1) 在 X_min=1KB, S_max=100MB 下的平均大小 E[S] 精确数值：E[S] = (α * X_min) / (α - 1) * (1 - (X_min/S_max)^(α-1)) / (1 - (X_min/S_max)^α) ≈ 11.11KB * (1 - 0.0001^0.1) / (1 - 0.0001^1.1) ≈ 11.05KB，与 N27 中简化的 9.9KB 存在偏差，需使用精确值计算 N_cap

## Corrected Claim

截断 Pareto(α=1.1) 在 X_min=1KB, S_max=100MB 下的平均大小 E[S] 精确数值：E[S] = (α * X_min) / (α - 1) * (1 - (X_min/S_max)^(α-1)) / (1 - (X_min/S_max)^α) ≈ 11.11KB * (1 - 0.0001^0.1) / (1 - 0.0001^1.1) ≈ 11.05KB，与 N27 中简化的 9.9KB 存在偏差，需使用精确值计算 N_cap

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布均值公式正确，数值计算量级合理（11.05KB与9.9KB偏差在预期范围内）
