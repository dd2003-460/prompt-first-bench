# N138: Qwen3-27B 每 token 的 KV Cache 显存占用计算：kv_per_token = 2 (K+V) * num_layers * num_kv

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

Qwen3-27B 每 token 的 KV Cache 显存占用计算：kv_per_token = 2 (K+V) * num_layers * num_kv_heads * head_dim * bytes_per_token。若 L=32, KV_heads=8, head_dim=128, BF16 (2 bytes)，则 kv_per_token = 2 * 32 * 8 * 128 * 2 = 131,072 bytes ≈ 128 KB/token。

## Corrected Claim

Qwen3-27B 每 token 的 KV Cache 显存占用计算：kv_per_token = 2 (K+V) * num_layers * num_kv_heads * head_dim * bytes_per_token。若 L=32, KV_heads=8, head_dim=128, BF16 (2 bytes)，则 kv_per_token = 2 * 32 * 8 * 128 * 2 = 131,072 bytes ≈ 128 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V，其余参数相乘），数值计算 2*32*8*128*2 = 131,072 无误，单位换算 131,072 bytes = 128 KB 正确。

## Search Query

Qwen3-27B architecture num_layers num_kv_heads head_dim
