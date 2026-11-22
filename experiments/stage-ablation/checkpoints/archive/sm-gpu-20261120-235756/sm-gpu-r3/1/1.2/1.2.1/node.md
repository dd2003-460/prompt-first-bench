# N39: Qwen3-27B 的 KV Cache 每 token 显存占用公式为 2 × n_layers × n_kv_heads × head_dim × dtyp

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式为 2 × n_layers × n_kv_heads × head_dim × dtype_size，代入已确认参数（n_layers=64, n_kv_heads=8, head_dim=128, dtype_size=2 bytes for BF16）计算得每 token 占用为 262,144 bytes (256 KB)，该值直接决定 32K 上下文下的总 KV Cache 峰值显存。

## Corrected Claim

Qwen3-27B 的 KV Cache 每 token 显存占用公式为 2 × n_layers × n_kv_heads × head_dim × dtype_size，代入已确认参数（n_layers=64, n_kv_heads=8, head_dim=128, dtype_size=2 bytes for BF16）计算得每 token 占用为 262,144 bytes (256 KB)，该值直接决定 32K 上下文下的总 KV Cache 峰值显存。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 × 64 × 8 × 128 × 2 = 262,144 bytes 计算正确，量纲与数值量级合理。
