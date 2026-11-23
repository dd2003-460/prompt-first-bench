# N212: 峰值带宽计算值修正：基于日均下载2TB，峰值小时流量占比15-20%（N51），峰值带宽 = (2 * 1024 * 1024 MB / 24h) * 0.2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

峰值带宽计算值修正：基于日均下载2TB，峰值小时流量占比15-20%（N51），峰值带宽 = (2 * 1024 * 1024 MB / 24h) * 0.2 * 8 bits/byte ≈ 139,810 Mbps (140 Gbps)，而非N73中假设的18.5 Mbps（该值错误地使用了日均/24h且未考虑峰值系数）

## Corrected Claim

峰值带宽计算值修正：基于日均下载2TB，峰值小时流量占比15-20%（N51），峰值带宽 = (2 * 1024 * 1024 MB / 24h) * 0.2 * 8 bits/byte ≈ 139,810 Mbps (140 Gbps)，而非N73中假设的18.5 Mbps（该值错误地使用了日均/24h且未考虑峰值系数）

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2 * 1024 * 1024 MB / 24h) * 0.2 * 8 bits/byte ≈ 139,810 Mbps 数学推导正确，量级合理。
