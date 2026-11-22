# N53: 买家容忍阈值 P_max 的动态边界：P_max 并非固定 1.1-1.2 倍，而是 P_max = P_ref * (1 + α * Urgency + β 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

买家容忍阈值 P_max 的动态边界：P_max 并非固定 1.1-1.2 倍，而是 P_max = P_ref * (1 + α * Urgency + β * Scarcity)，其中 Urgency 为买家急需程度，Scarcity 为商品稀缺性指数；需量化 α 和 β 在二手交易中的典型取值范围（如 α ∈ [0.05, 0.1], β ∈ [0.02, 0.08]）。

## Corrected Claim

买家容忍阈值 P_max 可建模为 P_ref 的函数，受急需程度（Urgency）和稀缺性（Scarcity）正向影响，即 P_max = P_ref * (1 + α * Urgency + β * Scarcity)；具体系数 α 和 β 需通过实证数据回归确定，而非固定为特定区间。

## Evidence

[质询]该陈述包含具体的经验参数范围（α ∈ [0.05, 0.1], β ∈ [0.02, 0.08]），属于二手交易市场的经验事实，无法从第一性原理严格推导，且缺乏权威来源直接支持这些具体数值区间。 | 参考来源[1]讨论的是谷歌广告产品（PLA/PMax），与二手交易买家价格容忍度模型完全无关，属于无关来源；该事实为经验性模型参数，逻辑自洽但缺来源支持，依据经验事实排除条款降级。

## Search Query

willingness to pay premium urgency scarcity second hand goods elasticity

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/705128452&rut=dc7c682039e792792d92ba3968914fad99cb078fc0d65c703cdfd58479e74e09', 'type': 'ddg', 'title': '1+1＞2!谷歌购物广告PLA & PMax之间的协同使用 - 知乎'}
