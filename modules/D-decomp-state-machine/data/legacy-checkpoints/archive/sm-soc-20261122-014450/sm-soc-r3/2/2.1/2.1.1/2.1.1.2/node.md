# N163: Signal_Quality 的计算输入参数：Seller_Rating 为卖家历史平均评分（5分制），Avg_Rating 为平台同类目卖家平均评分。需获取特

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Signal_Quality 的计算输入参数：Seller_Rating 为卖家历史平均评分（5分制），Avg_Rating 为平台同类目卖家平均评分。需获取特定类目的 Avg_Rating 数值（如 Avg_Rating = 4.5）及高信号卖家的典型 Seller_Rating（如 4.8），以计算 Signal_Quality = (4.8 - 4.5) / 4.5 = 0.0667。

## Corrected Claim

Signal_Quality 的计算公式为 (Seller_Rating - Avg_Rating) / Avg_Rating。其中 Seller_Rating 为卖家历史平均评分，Avg_Rating 为平台同类目卖家平均评分。具体数值需根据实际平台数据获取，示例中若 Seller_Rating=4.8 且 Avg_Rating=4.5，则 Signal_Quality ≈ 0.0667。

## Evidence

[质询]该陈述包含具体的经验数值（Avg_Rating=4.5, Seller_Rating=4.8），属于特定平台或场景下的统计事实，无法从第一性原理或数学公理中严格推导得出，且缺乏外部来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

average seller rating distribution on second-hand trading platforms
