# N63: 单 Token KV Cache 内存增量计算：基于 N39 的参数 (假设 n_layers=32, n_kv_heads=8, head_dim=128, 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

单 Token KV Cache 内存增量计算：基于 N39 的参数 (假设 n_layers=32, n_kv_heads=8, head_dim=128, bytes_per_token=1 for FP8/INT8 或 2 for FP16)，单 token KV 占用 = 2 (K+V) * 32 * 8 * 128 * bytes。若 bytes=1 (FP8)，则单 token ≈ 65,536 Bytes = 64 KB。若 bytes=2 (FP16)，则单 token ≈ 128 KB。

## Corrected Claim

单 Token KV Cache 内存增量计算：基于 N39 的参数 (假设 n_layers=32, n_kv_heads=8, head_dim=128, bytes_per_token=1 for FP8/INT8 或 2 for FP16)，单 token KV 占用 = 2 (K+V) * 32 * 8 * 128 * bytes。若 bytes=1 (FP8)，则单 token ≈ 65,536 Bytes = 64 KB。若 bytes=2 (FP16)，则单 token ≈ 128 KB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算公式 2 * 32 * 8 * 128 * 1 = 65536 Bytes (64KB) 及 2 * 32 * 8 * 128 * 2 = 131072 Bytes (128KB) 算术正确，符合 Transformer KV Cache 标准结构定义。
