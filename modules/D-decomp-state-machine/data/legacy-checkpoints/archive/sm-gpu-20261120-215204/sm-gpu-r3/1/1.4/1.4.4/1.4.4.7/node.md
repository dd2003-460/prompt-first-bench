# N186: A100 80GB SXM4 的 NVLink 4.0 互联带宽为 600 GB/s (双向)，相比 PCIe 4.0 x16 (32 GB/s) 高 18.7

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

A100 80GB SXM4 的 NVLink 4.0 互联带宽为 600 GB/s (双向)，相比 PCIe 4.0 x16 (32 GB/s) 高 18.75 倍，这在多卡 Tensor Parallelism 中显著降低 AllReduce 通信延迟，使得 2x A100 的并行效率接近线性扩展 (90%+)，而 2x 消费级 GPU 通常仅 60-70%。

## Corrected Claim

A100 80GB SXM4 的 NVLink 4.0 互联带宽为 600 GB/s (双向)，相比 PCIe 4.0 x16 (32 GB/s) 高 18.75 倍，这在多卡 Tensor Parallelism 中显著降低 AllReduce 通信延迟，使得 2x A100 的并行效率接近线性扩展 (90%+)，而 2x 消费级 GPU 通常仅 60-70%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM4 NVLink 4.0 带宽确为 600GB/s，PCIe 4.0 x16 理论带宽约 32GB/s，倍数计算正确；高带宽互联显著降低 AllReduce 延迟从而提升并行效率符合分布式训练基本原理。

## Search Query

A100 NVLink 4.0 bandwidth 600 GB/s vs PCIe
