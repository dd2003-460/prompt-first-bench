# N325: PCIe 4.0 x16 接口的实际有效带宽在双向传输时受协议开销影响，通常约为理论峰值 64 GB/s 的 80%-90%，即约 51-58 GB/s；NVL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115

## Claim

PCIe 4.0 x16 接口的实际有效带宽在双向传输时受协议开销影响，通常约为理论峰值 64 GB/s 的 80%-90%，即约 51-58 GB/s；NVLink 3.0 (A100 SXM) 的双向有效带宽约为理论峰值 600 GB/s 的 90% 以上，即约 540+ GB/s。

## Corrected Claim

PCIe 4.0 x16 接口的实际有效带宽在双向传输时受协议开销影响，通常约为理论峰值 64 GB/s 的 80%-90%，即约 51-58 GB/s；NVLink 3.0 (A100 SXM) 的双向有效带宽约为理论峰值 600 GB/s 的 90% 以上，即约 540+ GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 64 GB/s，有效带宽 80-90% 符合工程常识；NVLink 3.0 (A100) 理论带宽 600 GB/s，有效带宽 90%+ 符合 NVIDIA 官方规格及实测数据。

## Search Query

PCIe 4.0 x16 effective bidirectional bandwidth overhead NVLink 3.0 A100 effective bandwidth
