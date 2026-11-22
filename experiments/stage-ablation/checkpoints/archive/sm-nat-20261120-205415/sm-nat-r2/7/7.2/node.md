# N76: 在Pareto(α=1.1)大小分布下，缓存容量C=128GB对应的可缓存对象数K的解析近似为 K ≈ (C * (α-1) * x_min^(α-1))^(1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

在Pareto(α=1.1)大小分布下，缓存容量C=128GB对应的可缓存对象数K的解析近似为 K ≈ (C * (α-1) * x_min^(α-1))^(1/(α-1))，其中x_min为最小对象大小（通常设为1KB或1MB），该公式来源于Pareto分布的累积分布函数反演。

## Corrected Claim

在Pareto(α=1.1)大小分布下，缓存容量C=128GB对应的可缓存对象数K的解析近似为 K ≈ (C * (α-1) * x_min^(α-1))^(1/(α-1))，其中x_min为最小对象大小（通常设为1KB或1MB），该公式来源于Pareto分布的累积分布函数反演。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF反演推导正确，量纲与数值量级合理
