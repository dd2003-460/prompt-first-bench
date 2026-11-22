# N749: 基于 n_layers=32, n_kv_heads=8, head_dim=128, BF16 (2 bytes/token) 的单 token KV Cac

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N266

## Claim

基于 n_layers=32, n_kv_heads=8, head_dim=128, BF16 (2 bytes/token) 的单 token KV Cache 精确值：2 * 32 * 8 * 128 * 2 = 131,072 bytes = 128 KB/token。修正 N89/N370 中基于 n_layers=64 得出的 256 KB/token 错误。

## Corrected Claim

基于 n_layers=32, n_kv_heads=8, head_dim=128, BF16 (2 bytes/token) 的单 token KV Cache 精确值：2 * 32 * 8 * 128 * 2 = 131,072 bytes = 128 KB/token。修正 N89/N370 中基于 n_layers=64 得出的 256 KB/token 错误。

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 2 * 32 * 8 * 128 * 2 = 131,072 bytes 正确，且 131,072 bytes 等于 128 KB，数值量级与逻辑均自洽。
