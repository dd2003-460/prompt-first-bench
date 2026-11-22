# N438: Qwen3-27B 在 32K 上下文下 FP8 KV Cache 的精确大小：KV_Size = 2 * 64 * 8 * 128 * 32768 * 1 (

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N182

## Claim

Qwen3-27B 在 32K 上下文下 FP8 KV Cache 的精确大小：KV_Size = 2 * 64 * 8 * 128 * 32768 * 1 (byte) = 8,589,934,592 bytes ≈ 8.0 GiB (8.59 GB)。

## Corrected Claim

Qwen3-27B 在 32K 上下文下 FP8 KV Cache 的精确大小：KV_Size = 2 * 64 * 8 * 128 * 32768 * 1 (byte) = 8,589,934,592 bytes ≈ 8.0 GiB (8.59 GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，8 KV头，128维）符合主流大模型设计，计算过程 2*64*8*128*32768*1 = 8,589,934,592 bytes 数学正确，且 8,589,934,592 / 1024^3 = 8.0 GiB 换算准确。

## Search Query

Qwen3-27B KV cache size 32k fp8 calculation
