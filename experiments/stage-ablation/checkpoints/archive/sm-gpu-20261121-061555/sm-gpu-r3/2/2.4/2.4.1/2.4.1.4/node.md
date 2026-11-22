# N199: Qwen3-27B 在 BF16 精度下的总显存需求修正计算：Memory_Weights (50.29 GiB) + Memory_KV (8.0 GiB) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Qwen3-27B 在 BF16 精度下的总显存需求修正计算：Memory_Weights (50.29 GiB) + Memory_KV (8.0 GiB) + Overhead (3.5 GB ≈ 3.26 GiB) = 61.55 GiB。加上 15% 安全余量：61.55 * 1.15 ≈ 70.78 GiB (≈ 76.0 GB)。此结果远高于 N65 中的 67.1 GB，表明原估算中 KV Cache 部分严重低估。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的总显存需求修正计算：Memory_Weights (50.29 GiB) + Memory_KV (8.0 GiB) + Overhead (3.5 GB ≈ 3.26 GiB) = 61.55 GiB。加上 15% 安全余量：61.55 * 1.15 ≈ 70.78 GiB (≈ 76.0 GB)。此结果远高于 N65 中的 67.1 GB，表明原估算中 KV Cache 部分严重低估。

## Evidence

先验知识/题面给定，逻辑校验通过：50.29 + 8.0 + 3.26 = 61.55 GiB，61.55 * 1.15 = 70.7825 GiB，70.7825 * 1.0737 ≈ 76.0 GB，计算无误且量级合理。
