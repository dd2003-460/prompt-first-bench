# N381: 商品独特性评分 s_uniqueness 的量化定义：s_uniqueness = 1 - (N_similar_items_active / N_total_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N133, N134, N135

## Claim

商品独特性评分 s_uniqueness 的量化定义：s_uniqueness = 1 - (N_similar_items_active / N_total_items_in_category)，其中 N_similar_items_active 为当前在售且属性相似度>0.8的商品数，该评分需实时计算以反映市场稀缺性动态。

## Corrected Claim

商品独特性评分 s_uniqueness 的量化定义：s_uniqueness = 1 - (N_similar_items_active / N_total_items_in_category)，其中 N_similar_items_active 为当前在售且属性相似度>0.8的商品数，该评分需实时计算以反映市场稀缺性动态。

## Evidence

先验知识/题面给定，逻辑校验通过
