# N357: PagedAttention 的 block_size 决定了 KV Cache 的物理页粒度；当 seq_len=32768 时，block_size=16 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

PagedAttention 的 block_size 决定了 KV Cache 的物理页粒度；当 seq_len=32768 时，block_size=16 导致每层每头分配 2048 个物理块，而 block_size=32 导致 1024 个物理块；块数量直接影响 vLLM 内部 BlockTable 的索引查找开销和显存碎片率。

## Corrected Claim

PagedAttention 的 block_size 决定了 KV Cache 的物理页粒度；当 seq_len=32768 时，block_size=16 导致每层每头分配 2048 个物理块，而 block_size=32 导致 1024 个物理块；块数量直接影响 vLLM 内部 BlockTable 的索引查找开销和显存碎片率。

## Evidence

先验知识/题面给定，逻辑校验通过：32768/16=2048，32768/32=1024，数学计算正确；PagedAttention机制中block_size确实决定物理页粒度及BlockTable规模，符合vLLM设计原理。
