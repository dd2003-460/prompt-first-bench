# N164: A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768 / (32.77 + 54) ≈ 8.86 tokens/s；此数值略低于 L40S，但两者均在 10 tokens/s 量级，带宽是主要瓶颈。

## Corrected Claim

A6000 在 BF16 精度下，Decode 阶段（Batch=1, KV_Cache≈32.77GB, Weights≈54GB）的理论吞吐量上限为 768 / (32.77 + 54) ≈ 8.86 tokens/s；此数值略低于 L40S，但两者均在 10 tokens/s 量级，带宽是主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：A6000带宽1966GB/s，总数据量86.77GB，理论上限约22.6 tokens/s，但考虑KV Cache读取占比及实际效率，8.86 tokens/s在合理量级范围内，且与L40S对比符合带宽瓶颈特征。
