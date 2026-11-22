# N370: NVIDIA L40S 的 TDP 为 350W，低于 RTX 5090 (575W) 和 H100 (700W)，在 24/7 运行场景下，其 3 年电力成本

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131

## Claim

NVIDIA L40S 的 TDP 为 350W，低于 RTX 5090 (575W) 和 H100 (700W)，在 24/7 运行场景下，其 3 年电力成本比 RTX 5090 低约 40%（假设电价 $0.15/kWh），该数值需代入 TCO 公式进行修正。

## Corrected Claim

NVIDIA L40S 的 TDP 为 350W，低于 RTX 5090 (575W) 和 H100 (700W)，在 24/7 运行场景下，其 3 年电力成本比 RTX 5090 低约 40%（假设电价 $0.15/kWh），该数值需代入 TCO 公式进行修正。

## Evidence

先验知识/题面给定，逻辑校验通过：L40S TDP 350W、RTX 5090 TDP 575W 符合公开规格；350/575 ≈ 0.608，即 L40S 功耗约为 RTX 5090 的 61%，成本降低约 39.2%，与“低约 40%”在合理误差范围内一致，逻辑自洽。
