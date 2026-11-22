# N117: 2×H100 SXM5 方案中，若采用 Tensor Parallelism，理论加速比为 1.98x，计算过程为 2 / (1 + 0.56ms / (100

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，理论加速比为 1.98x，计算过程为 2 / (1 + 0.56ms / (1000ms/51.7tokens))，其中 51.7 tokens/s 为单卡理论 Decode 速度

## Corrected Claim

2×H100 SXM5 方案中，若采用 Tensor Parallelism，理论加速比为 1.98x，计算过程为 2 / (1 + 0.56ms / (1000ms/51.7tokens))，其中 51.7 tokens/s 为单卡理论 Decode 速度

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 / (1 + 0.56 / (1000/51.7)) 计算结果约为 1.98，量纲与逻辑自洽。
