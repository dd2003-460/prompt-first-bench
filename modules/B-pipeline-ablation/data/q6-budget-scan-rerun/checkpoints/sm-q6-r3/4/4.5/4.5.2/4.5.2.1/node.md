# N269: 在均匀地理分布工作点下，单点峰值流量 B_peak_pop = (26.4 Mbps × 3.0) × 0.1 = 7.92 Mbps，此时 10 个 POP 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

在均匀地理分布工作点下，单点峰值流量 B_peak_pop = (26.4 Mbps × 3.0) × 0.1 = 7.92 Mbps，此时 10 个 POP 点负载均衡，单点容量需求最低，基础设施总成本最低，但缺乏应对突发热点的能力。

## Corrected Claim

在均匀地理分布工作点下，单点峰值流量 B_peak_pop = (26.4 Mbps × 3.0) × 0.1 = 7.92 Mbps，此时 10 个 POP 点负载均衡，单点容量需求最低，基础设施总成本最低，但缺乏应对突发热点的能力。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (26.4 * 3.0) * 0.1 = 7.92 正确；均匀分布下负载均衡导致单点峰值最低、总成本最低符合基本网络规划逻辑。
