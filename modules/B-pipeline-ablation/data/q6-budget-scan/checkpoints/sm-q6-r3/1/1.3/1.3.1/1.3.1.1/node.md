# N132: 日均 2TB 下载量的平均带宽计算：B_avg = (2 * 1024 * 1024 * 1024 * 8 bits) / 86400 s ≈ 191.4 Mb

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

日均 2TB 下载量的平均带宽计算：B_avg = (2 * 1024 * 1024 * 1024 * 8 bits) / 86400 s ≈ 191.4 Mbps ≈ 0.19 Gbps，此值为 24 小时平均值，未包含峰值系数

## Corrected Claim

日均 2TB 下载量的平均带宽计算：B_avg = (2 * 1024 * 1024 * 1024 * 8 bits) / 86400 s ≈ 191.4 Mbps ≈ 0.19 Gbps，此值为 24 小时平均值，未包含峰值系数

## Evidence

先验知识/题面给定，逻辑校验通过：2TB=2*1024^3 MB，换算为bits后除以86400秒，计算结果约为191.4 Mbps，量级与逻辑均正确。
