# N221: KV Cache 显存占用公式：Size = 2 * num_layers * num_kv_heads * head_dim * seq_len * byte

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

KV Cache 显存占用公式：Size = 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_elem。对于 Qwen3-27B (32 layers, 4 KV heads, 128 head_dim, 32K ctx)，BF16 下为 2.15 GB，INT8 下为 1.07 GB，W4 下为 0.54 GB。

## Corrected Claim

KV Cache 显存占用公式：Size = 2 * num_layers * num_kv_heads * head_dim * seq_len * bytes_per_elem。对于 Qwen3-27B (32 layers, 4 KV heads, 128 head_dim, 32K ctx)，BF16 下为 2.15 GB，INT8 下为 1.07 GB，W4 下为 0.54 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构正确（2代表K和V），数值计算准确（32*4*128*32768*2*2 bytes ≈ 2.15GB），符合Qwen3-27B的GQA架构参数及显存占用规律。
