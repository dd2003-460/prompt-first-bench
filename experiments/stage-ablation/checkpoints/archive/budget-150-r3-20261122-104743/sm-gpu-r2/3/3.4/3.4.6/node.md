# N116: 2×H100 SXM5 方案中，若采用 Tensor Parallelism，通信开销为每生成 1 token 传输一次激活值（约 0.5 GB），单次通信延迟

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，通信开销为每生成 1 token 传输一次激活值（约 0.5 GB），单次通信延迟为 0.56 ms，计算过程为 0.5 GB / 900 GB/s

## Corrected Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，通信开销为每生成 1 token 传输一次激活值（约 0.5 GB），单次通信延迟为 0.56 ms，计算过程为 0.5 GB / 900 GB/s

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 NVLink带宽为900GB/s，0.5GB数据量除以900GB/s确实等于约0.56ms，计算过程与数值量级均合理。
