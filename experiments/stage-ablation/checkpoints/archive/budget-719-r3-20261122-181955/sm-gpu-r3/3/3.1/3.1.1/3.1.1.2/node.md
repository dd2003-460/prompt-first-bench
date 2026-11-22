# N266: 基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 2 bytes = 4.295 GB，修正 N89 原估算 32.77 GB 的错误。

## Corrected Claim

基于修正参数 (n_layers=32, n_kv_heads=8) 的 32K BF16 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 2 bytes = 4.295 GB，修正 N89 原估算 32.77 GB 的错误。

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 32 * 8 * 128 * 32768 * 2 = 4,294,967,296 bytes，即 4 GiB (4.295 GB)，数学推导正确且量级合理。
