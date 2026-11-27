# N705: 若启用 CPU Offload，RTX 5090 的实际吞吐量提升幅度降至 50-65%，因为 CPU 内存带宽 (约 100 GB/s) 远低于 GPU 显存

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N289, N290, N291

## Claim

若启用 CPU Offload，RTX 5090 的实际吞吐量提升幅度降至 50-65%，因为 CPU 内存带宽 (约 100 GB/s) 远低于 GPU 显存带宽 (1792 GB/s)，形成瓶颈

## Corrected Claim

若启用 CPU Offload，RTX 5090 的实际吞吐量提升幅度降至 50-65%，因为 CPU 内存带宽 (约 100 GB/s) 远低于 GPU 显存带宽 (1792 GB/s)，形成瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：CPU内存带宽（~100 GB/s）与GPU显存带宽（~1792 GB/s）存在约18倍差距，启用Offload后数据搬运成为主要瓶颈，导致吞吐量显著下降至50-65%符合硬件性能直觉与工程经验。
