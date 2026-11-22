# N97: 买家搜索成本 C_search 与比价收益 ΔU 的阈值关系：高挂价策略占优的条件为 C_search > ΔU * p_match；C_search 可量化为

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

买家搜索成本 C_search 与比价收益 ΔU 的阈值关系：高挂价策略占优的条件为 C_search > ΔU * p_match；C_search 可量化为搜索时间 T_search * W_buyer（W_buyer 为买家时间价值，约 20-50 元/小时），ΔU 为发现低价商品的预期收益；当 C_search > 50 元/次时，高挂价策略在 ESS 中稳定。

## Corrected Claim

买家搜索成本 C_search 通常量化为搜索时间 T_search 乘以买家时间价值 W_buyer。高挂价策略占优的一般条件为搜索成本高于比价带来的预期收益（C_search > ΔU * p_match）。具体阈值（如50元/次）取决于特定市场环境下买家的时间价值分布及商品价差，并非通用常数。

## Evidence

[质询]陈述中关于“C_search > 50 元/次”作为高挂价策略在 ESS 中稳定的具体阈值缺乏理论推导支持，且将复杂的博弈均衡条件简化为单一数值阈值在逻辑上过于武断；此外，W_buyer 的取值范围（20-50元/小时）属于经验估计，不同地区和人群差异巨大，直接用于推导通用阈值存在口径混淆风险。 | 来源[1]仅定义了搜索成本的概念，未提供具体的量化公式、阈值数值或 ESS 均衡条件，属于间接相关但无直接支持；该事实包含具体经验参数（50元阈值、20-50元/小时），逻辑自洽但缺乏来源直接支持，符合经验事实排除条款。

## Search Query

consumer search cost threshold comparison benefit evolutionary stable strategy pricing

## Retrieval Sources

- {'url': 'https://www.scribd.com/presentation/987999160/%E7%AC%AC3%E7%AB%A0-%E6%90%9C%E7%B4%A2%E6%88%90%E6%9C%AC&rut=2a9549f3fbecb4852aca64692e25174b6016e5f3961fe0bea7352b381d4c6fff', 'type': 'ddg', 'title': '第3章 搜索成本 | PDF - Scribd'}
