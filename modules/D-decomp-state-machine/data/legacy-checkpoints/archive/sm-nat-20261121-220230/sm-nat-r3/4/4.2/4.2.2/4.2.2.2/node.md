# N196: 非线性修正项的数值范围：在 ρ=-0.3 且 α=1.1, β=0.9 的条件下，通过 Frank Copula 数值积分得到的 Δρ 实际值约为 0.03-0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

非线性修正项的数值范围：在 ρ=-0.3 且 α=1.1, β=0.9 的条件下，通过 Frank Copula 数值积分得到的 Δρ 实际值约为 0.03-0.04，而非线性近似的 0.264，此值直接决定了 H_byte 的最终估算区间为 0.13-0.14。

## Corrected Claim

在 ρ=-0.3 且 α=1.1, β=0.9 的条件下，通过 Frank Copula 数值积分得到的 Δρ 实际值约为 0.03-0.04，而非线性近似的 0.264，此值直接决定了 H_byte 的最终估算区间为 0.13-0.14（注：具体数值需依据原始计算数据或可靠文献进一步核实）。

## Evidence

[质询]该陈述包含具体的数值计算结果（Δρ≈0.03-0.04, H_byte≈0.13-0.14），属于经验事实/特定模型计算结果，无法仅通过第一性原理推导得出，且缺乏来源支持以验证其数值准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Frank Copula numerical integration Pareto correlation hit rate
