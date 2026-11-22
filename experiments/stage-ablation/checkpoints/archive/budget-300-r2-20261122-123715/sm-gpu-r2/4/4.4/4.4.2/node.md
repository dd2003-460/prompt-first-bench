# N95: 条件分支表-分支2：Budget_B > $5000 且 Latency_SLA < 50ms/token (即 >20 tok/s) 且 Quality_Se

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

条件分支表-分支2：Budget_B > $5000 且 Latency_SLA < 50ms/token (即 >20 tok/s) 且 Quality_Sensitivity=Medium → 推荐 1x L40S (48GB) + FP8；其单卡高带宽 (864 GB/s) 与 48GB 显存确保 32K 上下文下无 Offload，吞吐稳定在 30-40 tok/s，TCO ≈ $8000 + $3000 (电力) = $11000，性价比优于 2x 4090 的维护风险。

## Corrected Claim

条件分支表-分支2：Budget_B > $5000 且 Latency_SLA < 50ms/token (即 >20 tok/s) 且 Quality_Sensitivity=Medium → 推荐 1x L40S (48GB) + FP8；其单卡高带宽 (864 GB/s) 与 48GB 显存确保 32K 上下文下无 Offload，吞吐稳定在 30-40 tok/s，TCO ≈ $8000 + $3000 (电力) = $11000，性价比优于 2x 4090 的维护风险。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S 48GB显存足以容纳32K上下文模型权重及KV Cache，864GB/s带宽支持高吞吐，TCO计算逻辑自洽。
