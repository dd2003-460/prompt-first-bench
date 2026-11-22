# N177: 搜索耗时 t_search 的微观构成：t_search = t_browse + t_compare + t_decision，其中 t_browse 为浏览

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

搜索耗时 t_search 的微观构成：t_search = t_browse + t_compare + t_decision，其中 t_browse 为浏览列表时间（典型值 2-5 分钟），t_compare 为对比同类商品时间（典型值 5-15 分钟，随候选集数量 N_choices 线性增长），t_decision 为最终决策时间（典型值 1-3 分钟）；需基于平台日志数据校准各分项均值及方差。

## Corrected Claim

搜索耗时 t_search 的微观构成：t_search = t_browse + t_compare + t_decision，其中 t_browse 为浏览列表时间（典型值 2-5 分钟），t_compare 为对比同类商品时间（典型值 5-15 分钟，随候选集数量 N_choices 线性增长），t_decision 为最终决策时间（典型值 1-3 分钟）；需基于平台日志数据校准各分项均值及方差。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

online shopping browsing time comparison time decision time user behavior log analysis
