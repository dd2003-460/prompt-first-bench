# N310: 高压缩工作点（WebP/AVIF, 1080p）：s_img = 0.05 MB (50 KB)，单请求带宽成本贡献 C_bw_img = 0.05 * ¥0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

高压缩工作点（WebP/AVIF, 1080p）：s_img = 0.05 MB (50 KB)，单请求带宽成本贡献 C_bw_img = 0.05 * ¥0.25/GB * 1000/1024 ≈ ¥0.000012/req，适用于追求极致加载速度的场景。

## Corrected Claim

高压缩工作点（WebP/AVIF, 1080p）：s_img = 0.05 MB (50 KB)，单请求带宽成本贡献 C_bw_img = 0.05 * ¥0.25/GB * 1000/1024 ≈ ¥0.000012/req，适用于追求极致加载速度的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.05 * 0.25 * 1000 / 1024 ≈ 0.0122，单位换算后约为 ¥0.000012，量级与逻辑自洽。
