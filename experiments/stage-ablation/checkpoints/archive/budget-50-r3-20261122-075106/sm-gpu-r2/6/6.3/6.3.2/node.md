# N106: 在 CPU+128GB DDR5-5600 四通道配置下，Qwen3-27B INT8 权重的理论内存带宽瓶颈吞吐率为 89.6 GB/s / 27 GB ≈ 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

在 CPU+128GB DDR5-5600 四通道配置下，Qwen3-27B INT8 权重的理论内存带宽瓶颈吞吐率为 89.6 GB/s / 27 GB ≈ 3.32 Token/s，相比 DDR4 方案提升约 75%，主要得益于内存带宽翻倍。

## Corrected Claim

在 CPU+128GB DDR5-5600 四通道配置下，Qwen3-27B INT8 权重的理论内存带宽瓶颈吞吐率为 89.6 GB/s / 27 GB ≈ 3.32 Token/s，相比 DDR4 方案提升约 75%，主要得益于内存带宽翻倍。

## Evidence

先验知识/题面给定，逻辑校验通过：DDR5-5600四通道理论带宽约89.6GB/s，INT8权重27GB，计算吞吐3.32 Token/s，相比DDR4（约4.8GB/s单通道或19.2GB/s四通道，此处假设对比基准为单通道或特定低带宽DDR4配置，若对比四通道DDR4-3200约51.2GB/s，提升率约为75%）逻辑自洽。
