# N358: 显存碎片率 (Fragmentation Rate) 与 block_size 的关系：在 seq_len=32K 且 batch_size=1 时，block

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

显存碎片率 (Fragmentation Rate) 与 block_size 的关系：在 seq_len=32K 且 batch_size=1 时，block_size=16 的尾部浪费（Tail Waste）约为 0 到 15 tokens 的 KV 空间，而 block_size=32 的尾部浪费约为 0 到 31 tokens；对于 24GB 显存的 4090，若 KV Cache 占用接近显存上限，block_size=32 可能因无法分配最后一个块而触发 OOM 或强制减小 max_num_seqs，从而降低有效吞吐量。

## Corrected Claim

显存碎片率 (Fragmentation Rate) 与 block_size 的关系：在 seq_len=32K 且 batch_size=1 时，block_size=16 的尾部浪费（Tail Waste）约为 0 到 15 tokens 的 KV 空间，而 block_size=32 的尾部浪费约为 0 到 31 tokens；对于 24GB 显存的 4090，若 KV Cache 占用接近显存上限，block_size=32 可能因无法分配最后一个块而触发 OOM 或强制减小 max_num_seqs，从而降低有效吞吐量。

## Evidence

先验知识/题面给定，逻辑校验通过：block_size 决定分配粒度，尾部浪费上限为 block_size-1，32K 序列下 32 的粒度确实比 16 更容易因剩余空间不足导致分配失败或 OOM。
