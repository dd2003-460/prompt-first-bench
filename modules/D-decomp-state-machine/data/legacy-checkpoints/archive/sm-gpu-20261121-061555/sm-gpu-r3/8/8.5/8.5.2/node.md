# N361: PCIe 5.0 x16 单向理论带宽为 64 GB/s，双向全双工总带宽为 128 GB/s；实际有效传输带宽受协议开销影响，通常约为理论值的 85-90% 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

PCIe 5.0 x16 单向理论带宽为 64 GB/s，双向全双工总带宽为 128 GB/s；实际有效传输带宽受协议开销影响，通常约为理论值的 85-90% (约 54-58 GB/s 单向)。

## Corrected Claim

PCIe 5.0 x16 单向理论带宽为 64 GB/s，双向全双工总带宽为 128 GB/s；实际有效传输带宽受协议开销影响，通常约为理论值的 85-90% (约 54-58 GB/s 单向)。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 单通道速率 32 GT/s，x16 链路理论带宽 64 GB/s，双向 128 GB/s 符合物理定义；实际带宽受 TLP 头、CRC、流控等开销影响，85-90% 的效率符合工程经验。
