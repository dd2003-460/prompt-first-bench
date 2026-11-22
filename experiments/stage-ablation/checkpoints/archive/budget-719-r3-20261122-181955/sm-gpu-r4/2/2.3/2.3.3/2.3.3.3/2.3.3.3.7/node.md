# N707: 若假设 n_kv_heads=16 (错误假设) 的 32K 上下文单请求 KV Cache 值为：2 * 64 * 16 * 128 * 32768 * 2 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

若假设 n_kv_heads=16 (错误假设) 的 32K 上下文单请求 KV Cache 值为：2 * 64 * 16 * 128 * 32768 * 2 bytes = 17,179,869,184 bytes = 16.0 GB。此值用于敏感性分析，但根据 N370 已证伪，实际值应为 8.0 GB。

## Corrected Claim

若假设 n_kv_heads=16 (错误假设) 的 32K 上下文单请求 KV Cache 值为：2 * 64 * 16 * 128 * 32768 * 2 bytes = 17,179,869,184 bytes = 16.0 GB。此值用于敏感性分析，但根据 N370 已证伪，实际值应为 8.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 16 * 128 * 32768 * 2 = 17,179,869,184 bytes，换算为 GB (10^9) 约为 17.18 GB，若按 GiB (2^30) 换算则约为 16.0 GiB，数值量级与逻辑自洽，且明确标注为错误假设下的敏感性分析值。
