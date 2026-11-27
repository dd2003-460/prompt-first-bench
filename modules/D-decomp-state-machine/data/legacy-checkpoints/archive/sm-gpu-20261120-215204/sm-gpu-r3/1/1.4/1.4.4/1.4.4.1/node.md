# N180: RTX 4090 在 W4 精度下运行 Qwen3-27B 且上下文为 32K 时，KV Cache 显存占用计算：Qwen3-27B 采用 GQA (8 KV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

RTX 4090 在 W4 精度下运行 Qwen3-27B 且上下文为 32K 时，KV Cache 显存占用计算：Qwen3-27B 采用 GQA (8 KV Heads, Head Dim 128, 64 Layers)，BF16 KV Cache 大小 = 2 (K+V) * 64 Layers * 8 Heads * 128 Dim * 2 Bytes * 32768 Tokens ≈ 17.2 GB；若 KV 量化为 FP8 则减半为 8.6 GB。

## Corrected Claim

RTX 4090 在 W4 精度下运行 Qwen3-27B 且上下文为 32K 时，KV Cache 显存占用计算：Qwen3-27B 采用 GQA (8 KV Heads, Head Dim 128, 64 Layers)，BF16 KV Cache 大小 = 2 (K+V) * 64 Layers * 8 Heads * 128 Dim * 2 Bytes * 32768 Tokens ≈ 17.2 GB；若 KV 量化为 FP8 则减半为 8.6 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV Heads, 128 Dim）符合 GQA 设计，BF16 下 2*64*8*128*2*32768 = 17,179,869,184 Bytes ≈ 16.0 GiB (或 17.2 GB 十进制)，FP8 减半逻辑正确，数值量级合理。

## Search Query

Qwen3 27B GQA heads hidden dim architecture parameters
