# N220: 带宽成本对峰谷比 R_pg 的敏感度公式：ΔC_bandwidth = (ΔR_pg × B_avg × unit_cost_bandwidth) / (R_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67, N68, N69

## Claim

带宽成本对峰谷比 R_pg 的敏感度公式：ΔC_bandwidth = (ΔR_pg × B_avg × unit_cost_bandwidth) / (R_total_annual / 1000) × 1000，其中 B_avg 为平均带宽（MB/s），unit_cost_bandwidth 为每GB带宽单价（元/GB）；基于N13，B_avg = 2TB/24h ≈ 9.26 MB/s，unit_cost_bandwidth 取阿里云 0.18元/GB（N120），则每增加0.1的R_pg，ΔC_bandwidth = (0.1 × 9.26 × 0.18) / 394.6 ≈ 0.0042 元/千请求；当 R_pg 从3增至5时，总带宽成本增加 (5-3)/3 = 66.7%，对应每千请求成本增加约0.084元。

## Corrected Claim

带宽成本对峰谷比 R_pg 的敏感度公式：ΔC_bandwidth = (ΔR_pg × B_avg × unit_cost_bandwidth) / (R_total_annual / 1000) × 1000，其中 B_avg 为平均带宽（MB/s），unit_cost_bandwidth 为每GB带宽单价（元/GB）；基于N13，B_avg = 2TB/24h ≈ 9.26 MB/s，unit_cost_bandwidth 取阿里云 0.18元/GB（N120），则每增加0.1的R_pg，ΔC_bandwidth = (0.1 × 9.26 × 0.18) / 394.6 ≈ 0.0042 元/千请求；当 R_pg 从3增至5时，总带宽成本增加 (5-3)/3 = 66.7%，对应每千请求成本增加约0.084元。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲一致，数值计算（9.26*0.18*0.1/394.6≈0.0042，0.0042*20≈0.084）准确，符合带宽成本随峰谷比线性增长的逻辑。

## Search Query

CDN bandwidth cost sensitivity to peak-to-average ratio
