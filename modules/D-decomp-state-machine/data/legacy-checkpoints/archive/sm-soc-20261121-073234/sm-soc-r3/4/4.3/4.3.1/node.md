# N86: 买家主观估值噪音方差 σ_v² 在二手市场同类商品中的具体数值，需通过买家出价分布的离散程度估算，例如 σ_v² = Var(Bid_i | Item_i)，用

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

买家主观估值噪音方差 σ_v² 在二手市场同类商品中的具体数值，需通过买家出价分布的离散程度估算，例如 σ_v² = Var(Bid_i | Item_i)，用于计算匹配效率函数。

## Corrected Claim

买家主观估值噪音方差 σ_v² 在二手市场同类商品中通常需通过买家出价分布的离散程度进行估算（如 σ_v² ≈ Var(Bid_i | Item_i)），具体数值依赖于市场数据和模型假设，用于计算匹配效率函数。

## Evidence

父节点级核验未通过：不完备（子节点之间逻辑维度清晰（估算方法、异质性特征、边际效应），无重复或矛盾，正交性良好。但完备性不足，父节点明确要求“通过买家出价分布的离散程度估算”，子节点1仅提供了缺乏直接数据时的“代理变量”方案，缺失了基于直接出价数据计算 Var(Bid_i | Item_i) 的标准定义与计算方法这一核心路径。此外，子节点3涉及匹配效率函数，略微超出了父节点仅关注“方差数值估算”的范畴，存在轻微的范围蔓延。）

## Search Query

bid dispersion variance second-hand goods buyer valuation noise

## Retrieval Sources

- {'url': 'https://developer.volcengine.com/articles/7391689062819561523&rut=984f65e5a5adbb1e1c345fef9949ee05a4fcb8e2175654be24cb8f6506b2ed2a', 'type': 'ddg', 'title': '推荐系统（十三）——「阿里」二手市场商品定价方法 - 文章 - 开发者社区 - 火山引擎'}
