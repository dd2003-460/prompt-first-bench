# N279: 2x RTX 4090 在 FP8 量化下的 KV Cache 显存占用计算：KV_Cache = 2 * 32K * 32 * 128 * 2 bytes =

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

2x RTX 4090 在 FP8 量化下的 KV Cache 显存占用计算：KV_Cache = 2 * 32K * 32 * 128 * 2 bytes = 512MB/层 * 64 层 = 32GB，但实际因注意力头压缩和量化优化，KV Cache 占用约为 16GB-20GB，需从 48GB 总显存中扣除

## Corrected Claim

2x RTX 4090 (总显存 48GB) 在 FP8 量化下，若 KV Cache 理论占用为 32GB，则单卡占用约 16GB，处于 24GB 单卡显存的可承受范围内（需预留其他开销），实际占用因优化可能略低，但需确认 FP8 在 4090 上的具体实现效率。

## Evidence

[质询]数值量级与硬件规格矛盾：RTX 4090 单卡显存为 24GB，2x 4090 总显存为 48GB，但陈述中称“需从 48GB 总显存中扣除”暗示这是单卡或某种特定配置下的限制，而 32GB 的 KV Cache 占用已接近单卡 24GB 显存上限，若为双卡并行，单卡 KV Cache 约为 16GB，这与“16GB-20GB”的总占用描述存在口径混淆（是单卡还是双卡总和？）。此外，RTX 4090 原生不支持 FP8 硬件加速（需软件模拟或特定驱动/框架支持，且效率较低），直接断言“FP8 量化下”可能忽略硬件兼容性限制。 | 先验知识/题面给定，逻辑校验通过，但存在硬件规格与数值口径的潜在混淆，降级为定性表述。

## Search Query

Qwen3-27B FP8 KV cache size 32k context
