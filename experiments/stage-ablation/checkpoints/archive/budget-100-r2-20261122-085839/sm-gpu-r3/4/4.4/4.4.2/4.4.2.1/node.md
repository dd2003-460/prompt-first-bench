# N228: NVLink 4.0 单向 450 GB/s 带宽在 TP=2 场景下，768 KB 通信量的纯传输时间仅 1.7 µs/step，相比 PCIe 4.0 的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

NVLink 4.0 单向 450 GB/s 带宽在 TP=2 场景下，768 KB 通信量的纯传输时间仅 1.7 µs/step，相比 PCIe 4.0 的 12 µs 降低 86%。此带宽优势在 Batch_Size>1 时更为显著，如 Batch=8 时通信量 6 MB，NVLink 传输时间 13.3 µs，而 PCIe 需 93.75 µs，差距扩大至 7 倍。

## Corrected Claim

NVLink 4.0 单向 450 GB/s 带宽在 TP=2 场景下，768 KB 通信量的纯传输时间仅 1.7 µs/step，相比 PCIe 4.0 的 12 µs 降低 86%。此带宽优势在 Batch_Size>1 时更为显著，如 Batch=8 时通信量 6 MB，NVLink 传输时间 13.3 µs，而 PCIe 需 93.75 µs，差距扩大至 7 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：768KB/450GB/s≈1.7µs，768KB/64GB/s≈12µs，6MB/450GB/s≈13.3µs，6MB/64GB/s≈93.75µs，计算均准确且符合NVLink 4.0与PCIe 4.0 x16的典型带宽规格。
