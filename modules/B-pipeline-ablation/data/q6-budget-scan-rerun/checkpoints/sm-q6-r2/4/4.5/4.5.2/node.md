# N86: 自建节点单点峰值流量 B_peak_pop 的计算公式：B_peak_pop = (B_avg_total × R_pg) × geo_share_max，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

自建节点单点峰值流量 B_peak_pop 的计算公式：B_peak_pop = (B_avg_total × R_pg) × geo_share_max，其中 B_avg_total = 26.4 Mbps (基于日均2TB)，R_pg = 3.0 (基于N15峰值占40%流量推算的保守峰谷比)，geo_share_max 为最大单一POP点覆盖的地理流量占比（假设均匀分布下为0.1，Zipf分布下可能高达0.2-0.3）

## Corrected Claim

自建节点单点峰值流量 B_peak_pop 的计算公式：B_peak_pop = (B_avg_total × R_pg) × geo_share_max，其中 B_avg_total = 26.4 Mbps (基于日均2TB)，R_pg = 3.0 (基于N15峰值占40%流量推算的保守峰谷比)，geo_share_max 为最大单一POP点覆盖的地理流量占比（假设均匀分布下为0.1，Zipf分布下可能高达0.2-0.3）

## Evidence

先验知识/题面给定，逻辑校验通过
