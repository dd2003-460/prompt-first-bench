# N366: PCIe 4.0 协议开销导致的实际有效带宽约为理论值的 90%-95%（即 28.35-30.24 GB/s），主要受 TLP 包头、ACK/NAK 及链路训

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N123

## Claim

PCIe 4.0 协议开销导致的实际有效带宽约为理论值的 90%-95%（即 28.35-30.24 GB/s），主要受 TLP 包头、ACK/NAK 及链路训练开销影响，具体数值取决于传输粒度（通常 >256B 时开销最小）。

## Corrected Claim

PCIe 4.0 协议开销导致的实际有效带宽通常低于理论峰值，具体效率受 TLP 包头、ACK/NAK 及链路训练开销影响，随传输粒度变化，通常在大包传输时效率较高。

## Evidence

[质询]该陈述包含具体的经验性数值范围（90%-95%）和特定阈值（>256B），属于硬件协议性能指标，无法仅从第一性原理严格推导，且缺乏来源支持以确认其精确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

PCIe 4.0 effective bandwidth overhead percentage x8
