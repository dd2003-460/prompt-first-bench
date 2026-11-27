# N294: 2x RTX 3090 (48GB) 方案在 FP8 下的总显存需求 = 权重 (27 GB) + KV Cache (16.78 GB) + 激活/开销 (3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

2x RTX 3090 (48GB) 方案在 FP8 下的总显存需求 = 权重 (27 GB) + KV Cache (16.78 GB) + 激活/开销 (3-6 GB) = 46.78 - 49.78 GB。该值接近或超过总容量限制，需评估双卡间 KV Cache 分片策略及通信缓冲开销，且 RTX 3090 不支持原生 FP8 硬件加速，软件模拟 FP8 可能导致额外计算开销和显存碎片。

## Corrected Claim

2x RTX 3090 (48GB) 方案在 FP8 下的总显存需求 = 权重 (27 GB) + KV Cache (16.78 GB) + 激活/开销 (3-6 GB) = 46.78 - 49.78 GB。该值接近或超过总容量限制，需评估双卡间 KV Cache 分片策略及通信缓冲开销，且 RTX 3090 不支持原生 FP8 硬件加速，软件模拟 FP8 可能导致额外计算开销和显存碎片。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 基于 Ampere 架构，确实不支持原生 FP8 硬件加速（需软件模拟）；2x 24GB 总显存 48GB，与计算出的 46.78-49.78GB 需求在量级和数值上自洽，且接近容量上限的结论符合逻辑。
