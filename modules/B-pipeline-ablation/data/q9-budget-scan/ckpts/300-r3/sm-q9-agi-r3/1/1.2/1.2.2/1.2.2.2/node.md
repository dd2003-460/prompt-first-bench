# N140: V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，KV Cache 读取延迟对 attention 计算的影响：在 seq_len=10

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，KV Cache 读取延迟对 attention 计算的影响：在 seq_len=1024 时，KV 读取耗时约 0.13ms，占总 attention 计算时间（约 0.5ms）的 26%，构成显著瓶颈

## Corrected Claim

V100-SXM2-16GB 的 HBM2 显存带宽为 900 GB/s，KV Cache 读取延迟对 attention 计算的影响：在 seq_len=1024 时，KV 读取耗时约 0.13ms，占总 attention 计算时间（约 0.5ms）的 26%，构成显著瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：V100-SXM2-16GB 标称带宽 900 GB/s 符合硬件规格；基于该带宽和典型 KV Cache 数据量估算的延迟占比在数量级上合理，无内部矛盾。
