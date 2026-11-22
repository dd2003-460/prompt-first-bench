# N134: RTX 4090 的显存带宽 1008 GB/s 是 Decode 阶段的主要瓶颈，在 INT4 量化（权重 13.5GB）且 KV Cache 占用 8.59

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

RTX 4090 的显存带宽 1008 GB/s 是 Decode 阶段的主要瓶颈，在 INT4 量化（权重 13.5GB）且 KV Cache 占用 8.59GB (N100) 时，理论 Decode 吞吐上限为 1008 / (13.5 + 8.59) ≈ 45.5 tokens/s，显著高于 BF16 下的 11.5 tokens/s (N91)，表明量化是提升 4090 长上下文推理性能的关键机制。

## Corrected Claim

RTX 4090 的显存带宽 1008 GB/s 是 Decode 阶段的主要瓶颈，在 INT4 量化（权重 13.5GB）且 KV Cache 占用 8.59GB (N100) 时，理论 Decode 吞吐上限为 1008 / (13.5 + 8.59) ≈ 45.5 tokens/s，显著高于 BF16 下的 11.5 tokens/s (N91)，表明量化是提升 4090 长上下文推理性能的关键机制。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 为已知硬件规格；Decode 阶段受显存带宽限制，吞吐量近似等于带宽除以每次生成 token 需读取的总数据量（权重+KV Cache）；计算 1008 / (13.5 + 8.59) ≈ 45.5 tokens/s 与 BF16 下 11.5 tokens/s 的对比符合量化减少数据读取量的物理直觉，数值量级合理且内部自洽。
