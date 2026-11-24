# N142: 公有云 CDN 冷启动回源带宽占比模型：在日活 500 万、日均 2TB 下载场景下，冷启动（首次请求）产生的回源流量占比 f_cold 约为 5%-10%；该

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

公有云 CDN 冷启动回源带宽占比模型：在日活 500 万、日均 2TB 下载场景下，冷启动（首次请求）产生的回源流量占比 f_cold 约为 5%-10%；该部分流量直接计入回源成本，且因无法被边缘缓存命中，导致 P99 延迟分布尾部变宽。

## Corrected Claim

公有云 CDN 冷启动回源带宽占比模型：在日活 500 万、日均 2TB 下载场景下，冷启动（首次请求）产生的回源流量占比 f_cold 约为 5%-10%；该部分流量直接计入回源成本，且因无法被边缘缓存命中，导致 P99 延迟分布尾部变宽。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cold start origin bandwidth ratio daily active users 5 million
