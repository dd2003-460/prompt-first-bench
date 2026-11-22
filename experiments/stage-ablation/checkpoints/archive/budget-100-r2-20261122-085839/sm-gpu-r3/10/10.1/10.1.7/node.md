# N303: 2× RTX 3090 TP=2 方案中，每步 AllReduce 通信量 = 2 * Hidden_Size(4096) * Batch(1) * Bytes

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110, N111, N112

## Claim

2× RTX 3090 TP=2 方案中，每步 AllReduce 通信量 = 2 * Hidden_Size(4096) * Batch(1) * Bytes(2 for BF16 activation) * 48 layers = 768 KB，PCIe 4.0 x16 双向带宽 64 GB/s 下通信耗时 = 768 KB / 64 GB/s ≈ 12 µs

## Corrected Claim

2× RTX 3090 TP=2 方案中，每步 AllReduce 通信量 = 2 * Hidden_Size(4096) * Batch(1) * Bytes(2 for BF16 activation) * 48 layers = 768 KB，PCIe 4.0 x16 双向带宽 64 GB/s 下通信耗时 = 768 KB / 64 GB/s ≈ 12 µs
