# N83: 公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg -

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg - 1 = 2.0。这意味着峰值带宽是平均带宽的 3 倍，弹性空间为 2 倍平均带宽。若平均带宽 26.4 Mbps，则弹性伸缩需额外提供 52.8 Mbps 的瞬时容量。

## Corrected Claim

公有云弹性伸缩系数 E_pub 的具体数值：基于峰谷比 R_pg=3，E_pub = (B_peak_pub - B_avg) / B_avg = R_pg - 1 = 2.0。这意味着峰值带宽是平均带宽的 3 倍，弹性空间为 2 倍平均带宽。若平均带宽 26.4 Mbps，则弹性伸缩需额外提供 52.8 Mbps 的瞬时容量。

## Evidence

先验知识/题面给定，逻辑校验通过：基于峰谷比定义 R_pg = B_peak / B_avg，推导 E_pub = (B_peak - B_avg) / B_avg = R_pg - 1 在数学上严格成立；数值计算 26.4 * 2 = 52.8 准确无误。

## Search Query

CDN elasticity coefficient peak to average ratio
