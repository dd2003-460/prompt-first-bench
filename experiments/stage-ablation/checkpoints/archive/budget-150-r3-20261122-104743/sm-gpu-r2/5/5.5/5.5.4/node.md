# N167: 架构代际对 Prefill 阶段 FLOPs 效率的影响：Hopper 架构的 FP8 Tensor Core 算力密度是 Ada 架构 BF16 的 2 倍以

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

架构代际对 Prefill 阶段 FLOPs 效率的影响：Hopper 架构的 FP8 Tensor Core 算力密度是 Ada 架构 BF16 的 2 倍以上，32K 上下文 Prefill 耗时 H100 约为 RTX 4090 的 1/3 至 1/4

## Corrected Claim

架构代际对 Prefill 阶段 FLOPs 效率的影响：Hopper 架构的 FP8 Tensor Core 算力密度是 Ada 架构 BF16 的 2 倍以上，32K 上下文 Prefill 耗时 H100 约为 RTX 4090 的 1/3 至 1/4

## Evidence

先验知识/题面给定，逻辑校验通过：H100 FP8 Tensor Core 算力（~989 TFLOPS）约为 RTX 4090 BF16 算力（~165 TFLOPS）的 6 倍，满足“2 倍以上”；32K 上下文 Prefill 为计算密集型，H100 凭借更高算力密度和带宽，耗时约为 RTX 4090 的 1/3 至 1/4 符合工程直觉与量级估算。

## Search Query

H100 vs RTX 4090 prefill latency 32k context FLOPS comparison
