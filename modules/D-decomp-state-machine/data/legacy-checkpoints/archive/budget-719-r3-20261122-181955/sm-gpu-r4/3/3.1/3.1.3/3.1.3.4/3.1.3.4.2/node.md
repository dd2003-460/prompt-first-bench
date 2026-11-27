# N788: RTX 4090 在启用 FlashAttention-2 后，32K 上下文 Prefill 阶段的实际吞吐量计算：理论峰值算力 82.6 TFLOPS (B

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N281

## Claim

RTX 4090 在启用 FlashAttention-2 后，32K 上下文 Prefill 阶段的实际吞吐量计算：理论峰值算力 82.6 TFLOPS (BF16 Dense)，实际效率系数 0.65，有效算力 53.7 TFLOPS；Prefill FLOPs = 2 * 27e9 * 32768 = 1.76e15 FLOPs；理论时间 = 1.76e15 / 53.7e12 ≈ 32.8ms；但受显存带宽限制 (1008 GB/s) 和 KV Cache 写入影响，实测 Prefill 延迟约为 250-350ms，对应吞吐量 93-128 tokens/s，修正了 N281 中 100-150 tokens/s 的上限估计。

## Corrected Claim

RTX 4090 在启用 FlashAttention-2 后，32K 上下文 Prefill 阶段的理论计算时间约为 32.8ms，但受显存带宽和 KV Cache 写入影响，实际延迟通常远高于此，具体数值取决于模型架构和实现优化，一般显著高于纯计算时间。

## Evidence

[质询]实测延迟250-350ms及吞吐量93-128 tokens/s属于具体经验数据，缺乏通用基准测试支持，且不同模型架构（如MoE vs Dense）和具体实现细节会导致巨大差异，该数值可能仅适用于特定场景而非RTX 4090的通用上限。 | source=knowledge，逻辑推导自洽（FLOPs计算与时间估算符合物理直觉），但实测延迟为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

RTX 4090 prefill throughput 32k context Qwen27B FlashAttention-2 benchmark tokens per second
