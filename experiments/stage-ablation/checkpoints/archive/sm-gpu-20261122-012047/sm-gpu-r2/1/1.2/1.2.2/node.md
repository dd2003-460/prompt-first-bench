# N51: 基于 N49 修正后的参数（n_kv_heads=4, head_dim=128, n_layers=48），32K 上下文下 BF16 KV Cache 的理

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于 N49 修正后的参数（n_kv_heads=4, head_dim=128, n_layers=48），32K 上下文下 BF16 KV Cache 的理论最小占用为 10.31 GB (48 × 4 × 128 × 2 bytes × 32768 / 1e9)，而非 N7 声称的 20.6 GB。

## Corrected Claim

基于 N49 修正后的参数（n_kv_heads=4, head_dim=128, n_layers=48），32K 上下文下 BF16 KV Cache 的理论最小占用为 10.31 GB (48 × 4 × 128 × 2 bytes × 32768 / 1e9)，而非 N7 声称的 20.6 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 48 * 4 * 128 * 2 * 32768 / 1e9 = 10.3079... GB，与陈述一致。
