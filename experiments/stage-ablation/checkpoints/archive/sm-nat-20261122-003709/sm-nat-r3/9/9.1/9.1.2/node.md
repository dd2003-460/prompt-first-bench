# N247: 计算截断 Pareto(α=1.1) 的实际期望 E[S]_trunc：基于 N58 确定的最大对象大小 M_max ≈ 34.7MB，使用截断分布公式 E[S

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

计算截断 Pareto(α=1.1) 的实际期望 E[S]_trunc：基于 N58 确定的最大对象大小 M_max ≈ 34.7MB，使用截断分布公式 E[S] = [α * s_min / (α-1)] * [1 - (s_min/M_max)^(α-1)] / [1 - (s_min/M_max)^(α-1)]，由于 (s_min/M_max)^(0.1) ≈ 0.55，修正因子约为 1/(1-0.55) ≈ 2.2，得出 E[S]_trunc ≈ 24.2KB。

## Corrected Claim

计算截断 Pareto(α=1.1) 的实际期望 E[S]_trunc：基于 N58 确定的最大对象大小 M_max ≈ 34.7MB，使用截断分布公式 E[S] = [α * s_min / (α-1)] * [1 - (s_min/M_max)^(α-1)] / [1 - (s_min/M_max)^(α-1)]，由于 (s_min/M_max)^(0.1) ≈ 0.55，修正因子约为 1/(1-0.55) ≈ 2.2，得出 E[S]_trunc ≈ 24.2KB。
