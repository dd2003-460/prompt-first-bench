# N96: 信息缺失噪声 σ_info 的量化：定义为卖家无法获取同类商品近期成交数据时的估值偏差标准差，在缺乏算法推荐辅助的长尾品类中，σ_info 通常贡献总噪声的 6

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

信息缺失噪声 σ_info 的量化：定义为卖家无法获取同类商品近期成交数据时的估值偏差标准差，在缺乏算法推荐辅助的长尾品类中，σ_info 通常贡献总噪声的 60%-70%。

## Corrected Claim

信息缺失噪声 σ_info 的量化：定义为卖家无法获取同类商品近期成交数据时的估值偏差标准差，在缺乏算法推荐辅助的长尾品类中，σ_info 是总噪声的主要贡献来源之一。

## Evidence

[质询]该陈述中的具体数值比例（60%-70%）属于经验性统计结论，缺乏普遍适用的理论推导基础，且参考来源完全未涉及二手交易或长尾品类的噪声分解，存在数据无来源支持的风险。 | 参考来源[1]讨论的是量化交易中的时序CTA方法论及背景噪声定义，与二手商品估值噪声分解主题无关，无法提供外部支持；该事实为经验性量化结论，逻辑上自洽但缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

information gap valuation noise seller pricing second hand

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2058866821936297955&rut=0e4ebdb49b070379b03b0a3c28020f76e70c68bf8e159de562053dae739fcd0b', 'type': 'ddg', 'title': '【量化交易系列80研报精读】时序cta方法论综述：市场状态、开仓信号与退出机制 - 知乎'}
