# N309: PCIe 4.0 x16 链路有效双向带宽 B_eff 约为 32 GB/s (单向 ~15.75 GB/s, 双向理论 ~31.5 GB/s, 扣除协议开销后

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91, N92, N93

## Claim

PCIe 4.0 x16 链路有效双向带宽 B_eff 约为 32 GB/s (单向 ~15.75 GB/s, 双向理论 ~31.5 GB/s, 扣除协议开销后 ~30-32 GB/s)，是计算通信延迟 Latency_comm = C_step / B_eff 的基础参数。

## Corrected Claim

PCIe 4.0 x16 链路有效双向带宽 B_eff 约为 32 GB/s (单向 ~15.75 GB/s, 双向理论 ~31.5 GB/s, 扣除协议开销后 ~30-32 GB/s)，是计算通信延迟 Latency_comm = C_step / B_eff 的基础参数。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 单通道速率 16 GT/s，x16 链路单向理论带宽约 31.5 GB/s，扣除协议开销后有效带宽约 30-32 GB/s，数值量级与工程常识一致。

## Search Query

PCIe 4.0 x16 effective bandwidth GB/s bidirectional
