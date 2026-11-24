# N401: 日均请求数 R_daily 的精确计算公式为 R_daily = (Daily_Download_Volume_GB × 1024) / s_avg_MB，其中

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N141

## Claim

日均请求数 R_daily 的精确计算公式为 R_daily = (Daily_Download_Volume_GB × 1024) / s_avg_MB，其中 s_avg_MB 为加权平均对象大小，需区分图片(200-500KB)与短视频(5-20MB)的占比 w_img 和 w_vid 进行加权：s_avg_MB = w_img × s_img + w_vid × s_vid

## Corrected Claim

日均请求数 R_daily 的精确计算公式为 R_daily = (Daily_Download_Volume_GB × 1024) / s_avg_MB，其中 s_avg_MB 为加权平均对象大小，需区分图片(200-500KB)与短视频(5-20MB)的占比 w_img 和 w_vid 进行加权：s_avg_MB = w_img × s_img + w_vid × s_vid

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算（GB转MB乘以1024）及加权平均公式在数学上自洽，符合基本物理/经济直觉。
