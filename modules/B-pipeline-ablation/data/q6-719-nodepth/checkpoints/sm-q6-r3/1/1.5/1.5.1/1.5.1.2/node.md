# N185: 源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 40

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 400GB，峰值4小时承载则峰值回源带宽需求 = 400GB×8 / 14400s ≈ 222 Mbps；若 Effective_Bandwidth_to_Origin 受限于 TCP 窗口，需计算 BDP = RTT × Bandwidth，当 RTT=50ms 时，1Gbps 链路需窗口 ≥ 6.25MB 才能打满带宽。

## Corrected Claim

源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 400GB，峰值4小时承载则峰值回源带宽需求 = 400GB×8 / 14400s ≈ 222 Mbps；若 Effective_Bandwidth_to_Origin 受限于 TCP 窗口，需计算 BDP = RTT × Bandwidth，当 RTT=50ms 时，1Gbps 链路需窗口 ≥ 6.25MB 才能打满带宽。

## Evidence

先验知识/题面给定，逻辑校验通过：400GB*8/14400s≈222Mbps计算正确；BDP=50ms*1Gbps=6.25MB计算正确，符合网络工程基本原理。
