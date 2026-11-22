# N751: 基于 n_layers=32, n_kv_heads=8, head_dim=128, FP8 (1 byte/token) 的单 token KV Cache

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N267

## Claim

基于 n_layers=32, n_kv_heads=8, head_dim=128, FP8 (1 byte/token) 的单 token KV Cache 精确值：2 * 32 * 8 * 128 * 1 = 65,536 bytes = 64 KB/token。修正 N89 中基于错误层数得出的 16.38 GB 总量错误。

## Corrected Claim

基于 n_layers=32, n_kv_heads=8, head_dim=128, FP8 (1 byte/token) 的单 token KV Cache 精确值：2 * 32 * 8 * 128 * 1 = 65,536 bytes = 64 KB/token。修正 N89 中基于错误层数得出的 16.38 GB 总量错误。

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 2 * 32 * 8 * 128 * 1 = 65,536 bytes 正确，且 65,536 bytes 等于 64 KB，数值量级与逻辑自洽。
