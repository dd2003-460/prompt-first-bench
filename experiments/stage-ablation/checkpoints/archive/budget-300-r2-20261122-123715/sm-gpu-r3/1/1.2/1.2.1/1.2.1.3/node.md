# N149: A100 80GB SXM4 显存带宽为 2039 GB/s (HBM2e)，在 FP8 精度 (权重 27GB) 下，理论解码吞吐上限 ≈ 2039 / 27

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

A100 80GB SXM4 显存带宽为 2039 GB/s (HBM2e)，在 FP8 精度 (权重 27GB) 下，理论解码吞吐上限 ≈ 2039 / 27 ≈ 75.5 tokens/s，实际效率系数 0.8 下为 60.4 tokens/s，显著高于 L40S (GDDR6) 方案。

## Corrected Claim

A100 80GB SXM4 显存带宽为 2039 GB/s (HBM2e)，在 FP8 精度 (权重 27GB) 下，理论解码吞吐上限 ≈ 2039 / 27 ≈ 75.5 tokens/s，实际效率系数 0.8 下为 60.4 tokens/s，显著高于 L40S (GDDR6) 方案。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM4 显存带宽确为 2039 GB/s，2039/27≈75.5，75.5*0.8≈60.4，计算无误且符合硬件规格常识。
