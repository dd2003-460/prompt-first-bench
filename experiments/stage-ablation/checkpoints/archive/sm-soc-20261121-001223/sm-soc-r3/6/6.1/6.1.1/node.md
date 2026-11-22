# N190: 爬虫调度策略对 T_crawl 的影响参数化：T_crawl 并非固定 6-12 小时，而是服从指数分布或基于优先级的队列调度；定义 T_crawl = Bas

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

爬虫调度策略对 T_crawl 的影响参数化：T_crawl 并非固定 6-12 小时，而是服从指数分布或基于优先级的队列调度；定义 T_crawl = Base_Interval / Priority_Score，其中 Priority_Score 与商品热度、卖家信用分正相关，需量化高热度商品的 T_crawl 是否显著低于长尾商品（如 < 1 小时 vs > 12 小时）。

## Corrected Claim

爬虫调度策略对 T_crawl 的影响参数化：T_crawl 并非固定 6-12 小时，而是服从指数分布或基于优先级的队列调度；定义 T_crawl = Base_Interval / Priority_Score，其中 Priority_Score 与商品热度、卖家信用分正相关，需量化高热度商品的 T_crawl 是否显著低于长尾商品（如 < 1 小时 vs > 12 小时）。

## Evidence

先验知识/题面给定，逻辑校验通过
