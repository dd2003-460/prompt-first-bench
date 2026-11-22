# N114: 2×RTX 4090 方案中，若采用 Pipeline Parallelism，实际 Decode 吞吐量为 23.7 tokens/s，计算过程为 15.5 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism，实际 Decode 吞吐量为 23.7 tokens/s，计算过程为 15.5 tokens/s × 1.53

## Corrected Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism，实际 Decode 吞吐量为 23.7 tokens/s，计算过程为 15.5 tokens/s × 1.53

## Evidence

先验知识/题面给定，逻辑校验通过：15.5 × 1.53 = 23.715，四舍五入为 23.7，数值计算准确且量级合理。
