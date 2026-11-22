# N104: 2x RTX 4090 通信开销量化：PCIe 4.0 x16 双向带宽 ~64 GB/s。Tensor Parallelism 每层需 All-Reduce 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2x RTX 4090 通信开销量化：PCIe 4.0 x16 双向带宽 ~64 GB/s。Tensor Parallelism 每层需 All-Reduce 激活值。激活值大小 ≈ Batch_Size * Seq_Len * Hidden_Dim * Bytes。对于 Batch=1, 32K, Hidden=4096, BF16: 32768 * 4096 * 2 = 256 MB。All-Reduce 时间 ≈ 256 MB / 64 GB/s = 4 ms/层。64 层总通信时间 ≈ 256 ms。若 Compute 时间为 100 ms/token，通信开销占比显著 (256%+)，导致 Decode 速度大幅下降。

## Corrected Claim

2x RTX 4090 通信开销量化：PCIe 4.0 x16 双向带宽 ~64 GB/s。Tensor Parallelism 每层需 All-Reduce 激活值。激活值大小 ≈ Batch_Size * Seq_Len * Hidden_Dim * Bytes。对于 Batch=1, 32K, Hidden=4096, BF16: 32768 * 4096 * 2 = 256 MB。All-Reduce 时间 ≈ 256 MB / 64 GB/s = 4 ms/层。64 层总通信时间 ≈ 256 ms。若 Compute 时间为 100 ms/token，通信开销占比显著 (256%+)，导致 Decode 速度大幅下降。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向带宽约 64 GB/s 符合硬件规格；激活值大小计算 (32768 * 4096 * 2 = 256 MB) 及通信时间估算 (256 MB / 64 GB/s = 4 ms) 数学逻辑自洽；64 层总通信时间 256 ms 与 100 ms 计算时间的对比结论在量级上合理。

## Search Query

Tensor Parallelism PCIe bandwidth overhead LLM inference latency
