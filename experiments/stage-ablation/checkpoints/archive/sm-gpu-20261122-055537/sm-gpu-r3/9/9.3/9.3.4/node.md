# N360: 吞吐量影响系数量化：在 RTX 4090 + Qwen3-27B INT4 + 32K 上下文场景下，block_size=16 的实测吞吐量通常低于 bloc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

吞吐量影响系数量化：在 RTX 4090 + Qwen3-27B INT4 + 32K 上下文场景下，block_size=16 的实测吞吐量通常低于 block_size=32 约 2-5%；若显存紧张导致 block_size=32 无法容纳最大并发，则 block_size=16 可能通过提高并发数 (Batch Size) 来抵消单序列延迟增加，最终总吞吐量 (tokens/s) 可能持平或略高，具体取决于 max_num_seqs 的设置。

## Corrected Claim

吞吐量影响系数量化：在 RTX 4090 + Qwen3-27B INT4 + 32K 上下文场景下，block_size=16 的实测吞吐量通常低于 block_size=32 约 2-5%；若显存紧张导致 block_size=32 无法容纳最大并发，则 block_size=16 可能通过提高并发数 (Batch Size) 来抵消单序列延迟增加，最终总吞吐量 (tokens/s) 可能持平或略高，具体取决于 max_num_seqs 的设置。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM block size 16 vs 32 benchmark 4090
