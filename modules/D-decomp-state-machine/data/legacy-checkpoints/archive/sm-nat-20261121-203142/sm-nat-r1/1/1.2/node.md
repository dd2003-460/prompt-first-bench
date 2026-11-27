# N7: 请求热度服从 Pareto(β=0.9) 分布，其期望请求次数 E[R] 在 β≤1 时发散，β>1 时为 E[R] = β/(β-1) * r_min，需明确

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

请求热度服从 Pareto(β=0.9) 分布，其期望请求次数 E[R] 在 β≤1 时发散，β>1 时为 E[R] = β/(β-1) * r_min，需明确 r_min（最小请求频率）以归一化总请求量 5000 万次/天

## Corrected Claim

请求热度服从 Pareto(β=0.9) 分布，其期望请求次数 E[R] 在 β≤1 时发散，β>1 时为 E[R] = β/(β-1) * r_min，需明确 r_min（最小请求频率）以归一化总请求量 5000 万次/天

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（Type I）在形状参数β≤1时均值确实发散，β>1时均值公式为 β/(β-1) * r_min，数学推导正确。
