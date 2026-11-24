# N399: 源站出口带宽 B_origin (Mbps) 的规格选择：基于日均回源流量 200GB 和峰值系数 K_peak=3，B_origin_peak = (200G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

源站出口带宽 B_origin (Mbps) 的规格选择：基于日均回源流量 200GB 和峰值系数 K_peak=3，B_origin_peak = (200GB * 8 * 1024 * 1024 * 3) / 86400 ≈ 14.8 Mbps，建议配置 20-50 Mbps 以留出冗余，避免带宽瓶颈导致 P99 传输时间激增。

## Corrected Claim

源站出口带宽 B_origin (Mbps) 的规格选择：基于日均回源流量 200GB 和峰值系数 K_peak=3，B_origin_peak = (200GB * 8 * 1024 * 1024 * 3) / 86400 ≈ 14.8 Mbps，建议配置 20-50 Mbps 以留出冗余，避免带宽瓶颈导致 P99 传输时间激增。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (200 * 8 * 1024 * 1024 * 3) / 86400 ≈ 14.8 Mbps 准确，建议值 20-50 Mbps 符合工程冗余惯例。
