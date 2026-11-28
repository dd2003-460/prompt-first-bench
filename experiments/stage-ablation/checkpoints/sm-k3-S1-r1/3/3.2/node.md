# N22: KV Cache管理采用PagedAttention算法，将KV Cache分割为固定大小的块（默认16 tokens/block），减少内存碎片，内存利用率从

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

KV Cache管理采用PagedAttention算法，将KV Cache分割为固定大小的块（默认16 tokens/block），减少内存碎片，内存利用率从传统的50-60%提升至90%以上，支持更长的上下文而不OOM。

## Corrected Claim

KV Cache管理采用PagedAttention算法，将KV Cache分割为固定大小的块（默认16 tokens/block），减少内存碎片，内存利用率从传统的50-60%提升至90%以上，支持更长的上下文而不OOM。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM PagedAttention memory efficiency
