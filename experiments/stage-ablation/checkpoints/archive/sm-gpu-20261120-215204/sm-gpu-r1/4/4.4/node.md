# N25: 在32K上下文窗口下，KV Cache内存占用随序列长度线性增长，计算公式为 2 × 层数 × 头数 × 头维度 × 序列长度 × 精度字节数；对于Qwen3-

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在32K上下文窗口下，KV Cache内存占用随序列长度线性增长，计算公式为 2 × 层数 × 头数 × 头维度 × 序列长度 × 精度字节数；对于Qwen3-27B（64层，40头，128维），BF16下32K序列的KV Cache约为40GB，这意味着总显存需求=权重内存+KV Cache+激活值缓冲。

## Corrected Claim

在32K上下文窗口下，KV Cache内存占用随序列长度线性增长，计算公式为 2 × 层数 × 头数 × 头维度 × 序列长度 × 精度字节数；对于Qwen3-27B（64层，40头，128维），BF16下32K序列的KV Cache约为40GB，这意味着总显存需求=权重内存+KV Cache+激活值缓冲。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（2×64×40×128×32768×2 bytes ≈ 42.9 GB，与40GB量级一致），符合Transformer架构基本原理。
