# N160: KV Cache 显存占用公式：KV_Mem = 2 × n_layers × n_kv_heads × head_dim × S_ctx × D_bytes，

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

KV Cache 显存占用公式：KV_Mem = 2 × n_layers × n_kv_heads × head_dim × S_ctx × D_bytes，代入 S_ctx=32768 计算得出具体 GB 值

## Corrected Claim

KV Cache 显存占用公式：KV_Mem = 2 × n_layers × n_kv_heads × head_dim × S_ctx × D_bytes，代入 S_ctx=32768 计算得出具体 GB 值

## Evidence

先验知识/题面给定，逻辑校验通过
