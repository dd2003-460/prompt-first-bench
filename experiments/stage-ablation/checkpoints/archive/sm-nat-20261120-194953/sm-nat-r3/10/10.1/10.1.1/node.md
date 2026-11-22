# N172: 基于 CDN 典型对象存储规模反推 S_max 的约束条件：若总对象数 N=10^5，假设 CDN 总存储容量为 1TB，则平均对象大小 E[S]_total 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

基于 CDN 典型对象存储规模反推 S_max 的约束条件：若总对象数 N=10^5，假设 CDN 总存储容量为 1TB，则平均对象大小 E[S]_total = 1TB/10^5 = 10MB；对比 Pareto(α=1.1) 理论均值 6.9KB，偏差系数 K_bias = 10MB/6.9KB ≈ 1493，表明纯 Pareto(1.1) 假设与典型 CDN 存储规模严重不符，需引入双峰分布或修正 α 值

## Corrected Claim

基于 CDN 典型对象存储规模反推 S_max 的约束条件：若总对象数 N=10^5，假设 CDN 总存储容量为 1TB，则平均对象大小 E[S]_total = 1TB/10^5 = 10MB；对比 Pareto(α=1.1) 理论均值 6.9KB，偏差系数 K_bias = 10MB/6.9KB ≈ 1493，表明纯 Pareto(1.1) 假设与典型 CDN 存储规模严重不符，需引入双峰分布或修正 α 值

## Evidence

先验知识/题面给定，逻辑校验通过：1TB/10^5=10MB，10MB/6.9KB≈1493，计算无误且符合CDN存储规模常识

## Search Query

CDN object storage average size distribution typical values
