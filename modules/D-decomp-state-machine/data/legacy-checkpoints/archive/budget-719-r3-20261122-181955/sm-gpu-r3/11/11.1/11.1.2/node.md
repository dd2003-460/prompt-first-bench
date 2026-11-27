# N373: PagedAttention的内存效率修正：PagedAttention将KV Cache分为固定大小block（通常16-32 tokens/block），减

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N126

## Claim

PagedAttention的内存效率修正：PagedAttention将KV Cache分为固定大小block（通常16-32 tokens/block），减少内存碎片浪费约5-15%。在8.5GB显存下，若block_size=16 tokens，实际可用KV Cache容量 = 8.5GB / (1 + 0.1) ≈ 7.73GB，可支持 7.73GB / 256KB ≈ 30,900 tokens，仍略低于32K需求，需启用INT8 KV Cache（256KB→128KB/token）或减少batch size至1。

## Corrected Claim

PagedAttention的内存效率修正：PagedAttention将KV Cache分为固定大小block（通常16-32 tokens/block），减少内存碎片浪费约5-15%。在8.5GB显存下，若block_size=16 tokens，实际可用KV Cache容量 = 8.5GB / (1 + 0.1) ≈ 7.73GB，可支持 7.73GB / 256KB ≈ 30,900 tokens，仍略低于32K需求，需启用INT8 KV Cache（256KB→128KB/token）或减少batch size至1。

## Search Query

PagedAttention memory overhead block size vLLM
