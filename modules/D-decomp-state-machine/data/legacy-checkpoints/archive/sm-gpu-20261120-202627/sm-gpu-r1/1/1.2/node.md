# N8: 32K 上下文下 KV Cache 显存占用计算公式：2 * num_layers * hidden_dim * num_heads * seq_len * b

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文下 KV Cache 显存占用计算公式：2 * num_layers * hidden_dim * num_heads * seq_len * bytes_per_element，需代入 Qwen3-27B 具体架构参数（如 64 层、4096 hidden 等）进行计算

## Corrected Claim

32K 上下文下 KV Cache 显存占用计算公式：2 * num_layers * hidden_dim * num_heads * seq_len * bytes_per_element，需代入 Qwen3-27B 具体架构参数（如 64 层、4096 hidden 等）进行计算

## Evidence

先验知识/题面给定，逻辑校验通过
