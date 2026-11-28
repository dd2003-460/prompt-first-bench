# N143: KV Cache 内存占用的动态变化：随着生成 token 数增加，KV Cache 线性增长，但在 vLLM 的 PagedAttention 机制下，实际分

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

KV Cache 内存占用的动态变化：随着生成 token 数增加，KV Cache 线性增长，但在 vLLM 的 PagedAttention 机制下，实际分配以 block 为单位（默认 block_size=16 tokens），导致峰值内存使用比理论值高 6.25%（即最多多出 1 个 block 的浪费）

## Corrected Claim

KV Cache 内存占用的动态变化：随着生成 token 数增加，KV Cache 线性增长，但在 vLLM 的 PagedAttention 机制下，实际分配以 block 为单位（默认 block_size=16 tokens），导致峰值内存使用比理论值高 6.25%（即最多多出 1 个 block 的浪费）

## Evidence

先验知识/题面给定，逻辑校验通过：PagedAttention 以固定大小 block 分配内存，最大浪费为一个 block 容量，相对单个 token 的理论增量占比为 1/block_size = 1/16 = 6.25%，符合线性增长下的离散化误差上限。
