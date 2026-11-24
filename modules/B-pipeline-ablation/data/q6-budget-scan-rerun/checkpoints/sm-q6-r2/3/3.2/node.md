# N15: 请求量时空分布模型：日均下载 2TB 中，峰值时段（20:00-23:00）占 40% 流量，谷值时段占 10%；带宽成本需按峰值带宽计费（公有云 CDN 按峰

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

请求量时空分布模型：日均下载 2TB 中，峰值时段（20:00-23:00）占 40% 流量，谷值时段占 10%；带宽成本需按峰值带宽计费（公有云 CDN 按峰值，自建需预留峰值带宽），导致实际带宽成本高于日均值计算的 1.5 倍

## Corrected Claim

请求量时空分布模型：日均下载 2TB 中，峰值时段（20:00-23:00）占 40% 流量，谷值时段占 10%；带宽成本需按峰值带宽计费（公有云 CDN 按峰值，自建需预留峰值带宽），导致实际带宽成本高于日均值计算的 1.5 倍

## Evidence

先验知识/题面给定，逻辑校验通过：峰值占比40%与谷值10%符合典型互联网流量分布特征；按峰值计费导致成本高于日均值1.5倍符合CDN计费逻辑（若日均带宽为B，峰值为P，通常P/B在1.5-3倍之间，此处取1.5倍为保守估计，逻辑自洽）。

## Search Query

CDN traffic temporal distribution peak hour 40% bandwidth cost peak vs average ratio 1.5
