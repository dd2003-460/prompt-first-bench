# N557: 基于 N372 确认的参数（n_kv_heads=8, layers=64, head_dim=128），修正 N89/N358 中基于 n_kv_heads=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N194

## Claim

基于 N372 确认的参数（n_kv_heads=8, layers=64, head_dim=128），修正 N89/N358 中基于 n_kv_heads=32 的错误计算：BF16 32K 上下文单请求 KV Cache 总占用 = 256 KB/token * 32768 tokens = 8 GB，而非 N89 计算的 32.77 GB 或 N358 计算的 64 GB。

## Corrected Claim

基于 N372 确认的参数（n_kv_heads=8, layers=64, head_dim=128），修正 N89/N358 中基于 n_kv_heads=32 的错误计算：BF16 32K 上下文单请求 KV Cache 总占用 = 256 KB/token * 32768 tokens = 8 GB，而非 N89 计算的 32.77 GB 或 N358 计算的 64 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小 = 2 (K/V) * 64 (layers) * 8 (kv_heads) * 128 (head_dim) * 2 (bytes) * 32768 (tokens) = 8,589,934,592 bytes = 8 GB。计算无误。
