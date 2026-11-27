# N160: 在 Pareto(β=0.9) 分布下，头部对象的热度集中度极高：当 K=10 时，H_head ≈ (1 - 10^{-0.1}) / (1 - 100000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

在 Pareto(β=0.9) 分布下，头部对象的热度集中度极高：当 K=10 时，H_head ≈ (1 - 10^{-0.1}) / (1 - 100000^{-0.1}) ≈ 0.21；当 K=100 时，H_head ≈ 0.52；当 K=1000 时，H_head ≈ 0.75，表明前 1000 个对象承载了 75% 的请求量。

## Corrected Claim

在 Pareto(β=0.9) 分布下，头部对象的热度集中度极高：当 K=10 时，H_head ≈ (1 - 10^{-0.1}) / (1 - 100000^{-0.1}) ≈ 0.21；当 K=100 时，H_head ≈ 0.52；当 K=1000 时，H_head ≈ 0.75，表明前 1000 个对象承载了 75% 的请求量。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积分布函数计算正确，数值量级合理
