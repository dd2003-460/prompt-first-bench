# N67: PCIe 5.0 x16 双向带宽与 PCIe 4.0 的对比，以及多卡消费级平台（如 Threadripper）是否支持 PCIe 5.0 对通信开销的影响

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

PCIe 5.0 x16 双向带宽与 PCIe 4.0 的对比，以及多卡消费级平台（如 Threadripper）是否支持 PCIe 5.0 对通信开销的影响

## Corrected Claim

PCIe 5.0 x16 双向带宽与 PCIe 4.0 的对比，以及多卡消费级平台（如 Threadripper）是否支持 PCIe 5.0 对通信开销的影响

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 单向带宽为 64 GB/s，双向为 128 GB/s，是 PCIe 4.0 x16（双向 64 GB/s）的两倍；Threadripper 等高端消费级/工作站平台确实支持 PCIe 5.0，能显著降低多卡通信瓶颈。
