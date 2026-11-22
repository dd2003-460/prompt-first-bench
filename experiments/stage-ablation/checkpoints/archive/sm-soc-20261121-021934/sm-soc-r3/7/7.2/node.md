# N133: 未成交商品（Censored Observations）的截断时间 T_censor 分布：在二手交易平台上，未成交商品的 T_censor 通常服从指数分布或

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N56

## Claim

未成交商品（Censored Observations）的截断时间 T_censor 分布：在二手交易平台上，未成交商品的 T_censor 通常服从指数分布或威布尔分布，需估计其形状参数 k 和尺度参数 λ；若 T_censor 的中位数显著低于 T_deal 的中位数，则表明高挂价商品大量滞留在长尾，拉高了 T_mean。

## Corrected Claim

在二手交易平台上，未成交商品的截断时间 T_censor 通常可用指数分布或威布尔分布建模，需估计其形状参数 k 和尺度参数 λ；若 T_censor 的中位数显著低于 T_deal 的中位数，可能表明存在长尾滞留现象，从而拉高 T_mean。

## Evidence

[质询]该陈述包含具体的经验性分布假设（指数/威布尔）及特定平台的市场行为推断（高挂价导致长尾滞留），属于经验事实，无法仅从第一性原理推导，且参考来源未提供相关数据支持。 | 逻辑自洽（截断时间服从生存分析常用分布，中位数差异反映分布形态变化），但参考来源[1]仅解释删失/截断概念，未涉及二手交易具体分布或参数，属经验事实缺来源支持。

## Search Query

censored data distribution unlisted items time to sale Kaplan-Meier estimator second-hand market

## Retrieval Sources

- {'url': 'https://www.zhihu.com/question/365590893&rut=84ed18ec3098cd269a0b50c89cae689a6c017f516677d2b0547a23b26e03687a', 'type': 'ddg', 'title': '解释删失（censored）回归模型，截断（truncated）回归模型与从属截断回归模型的偏效应？ - 知乎'}
