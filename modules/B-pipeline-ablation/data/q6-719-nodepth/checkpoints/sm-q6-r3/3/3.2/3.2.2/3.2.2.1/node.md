# N307: 基准工作点（高图片占比）：P_img = 0.8, P_vid = 0.2，对应日均总请求量 Q_day = (2000 GB) / (0.8 * 0.15 M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

基准工作点（高图片占比）：P_img = 0.8, P_vid = 0.2，对应日均总请求量 Q_day = (2000 GB) / (0.8 * 0.15 MB + 0.2 * 7.5 MB) ≈ 1,428,571 req/day，加权平均对象大小 s_weighted = 1.77 MB。

## Corrected Claim

基准工作点（高图片占比）：P_img = 0.8, P_vid = 0.2，对应日均总请求量 Q_day = (2000 GB) / (0.8 * 0.15 MB + 0.2 * 7.5 MB) ≈ 1,428,571 req/day，加权平均对象大小 s_weighted = 1.77 MB。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均大小 0.8*0.15 + 0.2*7.5 = 1.77 MB；日均请求量 2000 GB / 1.77 MB ≈ 1,428,571 req/day，数值量级与计算逻辑自洽。
