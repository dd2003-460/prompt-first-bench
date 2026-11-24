# N311: 标准压缩工作点（JPEG/WebP, 1080p, Q=80%）：s_img = 0.15 MB (150 KB)，单请求带宽成本贡献 C_bw_img = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

标准压缩工作点（JPEG/WebP, 1080p, Q=80%）：s_img = 0.15 MB (150 KB)，单请求带宽成本贡献 C_bw_img = 0.15 * ¥0.25/GB * 1000/1024 ≈ ¥0.000036/req，为行业主流基准。

## Corrected Claim

标准压缩工作点（JPEG/WebP, 1080p, Q=80%）：s_img = 0.15 MB (150 KB)，单请求带宽成本贡献 C_bw_img = 0.15 * ¥0.25/GB * 1000/1024 ≈ ¥0.000036/req，为行业主流基准。

## Evidence

先验知识/题面给定，逻辑校验通过：1080p JPEG Q80 典型大小约 150KB，带宽成本计算量级正确（0.15MB * 0.25元/GB ≈ 0.000036元），符合行业基准。
