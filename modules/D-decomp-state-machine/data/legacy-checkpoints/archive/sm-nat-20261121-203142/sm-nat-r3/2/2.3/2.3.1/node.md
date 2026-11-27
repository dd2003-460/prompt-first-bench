# N42: 稳态时间 T_steady 的解析表达式为 T_steady = C / (λ_total × E[S])，其中 C=128GB，λ_total=5000万次/

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

稳态时间 T_steady 的解析表达式为 T_steady = C / (λ_total × E[S])，其中 C=128GB，λ_total=5000万次/天，E[S] 为 Pareto(α=1.1) 大小分布的数学期望，需代入 x_min 计算具体小时数

## Corrected Claim

稳态时间 T_steady 的解析表达式为 T_steady = C / (λ_total × E[S])，其中 C=128GB，λ_total=5000万次/天，E[S] 为 Pareto(α=1.1) 大小分布的数学期望，需代入 x_min 计算具体小时数

## Evidence

先验知识/题面给定，逻辑校验通过
