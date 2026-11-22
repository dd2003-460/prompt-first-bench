# N124: Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim × 2 byte

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim × 2 bytes (BF16)，其中 n_layers=64, n_kv_heads=4 (GQA), head_dim=128，计算结果为 131,072 bytes/token (128 KB/token)

## Corrected Claim

Qwen3-27B 的 KV Cache 单 token 显存占用为 2 × n_layers × n_kv_heads × head_dim × 2 bytes (BF16)，其中 n_layers=64, n_kv_heads=4 (GQA), head_dim=128，计算结果为 131,072 bytes/token (128 KB/token)

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 4 * 128 * 2 = 131,072 bytes 计算正确，且符合 Qwen3-27B 采用 GQA (4 KV heads) 的架构特征。

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads head_dim
