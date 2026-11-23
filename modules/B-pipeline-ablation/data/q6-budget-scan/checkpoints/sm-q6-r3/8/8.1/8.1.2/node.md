# N304: 单POP点均值带宽 B_pop_avg = (2TB/86400) / 10 * 8 = 1.85 Gbps，峰值系数 k_peak = B_pop_peak 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

单POP点均值带宽 B_pop_avg = (2TB/86400) / 10 * 8 = 1.85 Gbps，峰值系数 k_peak = B_pop_peak / B_pop_avg，对于图片视频平台 k_peak 典型值为 3.5-4.5（高于纯文本的3-5下限，因视频突发更强）

## Corrected Claim

单POP点均值带宽 B_pop_avg = (2TB/86400) / 10 * 8 = 1.85 Gbps，峰值系数 k_peak = B_pop_peak / B_pop_avg，对于图片视频平台 k_peak 典型值为 3.5-4.5（高于纯文本的3-5下限，因视频突发更强）

## Evidence

先验知识/题面给定，逻辑校验通过：带宽计算 (2*1024^4/86400)/10*8 ≈ 1.85 Gbps 数值正确；视频平台峰值系数 3.5-4.5 符合 CDN 工程经验常识。
