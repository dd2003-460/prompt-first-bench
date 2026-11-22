# N98: 工作点 1（高性低成）：假设耦合系数 k=0.5，计算修正因子 F_corr = 1 - 0.5 * (-0.3) * (Var(S)/E[S]^2)，其中 V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

工作点 1（高性低成）：假设耦合系数 k=0.5，计算修正因子 F_corr = 1 - 0.5 * (-0.3) * (Var(S)/E[S]^2)，其中 Var(S)/E[S]^2 为 Pareto(α=1.1) 的变异系数平方（需计算具体值），得出 F_corr 的数值及对应的命中率提升百分比。

## Corrected Claim

工作点 1（高性低成）：假设耦合系数 k=0.5，计算修正因子 F_corr = 1 - 0.5 * (-0.3) * (Var(S)/E[S]^2)，其中 Var(S)/E[S]^2 为 Pareto(α=1.1) 的变异系数平方（需计算具体值），得出 F_corr 的数值及对应的命中率提升百分比。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 的变异系数平方为 1/(α-1)^2 - 1 = 1/0.01 - 1 = 99，代入公式 F_corr = 1 - 0.5 * (-0.3) * 99 = 1 + 14.85 = 15.85，计算过程自洽。
