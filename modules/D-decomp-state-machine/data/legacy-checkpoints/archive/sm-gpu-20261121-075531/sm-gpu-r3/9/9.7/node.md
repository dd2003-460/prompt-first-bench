# N123: 消费级主板 (如 Z790) 双 PCIe 4.0 x8 插槽的单向有效带宽 (GB/s)，考虑协议开销后的实际吞吐能力，作为多卡通信瓶颈的物理上限。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33, N34

## Claim

消费级主板 (如 Z790) 双 PCIe 4.0 x8 插槽的单向有效带宽 (GB/s)，考虑协议开销后的实际吞吐能力，作为多卡通信瓶颈的物理上限。

## Corrected Claim

消费级主板 (如 Z790) 双 PCIe 4.0 x8 插槽的单向有效带宽 (GB/s)，考虑协议开销后的实际吞吐能力，作为多卡通信瓶颈的物理上限。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x8 单向理论带宽为 32 GB/s，扣除协议开销后实际有效吞吐通常在 25-28 GB/s 左右，量级与物理限制相符。
