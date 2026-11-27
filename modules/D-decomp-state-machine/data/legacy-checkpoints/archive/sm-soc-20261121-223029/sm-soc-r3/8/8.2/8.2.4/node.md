# N350: 买家搜索频率 f_search 的量化估计：f_search 定义为单位时间内买家主动搜索并查看某类商品的频率，需基于平台日志计算 f_search = N_s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116, N117, N118

## Claim

买家搜索频率 f_search 的量化估计：f_search 定义为单位时间内买家主动搜索并查看某类商品的频率，需基于平台日志计算 f_search = N_search_events / (N_users * T_window)，典型二手平台 f_search 约为 0.5-2.0 次/小时/用户，需检索具体平台数据以确定用于 E[Inquiries] 计算的具体数值。

## Corrected Claim

买家搜索频率 f_search 定义为单位时间内买家主动搜索并查看某类商品的频率，计算公式为 f_search = N_search_events / (N_users * T_window)。具体数值需基于特定平台的日志数据计算，不同平台及用户群体差异较大，无法给出通用的固定范围。

## Evidence

[质询]该陈述包含具体的经验数值（0.5-2.0 次/小时/用户），属于二手平台用户行为统计，无法从第一性原理推导，且参考来源完全无关，缺乏数据支持。 | 逻辑自洽（量纲正确，定义合理），但参考来源 [1][2][3] 均与二手平台搜索频率无关，无法提供外部证据支持具体数值范围，属于经验事实缺来源支持。

## Search Query

second hand platform user search frequency average hourly rate

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/WatchOS', 'type': 'wikipedia', 'title': 'WatchOS'}
- {'url': 'https://en.wikipedia.org/wiki/AMPRNet', 'type': 'wikipedia', 'title': 'AMPRNet'}
- {'url': 'https://en.wikipedia.org/wiki/Glossary_of_geography_terms_%28N%E2%80%93Z%29', 'type': 'wikipedia', 'title': 'Glossary of geography terms (N–Z)'}
