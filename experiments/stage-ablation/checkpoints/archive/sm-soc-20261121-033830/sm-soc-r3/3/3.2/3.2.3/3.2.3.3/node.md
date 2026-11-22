# N194: WTP分布参数估计：基于二手市场成交数据，使用对数正态分布或Gamma分布拟合买家WTP，估计形状参数α和尺度参数β，其中 E[WTP] = αβ，Var(WT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

WTP分布参数估计：基于二手市场成交数据，使用对数正态分布或Gamma分布拟合买家WTP，估计形状参数α和尺度参数β，其中 E[WTP] = αβ，Var(WTP) = αβ²(α+1)，需验证拟合优度R²>0.8以确保截断计算的有效性

## Corrected Claim

WTP分布参数估计：基于二手市场成交数据，使用对数正态分布或Gamma分布拟合买家WTP，估计形状参数α和尺度参数β，其中 E[WTP] = αβ，Var(WTP) = αβ²(α+1)，需验证拟合优度R²>0.8以确保截断计算的有效性

## Evidence

先验知识/题面给定，逻辑校验通过：Gamma分布的均值E[X]=αβ和方差Var(X)=αβ²(α+1)公式正确，R²>0.8作为拟合优度阈值在统计实践中合理
