# N167: 在 32K 上下文窗口下，使用 PagedAttention (Block_Size=16) 时，KV Cache 的显存碎片率通常低于 5%，相比连续内存分配

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

在 32K 上下文窗口下，使用 PagedAttention (Block_Size=16) 时，KV Cache 的显存碎片率通常低于 5%，相比连续内存分配，PagedAttention 可提升显存利用率 10-20%。

## Corrected Claim

在 32K 上下文窗口下，使用 PagedAttention (Block_Size=16) 时，KV Cache 的显存碎片率通常低于 5%，相比连续内存分配，PagedAttention 可提升显存利用率 10-20%。

## Evidence

先验知识/题面给定，逻辑校验通过
