# N314: 买家搜索行为存在截断效应，实际可匹配买家池大小 N_pool 受限于搜索深度 D_search，因此修正后的匹配概率为 p_match_adj = min(p_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

买家搜索行为存在截断效应，实际可匹配买家池大小 N_pool 受限于搜索深度 D_search，因此修正后的匹配概率为 p_match_adj = min(p_match_theory, D_search / N_total_sellers)，当搜索深度不足时，理论 p_match 会高估实际成交机会。

## Corrected Claim

买家搜索行为存在截断效应，实际可匹配买家池大小 N_pool 受限于搜索深度 D_search，因此修正后的匹配概率为 p_match_adj = min(p_match_theory, D_search / N_total_sellers)，当搜索深度不足时，理论 p_match 会高估实际成交机会。

## Evidence

先验知识/题面给定，逻辑校验通过
