# N135: Batch Size=B 时，KV Cache 总显存占用公式 = 2 (K+V) * num_kv_heads * head_dim * seq_len * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

Batch Size=B 时，KV Cache 总显存占用公式 = 2 (K+V) * num_kv_heads * head_dim * seq_len * B * bytes_per_element，需代入 Qwen3-27B 的 num_kv_heads (GQA 配置，如 8) 和 head_dim (128) 计算 B=4 和 B=8 时的具体 GB 值

## Corrected Claim

Batch Size=B 时，KV Cache 总显存占用公式 = 2 (K+V) * num_kv_heads * head_dim * seq_len * B * bytes_per_element，需代入 Qwen3-27B 的 num_kv_heads (GQA 配置，如 8) 和 head_dim (128) 计算 B=4 和 B=8 时的具体 GB 值

## Evidence

先验知识/题面给定，逻辑校验通过
