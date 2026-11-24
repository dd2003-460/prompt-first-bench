# N504: 工作点3（高活跃/重负载）：Avg_Requests_Per_User = 50次/天，Total_Requests = 250,000,000次/天，对应月请

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N169

## Claim

工作点3（高活跃/重负载）：Avg_Requests_Per_User = 50次/天，Total_Requests = 250,000,000次/天，对应月请求量 7.5B，用于评估高并发下自建节点带宽与计算资源的边际成本激增。

## Corrected Claim

工作点3（高活跃/重负载）：Avg_Requests_Per_User = 50次/天，Total_Requests = 250,000,000次/天，对应月请求量 7.5B，用于评估高并发下自建节点带宽与计算资源的边际成本激增。

## Evidence

先验知识/题面给定，逻辑校验通过：50次/天/用户 * 5,000,000用户 = 250,000,000次/天，250,000,000 * 30天 = 7.5B次/月，数值量级与内部逻辑自洽。
