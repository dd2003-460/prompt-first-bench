# N215: PCIe 4.0 x16 在双卡 TP 场景下的有效双向带宽实测值通常为 25-28 GB/s（理论 32 GB/s），需扣除协议头开销，此数值作为计算通信延迟

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

PCIe 4.0 x16 在双卡 TP 场景下的有效双向带宽实测值通常为 25-28 GB/s（理论 32 GB/s），需扣除协议头开销，此数值作为计算通信延迟分母的基础参数。

## Corrected Claim

PCIe 4.0 x16 在双卡 TP 场景下的有效双向带宽实测值通常为 25-28 GB/s（理论 32 GB/s），需扣除协议头开销，此数值作为计算通信延迟分母的基础参数。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽约 32 GB/s，扣除协议开销后有效带宽 25-28 GB/s 符合工程常识与物理限制。

## Search Query

PCIe 4.0 x16 effective bandwidth GB/s dual gpu tensor parallelism
