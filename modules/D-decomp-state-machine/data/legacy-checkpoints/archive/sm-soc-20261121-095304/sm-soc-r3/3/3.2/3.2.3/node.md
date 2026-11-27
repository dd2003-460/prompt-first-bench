# N52: 低质卖家进入概率 P_entry_low_quality 与价格下限 P_floor 负相关：P_entry_low_quality = f(P_floor /

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

低质卖家进入概率 P_entry_low_quality 与价格下限 P_floor 负相关：P_entry_low_quality = f(P_floor / P_market)，当 P_floor 低于市场均价 10% 时，低质卖家进入概率上升幅度 ΔP_entry 需通过历史数据回归估算。

## Corrected Claim

低质卖家进入概率 P_entry_low_quality 通常与价格下限 P_floor 负相关。具体函数形式及阈值（如低于市场均价10%时的影响幅度）需通过特定市场的历史数据回归估算，缺乏通用理论公式。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从函数形式（非线性关系）、经济约束（利润门槛）和实证方法（回归估算）三个不同维度拆解了父节点，逻辑清晰且互不重叠，覆盖了定义、边界和计算方法的完整闭环。）

## Search Query

market entry probability low quality sellers price threshold second hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1955300140131804396&rut=72e9edf7cdcd48da1a50c531d260cfbcec26915c1a0ce6dbb957c22ec105d825', 'type': 'ddg', 'title': '第13篇： 如何精准控制买入卖出价格？entry/exit_pricing 实战配置'}
- {'url': 'https://zhuanlan.zhihu.com/p/2070443219201029608&rut=4c15588b61f449880123ff785ab36e5ddb9ebac00033ce652a2e74bd1bca3156', 'type': 'ddg', 'title': "Lowe's定价实操指南｜VC和3P全拆解 - 知乎"}
