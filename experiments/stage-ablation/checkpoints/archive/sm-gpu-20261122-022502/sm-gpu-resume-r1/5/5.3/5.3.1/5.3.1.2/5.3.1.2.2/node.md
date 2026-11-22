# N878: KV Cache 显存计算公式推导：Memory_KV = 2 (K,V) * L * N_kv * D * S * B_kv / 1e9 GB。其中 S=32

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276, N277, N278

## Claim

KV Cache 显存计算公式推导：Memory_KV = 2 (K,V) * L * N_kv * D * S * B_kv / 1e9 GB。其中 S=32768 (32K context), B_kv 为 KV 缓存精度字节数。此公式是 N276 中 2.0133 GB 结果的唯一来源，需验证 L, N_kv, D, S 的具体取值是否准确。

## Corrected Claim

KV Cache 显存计算公式推导：Memory_KV = 2 (K,V) * L * N_kv * D * S * B_kv / 1e9 GB。其中 S=32768 (32K context), B_kv 为 KV 缓存精度字节数。此公式是 N276 中 2.0133 GB 结果的唯一来源，需验证 L, N_kv, D, S 的具体取值是否准确。

## Evidence

先验知识/题面给定，逻辑校验通过
