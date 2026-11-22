# N773: 基于 N370 修正后的 Qwen3-27B 参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），KV_Ca

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276

## Claim

基于 N370 修正后的 Qwen3-27B 参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），KV_Cache_Size_per_token = 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes = 256 KB，该值取代 N276 中 n_kv_heads=8 时 64 KB 的错误计算（原计算误用 n_layers=16）。

## Corrected Claim

基于 N370 修正后的 Qwen3-27B 参数（n_kv_heads=8, num_layers=64, head_dim=128, BF16），KV_Cache_Size_per_token = 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes = 256 KB，该值取代 N276 中 n_kv_heads=8 时 64 KB 的错误计算（原计算误用 n_layers=16）。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 计算公式 2 * n_layers * n_kv_heads * head_dim * dtype_size 代入数值 2 * 64 * 8 * 128 * 2 = 262,144 bytes (256 KB) 计算正确，且符合 Qwen3-27B 的架构参数常识。
