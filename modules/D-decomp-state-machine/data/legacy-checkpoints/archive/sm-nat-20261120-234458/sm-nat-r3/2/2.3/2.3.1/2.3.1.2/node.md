# N124: 截断 Pareto(α=1.1) 的截断方差 Var_S 的数值计算：Var_S = E[S^2] - (E[S])^2，其中 E[S]≈7490KB，E[S^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

截断 Pareto(α=1.1) 的截断方差 Var_S 的数值计算：Var_S = E[S^2] - (E[S])^2，其中 E[S]≈7490KB，E[S^2]≈2.2*10^9 KB^2，计算得 Var_S ≈ 2.2*10^9 - 5.6*10^7 ≈ 2.144*10^9 KB^2

## Corrected Claim

截断 Pareto(α=1.1) 的截断方差 Var_S 的数值计算：Var_S = E[S^2] - (E[S])^2，其中 E[S]≈7490KB，E[S^2]≈2.2*10^9 KB^2，计算得 Var_S ≈ 2.2*10^9 - 5.6*10^7 ≈ 2.144*10^9 KB^2

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 2.2*10^9 - (7490)^2 ≈ 2.2*10^9 - 5.61*10^7 ≈ 2.144*10^9 正确，量纲一致。
