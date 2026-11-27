# N356: FlashAttention-2/3 对 RTX 4090 长上下文 Decode 阶段吞吐量的提升有限：FlashAttention 主要优化 Prefill

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

FlashAttention-2/3 对 RTX 4090 长上下文 Decode 阶段吞吐量的提升有限：FlashAttention 主要优化 Prefill 阶段的 O(N^2) 计算，而在 Decode 阶段 (Batch=1)，注意力计算量仅为 O(N)，且已受限于 KV Cache 读取带宽，启用 FlashAttention 对 Decode 速度提升通常 < 5% [待核验]

## Corrected Claim

FlashAttention-2/3 对 RTX 4090 长上下文 Decode 阶段吞吐量的提升有限：FlashAttention 主要优化 Prefill 阶段的 O(N^2) 计算，而在 Decode 阶段 (Batch=1)，注意力计算量仅为 O(N)，且已受限于 KV Cache 读取带宽，启用 FlashAttention 对 Decode 速度提升通常 < 5% [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 核心优化在于减少 HBM 读写次数（IO-aware），主要收益在 Prefill 的大矩阵乘法；Decode 阶段 Batch=1 时计算量低且受限于 KV Cache 读取带宽（Memory-bound），FlashAttention 的优化空间极小，符合硬件与算法原理。

## Search Query

FlashAttention decode phase speedup single sequence long context
