# N56: vLLM PagedAttention 机制下，KV Cache 实际占用 = 2 * n_layers * n_kv_heads * head_dim * b

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

vLLM PagedAttention 机制下，KV Cache 实际占用 = 2 * n_layers * n_kv_heads * head_dim * block_size * num_blocks * bytes_per_elem，其中 num_blocks = ceil(seq_len / block_size) + 1（预留一个 block 用于新 token），block_size 默认 16 tokens

## Corrected Claim

vLLM PagedAttention 机制下，KV Cache 实际占用 = 2 * n_layers * n_kv_heads * head_dim * block_size * num_blocks * bytes_per_elem，其中 num_blocks = ceil(seq_len / block_size) + 1（预留一个 block 用于新 token），block_size 默认 16 tokens

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM PagedAttention KV cache memory calculation block size overhead
