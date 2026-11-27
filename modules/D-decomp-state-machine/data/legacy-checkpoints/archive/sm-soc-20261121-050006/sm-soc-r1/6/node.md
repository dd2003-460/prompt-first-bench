# N29: 随机偏好噪声的分布参数估计：基于二手电商平台（如eBay或闲鱼）历史成交数据，买家保留价格 U_i 的分布拟合显示，其尾部指数 α ∈ [1.5, 2.5]（P

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声的分布参数估计：基于二手电商平台（如eBay或闲鱼）历史成交数据，买家保留价格 U_i 的分布拟合显示，其尾部指数 α ∈ [1.5, 2.5]（Pareto分布），标准差 σ_pref ≈ 15-20% * P_median；该噪声结构解释了为何 15-25% 的高挂价仍能通过长尾匹配实现短周期（T_close < 7 days），因为 P_ask 落在 U_i 分布的第 80-90 百分位区间时，匹配概率 p_match 虽降至 0.1-0.2，但匹配买家的支付意愿 WTP 极高，决策时间 Δt_decision < 1 hour。

## Corrected Claim

基于二手电商平台历史成交数据的分布拟合通常显示买家保留价格具有重尾特征（如Pareto分布），且高挂价商品可能通过匹配长尾高支付意愿买家实现快速成交，但具体的尾部指数、标准差及匹配概率数值需依据特定数据集的实证结果确定。

## Evidence

[质询]该陈述包含大量具体的经验性数值参数（如尾部指数α∈[1.5, 2.5]、标准差σ_pref≈15-20%、匹配概率p_match 0.1-0.2、决策时间<1小时等），这些属于二手电商市场的特定统计规律，无法从第一性原理或数学公理中严格推导出来，必须依赖具体的实证数据支持。 | 参考来源[1]和[2]讨论的是基于观测排序的偏好学习算法（IPW、SGD等），与二手电商买家保留价格分布的具体参数估计无关，属于主题不匹配；该事实为经验事实，逻辑上自洽（高挂价对应长尾高WTP买家符合经济学直觉），但缺乏直接来源支持，故降级。

## Retrieval Sources

- {'url': 'https://www.alphaxiv.org/zh/abs/2602.16476&rut=cb404cdd04b4736e2a317b44faff8fa6dcce29aa0ad5ae32f8f3c00260882026', 'type': 'ddg', 'title': '基于观测排序的偏好学习 | alphaXiv'}
- {'url': 'https://www.alphaxiv.org/zh/overview/2602.16476&rut=ccd9f0578af974da89518b5bac46a142b9fef9efb659056063fc271ed5820cff', 'type': 'ddg', 'title': '基于观测排序的偏好学习 | alphaXiv'}
