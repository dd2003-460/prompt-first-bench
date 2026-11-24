# N95: 平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB，取中值 150 KB = 0.000143 GB，[时效待核]。

## Corrected Claim

平均单张图片大小 s_img，基于典型 C 端图片压缩参数（JPEG/WebP，分辨率 1080x1080，质量 80%）估算，典型值约为 100-200 KB，取中值 150 KB = 0.000143 GB，[时效待核]。

## Evidence

先验知识/题面给定，逻辑校验通过：1080x1080分辨率、质量80%的JPEG/WebP图片典型大小确实在100-200KB区间，150KB为中值且单位换算正确（150KB ≈ 0.000143GB）。

## Search Query

average compressed image size 1080p webp jpeg
