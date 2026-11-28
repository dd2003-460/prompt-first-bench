# N9: KV Cache 显存占用公式为 KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * dty

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

KV Cache 显存占用公式为 KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * dtype_size，其中 Qwen3-27B 需确认 n_layers (约64), n_kv_heads (GQA/MQA 结构，需查具体值), head_dim 等参数

## Corrected Claim

KV Cache 显存占用公式为 KV_Bytes = 2 * n_layers * n_kv_heads * head_dim * seq_len * dtype_size，其中 Qwen3-27B 需确认 n_layers (约64), n_kv_heads (GQA/MQA 结构，需查具体值), head_dim 等参数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B model config n_layers n_kv_heads head_dim
