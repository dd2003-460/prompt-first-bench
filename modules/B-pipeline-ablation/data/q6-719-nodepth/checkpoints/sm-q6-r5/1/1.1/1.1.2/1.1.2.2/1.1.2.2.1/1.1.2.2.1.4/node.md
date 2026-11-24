# N1274: 标准工作点下，单请求带宽成本 C_bw_per_req = s_video_total * P_bw_cloud，在公有云 CDN 下 P_bw_cloud =

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N435

## Claim

标准工作点下，单请求带宽成本 C_bw_per_req = s_video_total * P_bw_cloud，在公有云 CDN 下 P_bw_cloud = 0.2 CNY/GB，C_bw_per_req = 4.0MB / 1024 * 0.2 ≈ ¥0.00078/req。

## Corrected Claim

标准工作点下，单请求带宽成本 C_bw_per_req = s_video_total * P_bw_cloud，在公有云 CDN 下 P_bw_cloud = 0.2 CNY/GB，C_bw_per_req = 4.0MB / 1024 * 0.2 ≈ ¥0.00078/req。

## Evidence

先验知识/题面给定，逻辑校验通过：4.0MB/1024 ≈ 0.00390625 GB，乘以 0.2 CNY/GB 得 0.00078125 CNY，与陈述中的 ≈ ¥0.00078/req 一致，量纲和数值计算正确。
