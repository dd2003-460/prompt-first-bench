# N314: 标准码率工作点（H.265/HEVC, 1080p, 30s, 4 Mbps）：s_vid = 15 MB，单请求带宽成本贡献 C_bw_vid = 15 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

标准码率工作点（H.265/HEVC, 1080p, 30s, 4 Mbps）：s_vid = 15 MB，单请求带宽成本贡献 C_bw_vid = 15 * ¥0.25/GB * 1000/1024 ≈ ¥0.003662/req，为当前主流高清短视频基准。

## Corrected Claim

标准码率工作点（H.265/HEVC, 1080p, 30s, 4 Mbps）：s_vid = 15 MB，单请求带宽成本贡献 C_bw_vid = 15 * ¥0.25/GB * 1000/1024 ≈ ¥0.003662/req，为当前主流高清短视频基准。

## Evidence

先验知识/题面给定，逻辑校验通过：15MB * 0.25/1024 ≈ 0.003662，计算无误，参数符合H.265 1080p典型码率范围
