# N203: Qwen3-27B 在 FP8/INT8 精度下的总显存需求修正计算：Memory_Weights (25.14 GiB) + Memory_KV (4.0 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Qwen3-27B 在 FP8/INT8 精度下的总显存需求修正计算：Memory_Weights (25.14 GiB) + Memory_KV (4.0 GiB) + Overhead (3.26 GiB) = 32.4 GiB。加上 15% 安全余量：32.4 * 1.15 ≈ 37.26 GiB (≈ 40.0 GB)。此结果与 N66 中的 35.6 GB 接近，但需基于修正后的 KV Cache 值进行最终确认。

## Corrected Claim

Qwen3-27B 在 FP8/INT8 精度下的总显存需求修正计算：Memory_Weights (25.14 GiB) + Memory_KV (4.0 GiB) + Overhead (3.26 GiB) = 32.4 GiB。加上 15% 安全余量：32.4 * 1.15 ≈ 37.26 GiB (≈ 40.0 GB)。此结果与 N66 中的 35.6 GB 接近，但需基于修正后的 KV Cache 值进行最终确认。

## Evidence

先验知识/题面给定，逻辑校验通过：25.14 + 4.0 + 3.26 = 32.4 GiB，32.4 * 1.15 = 37.26 GiB，换算为 GB 约 40.0 GB，计算自洽且量级合理。
