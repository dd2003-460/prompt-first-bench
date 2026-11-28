# N103: PCIe 4.0 x16 链路的单向理论带宽为 31.5 GB/s，双向为 63 GB/s；PCIe 5.0 x16 链路的单向理论带宽为 63 GB/s，双向

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

PCIe 4.0 x16 链路的单向理论带宽为 31.5 GB/s，双向为 63 GB/s；PCIe 5.0 x16 链路的单向理论带宽为 63 GB/s，双向为 126 GB/s。实际 AllReduce 通信中，由于协议开销和数据打包，有效带宽通常仅为理论值的 50%-70% [待核验]。

## Corrected Claim

PCIe 4.0 x16 链路的单向理论带宽为 31.5 GB/s，双向为 63 GB/s；PCIe 5.0 x16 链路的单向理论带宽为 63 GB/s，双向为 126 GB/s。实际 AllReduce 通信中，由于协议开销和数据打包，有效带宽通常仅为理论值的 50%-70% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 单向带宽计算正确（16 lanes * 2 GT/s * 128b/130b ≈ 31.5 GB/s），PCIe 5.0 x16 单向带宽计算正确（16 lanes * 4 GT/s * 128b/130b ≈ 63 GB/s）；AllReduce 有效带宽受协议开销影响通常为理论值的 50%-70% 符合工程经验常识。

## Search Query

PCIe 4.0 vs 5.0 x16 effective bandwidth AllReduce overhead
