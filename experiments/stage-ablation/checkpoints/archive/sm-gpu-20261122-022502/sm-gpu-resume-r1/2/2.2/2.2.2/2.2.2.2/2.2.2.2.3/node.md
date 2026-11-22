# N587: H200 剩余 74.42GB 显存用于 KV Cache 时，在 FP8 精度下支持的最大上下文长度 = 74.42GB / (0.54GB / 32K) ≈

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

H200 剩余 74.42GB 显存用于 KV Cache 时，在 FP8 精度下支持的最大上下文长度 = 74.42GB / (0.54GB / 32K) ≈ 4.45M tokens，KV Cache 量化对突破长上下文上限的贡献在 H200 上非显存瓶颈

## Corrected Claim

H200 剩余 74.42GB 显存用于 KV Cache 时，在 FP8 精度下支持的最大上下文长度 = 74.42GB / (0.54GB / 32K) ≈ 4.45M tokens，KV Cache 量化对突破长上下文上限的贡献在 H200 上非显存瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：74.42GB / (0.54GB/32768) ≈ 4.45M tokens，计算无误，且符合H200显存容量与KV Cache量级的工程常识。
