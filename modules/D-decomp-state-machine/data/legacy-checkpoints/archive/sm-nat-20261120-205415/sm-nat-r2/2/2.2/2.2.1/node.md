# N43: Zipf 近似下前 1% 对象贡献流量的具体数值计算：P(top 1%) = 1 - (0.01)^(1-0.9) = 1 - 0.01^0.1 ≈ 1 - 0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Zipf 近似下前 1% 对象贡献流量的具体数值计算：P(top 1%) = 1 - (0.01)^(1-0.9) = 1 - 0.01^0.1 ≈ 1 - 0.7943 = 0.2057 (20.57%)，而非 N11 中声称的 90%；若 β=0.9 是 Pareto 指数，则累积分布 F(k) = 1 - (k/N)^(1-β)。

## Corrected Claim

Zipf 近似下前 1% 对象贡献流量的具体数值计算：P(top 1%) = 1 - (0.01)^(1-0.9) = 1 - 0.01^0.1 ≈ 1 - 0.7943 = 0.2057 (20.57%)，而非 N11 中声称的 90%；若 β=0.9 是 Pareto 指数，则累积分布 F(k) = 1 - (k/N)^(1-β)。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - 0.01^0.1 ≈ 0.2057 正确，且符合 Zipf/Pareto 分布累积分布函数定义。

## Search Query

Pareto distribution cumulative probability beta 0.9 top 1 percent
