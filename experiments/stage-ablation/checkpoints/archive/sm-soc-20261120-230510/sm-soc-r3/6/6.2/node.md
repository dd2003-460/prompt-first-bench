# N95: 成交周期缩短幅度 T_shorten 的函数形式：T_shorten = T_base × exp(-μ × (P_ask - V)/σ)，其中 T_base 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

成交周期缩短幅度 T_shorten 的函数形式：T_shorten = T_base × exp(-μ × (P_ask - V)/σ)，其中 T_base 为无筛选时的基础成交周期，μ 为筛选效率系数，反映高意愿买家成交速度的提升倍数。

## Corrected Claim

成交周期缩短幅度 T_shorten 的函数形式：T_shorten = T_base × exp(-μ × (P_ask - V)/σ)，其中 T_base 为无筛选时的基础成交周期，μ 为筛选效率系数，反映高意愿买家成交速度的提升倍数。

## Evidence

父节点级核验未通过：不完备（子节点分别解释了基础参数 T_base、效率系数 μ 以及整体函数的数值验证，彼此独立且无矛盾，正交性良好。但父节点函数中明确包含变量 σ（标准差/波动率），子节点中仅在第3点作为计算输入出现，缺乏对 σ 的定义、来源或典型取值范围的独立解释，导致对函数各组成部分的覆盖不完备。）
