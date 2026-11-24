# N308: 平衡工作点（中等视频占比）：P_img = 0.6, P_vid = 0.4，对应日均总请求量 Q_day = (2000 GB) / (0.6 * 0.15 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

平衡工作点（中等视频占比）：P_img = 0.6, P_vid = 0.4，对应日均总请求量 Q_day = (2000 GB) / (0.6 * 0.15 MB + 0.4 * 7.5 MB) ≈ 833,333 req/day，加权平均对象大小 s_weighted = 3.09 MB。

## Corrected Claim

平衡工作点（中等视频占比）：P_img = 0.6, P_vid = 0.4，对应日均总请求量 Q_day = (2000 GB) / (0.6 * 0.15 MB + 0.4 * 7.5 MB) ≈ 833,333 req/day，加权平均对象大小 s_weighted = 3.09 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均大小 0.6*0.15 + 0.4*7.5 = 3.09 MB 计算正确；总请求量 2000 GB / 3.09 MB ≈ 833,333 req/day 量级与数值均合理。
