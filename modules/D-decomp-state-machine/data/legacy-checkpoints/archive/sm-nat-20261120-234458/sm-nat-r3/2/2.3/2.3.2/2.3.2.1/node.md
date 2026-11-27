# N127: 冷启动缺失率 P_miss_cold 在 T=1 天观察窗口下的数值计算：P_miss_cold = 1 - (1 - 1/100000)^(50000000 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

冷启动缺失率 P_miss_cold 在 T=1 天观察窗口下的数值计算：P_miss_cold = 1 - (1 - 1/100000)^(50000000 * 1) ≈ 1 - e^(-500) ≈ 1.0，表明在 1 天窗口内几乎所有对象至少被访问一次，冷启动效应可忽略

## Corrected Claim

冷启动缺失率 P_miss_cold 在 T=1 天观察窗口下的数值计算：P_miss_cold = 1 - (1 - 1/100000)^(50000000 * 1) ≈ 1 - e^(-500) ≈ 1.0，表明在 1 天窗口内几乎所有对象至少被访问一次，冷启动效应可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程符合概率论独立事件公式，e^(-500)极小，结论合理
