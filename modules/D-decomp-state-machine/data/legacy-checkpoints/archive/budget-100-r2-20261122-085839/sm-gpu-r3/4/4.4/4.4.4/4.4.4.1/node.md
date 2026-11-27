# N226: PCIe 4.0 双向带宽 64 GB/s 是理论峰值，实际有效带宽受协议开销、驱动效率及并发请求影响，通常仅为理论值的 70%-85%。在 TP=2 场景下，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

PCIe 4.0 双向带宽 64 GB/s 是理论峰值，实际有效带宽受协议开销、驱动效率及并发请求影响，通常仅为理论值的 70%-85%。在 TP=2 场景下，若实际带宽为 44.8 GB/s (70%)，则 768 KB 通信延迟从 12 µs 增加至 17.1 µs，需将此修正系数代入延迟模型。

## Corrected Claim

PCIe 4.0 双向带宽 64 GB/s 是理论峰值，实际有效带宽受协议开销、驱动效率及并发请求影响，通常仅为理论值的 70%-85%。在 TP=2 场景下，若实际带宽为 44.8 GB/s (70%)，则 768 KB 通信延迟从 12 µs 增加至 17.1 µs，需将此修正系数代入延迟模型。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论带宽 64 GB/s 符合标准，70% 效率系数及延迟计算（768KB/44.8GB/s ≈ 17.1µs）在数学和工程直觉上均自洽。

## Search Query

PCIe 4.0 effective bandwidth utilization efficiency
