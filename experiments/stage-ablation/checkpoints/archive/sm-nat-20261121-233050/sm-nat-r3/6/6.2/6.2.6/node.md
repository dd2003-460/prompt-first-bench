# N154: N61中 S_35% = x_min * (100/35)^(1/0.1) 的计算错误：Pareto分布的分位数公式为 S_p = x_min * (1-p)^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59, N60, N61

## Claim

N61中 S_35% = x_min * (100/35)^(1/0.1) 的计算错误：Pareto分布的分位数公式为 S_p = x_min * (1-p)^(-1/α)，而非 (100/p)^(1/α)。正确计算：S_35% = 1KB * (1-0.35)^(-1/1.1) = 1KB * (0.65)^(-0.909) ≈ 1.48KB，而非148MB。148MB是第99.999%分位的量级，35%分位应接近x_min。

## Corrected Claim

N61中 S_35% = x_min * (100/35)^(1/0.1) 的计算错误：Pareto分布的分位数公式为 S_p = x_min * (1-p)^(-1/α)，而非 (100/p)^(1/α)。正确计算：S_35% = 1KB * (1-0.35)^(-1/1.1) = 1KB * (0.65)^(-0.909) ≈ 1.48KB，而非148MB。148MB是第99.999%分位的量级，35%分位应接近x_min。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布分位数公式推导正确，数值量级估算合理（35%分位接近最小值，148MB确为极高尾部分位量级）

## Search Query

Pareto distribution quantile function formula correct calculation
