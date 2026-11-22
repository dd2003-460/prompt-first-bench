# N359: M3 Ultra (192GB) 在 BF16 精度下的最大并发请求数（Batch Size）计算：可用显存 = 192GB - 54GB (Weights) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

M3 Ultra (192GB) 在 BF16 精度下的最大并发请求数（Batch Size）计算：可用显存 = 192GB - 54GB (Weights) - 3GB (Overhead) = 135GB；Max_Batch = 135GB / 32GB (KV per req) = 4.2，即最大支持 4 个并发 32K 请求；若启用 FP8 KV Cache，KV 减半为 16GB/req，Max_Batch = 135/16 = 8.4，即最大 8 个并发。

## Corrected Claim

M3 Ultra (192GB) 在 BF16 精度下的最大并发请求数（Batch Size）计算：可用显存 = 192GB - 54GB (Weights) - 3GB (Overhead) = 135GB；Max_Batch = 135GB / 32GB (KV per req) = 4.2，即最大支持 4 个并发 32K 请求；若启用 FP8 KV Cache，KV 减半为 16GB/req，Max_Batch = 135/16 = 8.4，即最大 8 个并发。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（192-54-3=135, 135/32=4.21, 135/16=8.43）及取整逻辑（向下取整以符合并发限制）均正确，符合LLM推理显存估算的基本原理。
