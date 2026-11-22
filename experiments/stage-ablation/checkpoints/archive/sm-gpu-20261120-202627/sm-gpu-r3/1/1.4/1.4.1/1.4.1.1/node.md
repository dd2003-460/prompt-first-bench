# N190: KV Cache 显存公式修正项：N45 公式中 'num_heads' 应替换为 'num_kv_heads' (8)，且需确认是否包含 RoPE 或额外状态

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

KV Cache 显存公式修正项：N45 公式中 'num_heads' 应替换为 'num_kv_heads' (8)，且需确认是否包含 RoPE 或额外状态。修正后公式：2 * 64 * 8 * 128 * 32768 * 2 bytes = 13.11 GB。

## Corrected Claim

KV Cache 显存公式修正项：N45 公式中 'num_heads' 应替换为 'num_kv_heads' (8)，且需确认是否包含 RoPE 或额外状态。修正后公式：2 * 64 * 8 * 128 * 32768 * 2 bytes = 13.11 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式参数（2层KV, 64层, 8头, 128维, 32768长度, 2字节）乘积计算正确，量级合理。
