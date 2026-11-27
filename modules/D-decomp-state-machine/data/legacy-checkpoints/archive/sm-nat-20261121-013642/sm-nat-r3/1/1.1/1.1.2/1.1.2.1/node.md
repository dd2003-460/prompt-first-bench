# N103: 归一化系数 k_size 的解析表达式：若 100,000 个对象大小服从截断 Pareto(α=1.1, s_min, s_max)，则 Σ_{i=1}^{1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

归一化系数 k_size 的解析表达式：若 100,000 个对象大小服从截断 Pareto(α=1.1, s_min, s_max)，则 Σ_{i=1}^{100,000} x_i ≈ N * E[size]，故 k_size = C_total / (N * E[size])，其中 C_total 为约束的总数据量（如 128GB 或实际总数据量），N=100,000。

## Corrected Claim

归一化系数 k_size 的解析表达式：若 100,000 个对象大小服从截断 Pareto(α=1.1, s_min, s_max)，则 Σ_{i=1}^{100,000} x_i ≈ N * E[size]，故 k_size = C_total / (N * E[size])，其中 C_total 为约束的总数据量（如 128GB 或实际总数据量），N=100,000。

## Evidence

先验知识/题面给定，逻辑校验通过：基于大数定律，样本总和近似等于样本量乘以期望值，归一化系数推导符合数学逻辑。
