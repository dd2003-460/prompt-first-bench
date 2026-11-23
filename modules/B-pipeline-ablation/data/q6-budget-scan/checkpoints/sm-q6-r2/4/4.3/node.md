# N50: 基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500KB（纯图片），N_total ≈ 4,000,000 次；若 s_avg 取 5MB（纯视频），N_total ≈ 400,000 次。

## Corrected Claim

基于 s_avg=950KB 和日均下载 2TB，日均请求量 N_total = 2TB / 950KB ≈ 2,193,000 次；若 s_avg 取 500KB（纯图片），N_total ≈ 4,000,000 次；若 s_avg 取 5MB（纯视频），N_total ≈ 400,000 次。

## Evidence

先验知识/题面给定，逻辑校验通过：2TB/950KB≈2.19M, 2TB/500KB=4M, 2TB/5MB=400K，数值量级与计算均正确

## Search Query

CDN request count calculation 2TB daily traffic
