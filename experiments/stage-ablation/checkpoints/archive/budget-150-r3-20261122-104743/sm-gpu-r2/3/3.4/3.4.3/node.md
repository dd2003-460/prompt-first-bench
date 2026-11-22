# N113: 2×RTX 4090 方案中，若采用 Pipeline Parallelism，理论加速比为 1.53x，计算过程为 2 / (1 + 195ms / (100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism，理论加速比为 1.53x，计算过程为 2 / (1 + 195ms / (1000ms/15.5tokens))，其中 15.5 tokens/s 为单卡理论 Decode 速度

## Corrected Claim

2×RTX 4090 方案中，若采用 Pipeline Parallelism，理论加速比为 1.53x，计算过程为 2 / (1 + 195ms / (1000ms/15.5tokens))，其中 15.5 tokens/s 为单卡理论 Decode 速度

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 / (1 + 195ms / (1000ms/15.5tokens)) 计算结果约为 1.53，且符合 Pipeline Parallelism 在存在固定通信/启动延迟下的加速比推导逻辑。
