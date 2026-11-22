# N118: 2×H100 SXM5 方案中，若采用 Tensor Parallelism，实际 Decode 吞吐量为 102.4 tokens/s，计算过程为 51.7 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，实际 Decode 吞吐量为 102.4 tokens/s，计算过程为 51.7 tokens/s × 1.98

## Corrected Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，实际 Decode 吞吐量为 102.4 tokens/s，计算过程为 51.7 tokens/s × 1.98

## Evidence

先验知识/题面给定，逻辑校验通过：51.7 × 1.98 = 102.366，四舍五入为 102.4，数值计算准确且符合 Tensor Parallelism 近线性加速的工程直觉。
