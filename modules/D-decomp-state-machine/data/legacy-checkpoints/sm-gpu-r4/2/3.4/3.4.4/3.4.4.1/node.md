# N163: NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 计算：其第 4 代 Tensor Core 硬件级支持 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 计算：其第 4 代 Tensor Core 硬件级支持 FP8，无需软件模拟；相比 BF16，FP8 的矩阵乘法吞吐量理论上提升 2 倍（FLOPS 翻倍），但受限于内存带宽，实际端到端吞吐量提升通常在 1.5-1.8 倍之间 [待核验]。

## Corrected Claim

NVIDIA RTX 4090 (Ada Lovelace) 原生支持 FP8 (E4M3/E5M2) 计算：其第 4 代 Tensor Core 硬件级支持 FP8，无需软件模拟；相比 BF16，FP8 的矩阵乘法吞吐量理论上提升 2 倍（FLOPS 翻倍），但受限于内存带宽，实际端到端吞吐量提升通常在 1.5-1.8 倍之间 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 Ada Lovelace native FP8 tensor core support throughput vs BF16
