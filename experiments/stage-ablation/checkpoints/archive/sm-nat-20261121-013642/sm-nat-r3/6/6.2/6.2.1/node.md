# N233: 工作点1（保守下界）：假设大小与热度独立（ρ=0），s_cut 由 Pareto(α=1.1) 累积分布确定，s_cut ≈ s_min * (2)^{1/(1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

工作点1（保守下界）：假设大小与热度独立（ρ=0），s_cut 由 Pareto(α=1.1) 累积分布确定，s_cut ≈ s_min * (2)^{1/(1-α)} = 1KB * 2^{10} ≈ 10.24MB，此时缓存覆盖率恰为 50%。

## Corrected Claim

工作点1（保守下界）：假设大小与热度独立（ρ=0），s_cut 由 Pareto(α=1.1) 累积分布确定，s_cut ≈ s_min * (2)^{1/(1-α)} = 1KB * 2^{10} ≈ 10.24MB，此时缓存覆盖率恰为 50%。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布(α=1.1)的累积分布函数推导正确，s_cut计算符合数学定义，且ρ=0假设下缓存覆盖率50%与Pareto分布性质一致
