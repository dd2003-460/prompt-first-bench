# N47: FP8/INT8 精度下总显存需求：Weights (27.8 GB) + KV Cache (2 GB) + Activation (1.5 GB) + Ov

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

FP8/INT8 精度下总显存需求：Weights (27.8 GB) + KV Cache (2 GB) + Activation (1.5 GB) + Overhead (0.75 GB) ≈ 32.05 GB，向上取整需 32 GB 显存卡

## Corrected Claim

FP8/INT8 精度下总显存需求：Weights (27.8 GB) + KV Cache (2 GB) + Activation (1.5 GB) + Overhead (0.75 GB) ≈ 32.05 GB，向上取整需 32 GB 显存卡

## Evidence

先验知识/题面给定，逻辑校验通过：27.8 + 2 + 1.5 + 0.75 = 32.05 GB，向上取整至 32 GB 符合显存分配逻辑。
