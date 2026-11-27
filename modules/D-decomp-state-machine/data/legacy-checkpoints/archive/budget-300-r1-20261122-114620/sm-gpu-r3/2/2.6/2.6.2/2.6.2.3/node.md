# N261: Qwen3-27B 在 BF16 精度下，每生成 1 个 token 所需的 KV Cache 增量 N_kv_bytes_per_token 计算公式为 2 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Qwen3-27B 在 BF16 精度下，每生成 1 个 token 所需的 KV Cache 增量 N_kv_bytes_per_token 计算公式为 2 * num_layers * num_kv_heads * head_dim * 2 bytes，对于 Qwen3-27B (64 layers, 8 kv heads, 128 head dim)，该值为 2 * 64 * 8 * 128 * 2 = 262,144 bytes ≈ 0.25 MB/token。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，每生成 1 个 token 所需的 KV Cache 增量 N_kv_bytes_per_token 计算公式为 2 * num_layers * num_kv_heads * head_dim * 2 bytes，对于 Qwen3-27B (64 layers, 8 kv heads, 128 head dim)，该值为 2 * 64 * 8 * 128 * 2 = 262,144 bytes ≈ 0.25 MB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * num_layers * num_kv_heads * head_dim * bytes_per_element 符合 Transformer KV Cache 标准计算逻辑（2代表K和V，bytes_per_element=2对应BF16），数值计算 2*64*8*128*2 = 262,144 正确，量级合理。

## Search Query

Qwen3-27B KV cache size per token calculation
