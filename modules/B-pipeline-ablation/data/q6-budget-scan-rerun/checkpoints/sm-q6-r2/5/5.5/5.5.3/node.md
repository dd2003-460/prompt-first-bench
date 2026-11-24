# N111: 不确定性对决策的影响量化：计算每种策略的成本均值 μ_strategy 和标准差 σ_strategy；定义决策风险指标 R = |μ_A - μ_B| / (

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

不确定性对决策的影响量化：计算每种策略的成本均值 μ_strategy 和标准差 σ_strategy；定义决策风险指标 R = |μ_A - μ_B| / (σ_A + σ_B)，若 R > 2，则策略 A 显著优于 B（差异远大于不确定性）；若 R < 0.5，则两策略成本无显著差异，需结合 P99 延迟稳定性（σ_P99）进行二级决策。

## Corrected Claim

不确定性对决策的影响量化：计算每种策略的成本均值 μ_strategy 和标准差 σ_strategy；定义决策风险指标 R = |μ_A - μ_B| / (σ_A + σ_B)，若 R > 2，则策略 A 显著优于 B（差异远大于不确定性）；若 R < 0.5，则两策略成本无显著差异，需结合 P99 延迟稳定性（σ_P99）进行二级决策。

## Evidence

先验知识/题面给定，逻辑校验通过
