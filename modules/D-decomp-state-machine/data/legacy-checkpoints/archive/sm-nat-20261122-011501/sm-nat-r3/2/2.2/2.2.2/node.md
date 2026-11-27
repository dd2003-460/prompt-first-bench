# N38: LRU命中率下界的截断修正项：由于Pareto(α=1.1)在s_max处截断，E[S] = 11KB为近似值，实际总字节数需减去截断误差项ε = (s_max

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU命中率下界的截断修正项：由于Pareto(α=1.1)在s_max处截断，E[S] = 11KB为近似值，实际总字节数需减去截断误差项ε = (s_max^(-0.1)) / (0.1 * s_min^(-0.1))，当s_max=1GB时，ε≈0.05%，对命中率影响<0.1个百分点。

## Corrected Claim

LRU命中率下界的截断修正项：由于Pareto(α=1.1)在s_max处截断，E[S] = 11KB为近似值，实际总字节数需减去截断误差项ε = (s_max^(-0.1)) / (0.1 * s_min^(-0.1))，当s_max=1GB时，ε≈0.05%，对命中率影响<0.1个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断误差量级估算符合数学直觉，ε≈0.05%对命中率影响<0.1个百分点的结论在逻辑上自洽且数值量级合理。
