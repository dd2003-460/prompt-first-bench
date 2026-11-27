# N57: FlashAttention 2/3 不存储完整的 attention matrix (Q*K^T)，仅存储 softmax 输出和 V 的乘积，因此激活内存中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

FlashAttention 2/3 不存储完整的 attention matrix (Q*K^T)，仅存储 softmax 输出和 V 的乘积，因此激活内存中不包含 O(seq_len^2) 项，但 KV Cache 本身仍需完整存储 K 和 V 向量

## Corrected Claim

FlashAttention 2/3 不存储完整的 attention matrix (Q*K^T)，仅存储 softmax 输出和 V 的乘积，因此激活内存中不包含 O(seq_len^2) 项，但 KV Cache 本身仍需完整存储 K 和 V 向量

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 核心机制即为 IO 感知优化，通过分块计算避免显式存储 O(N^2) 的 Attention Matrix，仅保留输出；而 KV Cache 作为自回归推理的必要状态，必须完整存储历史 K/V 向量，二者逻辑自洽且符合技术事实。

## Search Query

FlashAttention memory footprint KV cache vs attention matrix storage
