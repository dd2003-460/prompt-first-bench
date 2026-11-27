# N708: BF16 精度下 Qwen3-27B 在 vLLM 框架的总内存需求 (n_kv_heads=8)：Weights (54 GB) + KV_Cache (8.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

BF16 精度下 Qwen3-27B 在 vLLM 框架的总内存需求 (n_kv_heads=8)：Weights (54 GB) + KV_Cache (8.0 GB) + Framework_Overhead (3 GB) + OS_Cuda_Reserve (1 GB) = 66.0 GB。此值修正了 N253 中基于 5.37 GB KV Cache 计算的 63.37 GB 错误。

## Corrected Claim

BF16 精度下 Qwen3-27B 在 vLLM 框架的总内存需求 (n_kv_heads=8)：Weights (54 GB) + KV_Cache (8.0 GB) + Framework_Overhead (3 GB) + OS_Cuda_Reserve (1 GB) = 66.0 GB。此值修正了 N253 中基于 5.37 GB KV Cache 计算的 63.37 GB 错误。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB；KV Cache 8GB与n_kv_heads=8及典型上下文长度匹配；总内存66GB量级合理，且内部算术自洽（54+8+3+1=66）。
