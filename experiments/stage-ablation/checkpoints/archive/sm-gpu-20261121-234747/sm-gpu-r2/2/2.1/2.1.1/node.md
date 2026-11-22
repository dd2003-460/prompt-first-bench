# N57: Qwen3-27B在BF16精度下，KV Cache每token占用量为2 * num_layers * num_kv_heads * head_dim * 2

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

Qwen3-27B在BF16精度下，KV Cache每token占用量为2 * num_layers * num_kv_heads * head_dim * 2 bytes，需基于config.json中具体参数计算

## Corrected Claim

Qwen3-27B在BF16精度下，KV Cache每token占用量为2 * num_layers * num_kv_heads * head_dim * 2 bytes，需基于config.json中具体参数计算

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Transformer KV cache size formula bytes per token
