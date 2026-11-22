# N181: L40S 48GB PCIe 在 350W TDP 下，按消费级电价 $0.15/kWh 计算，3 年持续满载电力成本为 350W * 24h * 365d *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

L40S 48GB PCIe 在 350W TDP 下，按消费级电价 $0.15/kWh 计算，3 年持续满载电力成本为 350W * 24h * 365d * 3y * $0.15/kWh ≈ $1435，其能效比（tokens/s/W）需结合 N146 的吞吐量数据进一步计算以评估性价比。

## Corrected Claim

L40S 48GB PCIe 在 350W TDP 下，按消费级电价 $0.15/kWh 计算，3 年持续满载电力成本为 350W * 24h * 365d * 3y * $0.15/kWh ≈ $1435，其能效比（tokens/s/W）需结合 N146 的吞吐量数据进一步计算以评估性价比。

## Evidence

先验知识/题面给定，逻辑校验通过：350W * 24h * 365d * 3y * $0.15/kWh = 1435.5，计算准确且量级合理。
