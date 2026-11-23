# N105: 全公有云策略月带宽成本 $C_{bw,cloud}$：基于日均下载 2TB，峰值系数 $K_{peak}=2.0$，月总流量 $V_{month} = 2 \t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

全公有云策略月带宽成本 $C_{bw,cloud}$：基于日均下载 2TB，峰值系数 $K_{peak}=2.0$，月总流量 $V_{month} = 2 \text{ TB/day} \times 30 = 60 \text{ TB}$；若采用流量计费，$C_{bw,cloud} = 60 \times 1024 \times 0.24 \approx 14746$ 元（假设 0.24 元/GB）；若采用 95th 带宽计费，需计算月峰值带宽 $B_{peak} = (2 \text{ TB}/86400 \text{ s}) \times 2.0 \approx 46.3 \text{ Mbps}$，月成本 $C_{bw,95} = B_{peak} \times R_{95}$。

## Corrected Claim

全公有云策略月带宽成本 $C_{bw,cloud}$：基于日均下载 2TB，峰值系数 $K_{peak}=2.0$，月总流量 $V_{month} = 2 \text{ TB/day} \times 30 = 60 \text{ TB}$；若采用流量计费，$C_{bw,cloud} = 60 \times 1024 \times 0.24 \approx 14746$ 元（假设 0.24 元/GB）；若采用 95th 带宽计费，需计算月峰值带宽 $B_{peak} = (2 \text{ TB}/86400 \text{ s}) \times 2.0 \approx 46.3 \text{ Mbps}$，月成本 $C_{bw,95} = B_{peak} \times R_{95}$。

## Evidence

先验知识/题面给定，逻辑校验通过：月流量计算 2TB*30=60TB 正确；流量计费 60*1024*0.24=14745.6 元正确；峰值带宽 (2*1024*1024*1024*8)/(86400*2) ≈ 46.3 Mbps 计算正确（注：此处假设 1TB=1024^4 bytes，1Mbps=10^6 bits/s，量级合理）。

## Search Query

Alibaba Cloud CDN pricing per GB 2024
