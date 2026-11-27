# N46: BF16 精度下总显存需求：Weights (55.6 GB) + KV Cache (4 GB) + Activation (1.5 GB) + Overhe

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

BF16 精度下总显存需求：Weights (55.6 GB) + KV Cache (4 GB) + Activation (1.5 GB) + Overhead (0.75 GB) ≈ 61.85 GB，向上取整需 64 GB 显存卡

## Corrected Claim

BF16 精度下总显存需求：Weights (55.6 GB) + KV Cache (4 GB) + Activation (1.5 GB) + Overhead (0.75 GB) ≈ 61.85 GB，向上取整需 64 GB 显存卡

## Evidence

先验知识/题面给定，逻辑校验通过：55.6+4+1.5+0.75=61.85，且61.85GB向上取整至常见显存规格64GB符合工程惯例。
