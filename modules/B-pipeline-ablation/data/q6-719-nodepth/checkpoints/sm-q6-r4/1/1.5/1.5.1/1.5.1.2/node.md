# N185: 源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 40

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 400GB，峰值4小时承载则峰值回源带宽需求 = 400GB×8 / 14400s ≈ 222 Mbps；若 Effective_Bandwidth_to_Origin 受限于 TCP 窗口，需计算 BDP = RTT × Bandwidth，当 RTT=50ms 时，1Gbps 链路需窗口 ≥ 6.25MB 才能打满带宽。

## Corrected Claim

源站出口带宽瓶颈量化：假设源站总出口带宽为 10 Gbps，并发回源请求数 N_concurrent 由未命中流量决定；若未命中流量占比 20%，日均回源 400GB，峰值4小时承载则峰值回源带宽需求 = 400GB×8 / 14400s ≈ 222 Mbps；若 Effective_Bandwidth_to_Origin 受限于 TCP 窗口，需计算 BDP = RTT × Bandwidth，当 RTT=50ms 时，1Gbps 链路需窗口 ≥ 6.25MB 才能打满带宽。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点在逻辑上互斥且覆盖不同带宽场景，正交性良好；但父节点明确包含'BDP计算'和'TCP窗口限制'这一关键物理层约束，而三个子节点仅讨论排队论（M/M/1）和利用率，完全遗漏了BDP部分，导致不完备；此外，三个子节点本质上是同一公式 U = Demand/Bandwidth 在不同带宽参数下的计算实例，属于参数化冗余，可压缩为一个通用公式加具体案例，而非拆分为三个独立节点。）
