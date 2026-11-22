# N524: PCIe 4.0 x16 的链路建立和协议头开销约为理论带宽的 5-10%，导致有效载荷带宽 (Payload Bandwidth) 降至 28.8-30.4 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N215

## Claim

PCIe 4.0 x16 的链路建立和协议头开销约为理论带宽的 5-10%，导致有效载荷带宽 (Payload Bandwidth) 降至 28.8-30.4 GB/s，该数值用于计算小消息 (如 8KB All-Reduce) 的传输延迟时更为准确。

## Corrected Claim

PCIe 4.0 x16 的链路建立和协议头开销约为理论带宽的 5-10%，导致有效载荷带宽 (Payload Bandwidth) 降至 28.8-30.4 GB/s，该数值用于计算小消息 (如 8KB All-Reduce) 的传输延迟时更为准确。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽为 32 GB/s，扣除 5-10% 开销后有效带宽约为 28.8-30.4 GB/s，数值量级与工程常识一致。

## Search Query

PCIe 4.0 payload bandwidth overhead percentage
