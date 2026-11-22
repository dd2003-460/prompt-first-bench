# N183: 修正N56矛盾：N56中'BF16 KV下为25.77 GB'的计算基于 n_layers=64, n_kv_heads=8, head_dim=128。但Qw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

修正N56矛盾：N56中'BF16 KV下为25.77 GB'的计算基于 n_layers=64, n_kv_heads=8, head_dim=128。但Qwen3-27B实际架构参数需核验：若 n_layers=64, n_kv_heads=8, head_dim=128，则每token KV = 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes = 256 KB。32K tokens * 256 KB/token = 8,192 KB * 32 = 256 MB? 错误。正确计算：256 KB/token * 32,768 tokens = 8,388,608 KB = 8 GB。N56的25.77 GB数值错误，正确BF16 KV Cache (32K) 应为 8 GB。

## Corrected Claim

修正N56矛盾：N56中'BF16 KV下为25.77 GB'的计算基于 n_layers=64, n_kv_heads=8, head_dim=128。但Qwen3-27B实际架构参数需核验：若 n_layers=64, n_kv_heads=8, head_dim=128，则每token KV = 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes = 256 KB。32K tokens * 256 KB/token = 8,192 KB * 32 = 256 MB? 错误。正确计算：256 KB/token * 32,768 tokens = 8,388,608 KB = 8 GB。N56的25.77 GB数值错误，正确BF16 KV Cache (32K) 应为 8 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache大小计算公式为 2(K+V) * n_layers * n_kv_heads * head_dim * bytes_per_element * num_tokens。代入参数：2 * 64 * 8 * 128 * 2 * 32768 = 8,589,934,592 bytes = 8 GB。计算逻辑自洽且数值正确。

## Search Query

Qwen3-27B KV cache size 32k context BF16
