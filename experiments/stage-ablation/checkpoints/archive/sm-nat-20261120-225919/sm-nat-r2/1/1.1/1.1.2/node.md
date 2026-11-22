# N30: 在截断上限 S_max=1.3MB 下，修正后的 Pareto(α=1.1) 平均对象大小 E[S] 计算公式为 E[S] = [S_min^(1.1) - S

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

在截断上限 S_max=1.3MB 下，修正后的 Pareto(α=1.1) 平均对象大小 E[S] 计算公式为 E[S] = [S_min^(1.1) - S_max^(1.1)] / [1.1 * (S_max^(0.1) - S_min^(0.1))]，当 S_min=1KB 时，E[S] ≈ 1.1 * S_min / (1.1 - 1) * (1 - (S_min/S_max)^0.1) ≈ 1.1KB * (1 - 0.43) ≈ 0.63KB，但需根据实际分布积分精确计算

## Corrected Claim

在截断上限 S_max=1.3MB 下，修正后的 Pareto(α=1.1) 平均对象大小 E[S] 应大于 S_min (1KB)。若使用近似公式 E[S] ≈ S_min * (1 - (S_min/S_max)^0.1) / (1 - 0.1) 或其他正确积分形式，结果应在 1KB 至数 KB 之间，具体需根据精确积分计算，但绝不可能小于 1KB。

## Evidence

[质询]数值量级严重错误：根据给定的公式和参数计算，E[S] 应约为 1.1KB 或更大（取决于具体积分形式），而非 0.63KB；且 0.63KB 小于 S_min (1KB)，这在逻辑上是不可能的，因为对象大小不可能小于最小值。 | 逻辑校验失败：计算结果 0.63KB < S_min (1KB)，违背基本定义；且公式推导与数值结果不匹配。

## Search Query

truncated Pareto distribution mean formula
