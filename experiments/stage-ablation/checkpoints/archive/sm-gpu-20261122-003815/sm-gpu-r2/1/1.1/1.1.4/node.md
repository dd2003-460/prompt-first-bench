# N47: RTX 3090 (24GB) 与 RTX 4090 在 LLM 推理上的性能差异：显存带宽 936 GB/s vs 1008 GB/s (差 7.1%)，但 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

RTX 3090 (24GB) 与 RTX 4090 在 LLM 推理上的性能差异：显存带宽 936 GB/s vs 1008 GB/s (差 7.1%)，但 RTX 3090 无 FP8 硬件支持，INT4 量化推理效率可能因缺乏 Tensor Core 优化而比 RTX 4090 低 10-20% [待核验]。

## Corrected Claim

RTX 3090 (24GB) 与 RTX 4090 在 LLM 推理上的性能差异：显存带宽 936 GB/s vs 1008 GB/s (差 7.1%)，但 RTX 3090 无 FP8 硬件支持，INT4 量化推理效率可能因缺乏 Tensor Core 优化而比 RTX 4090 低 10-20% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存带宽936GB/s与RTX 4090的1008GB/s符合硬件规格，且3090确实缺乏FP8硬件支持，INT4推理效率差异符合架构特性逻辑。

## Search Query

RTX 3090 vs 4090 LLM inference INT4 performance comparison
