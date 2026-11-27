# N319: 演化假设在强逐利行为下的置信度修正公式：C_evo_corrected = C_evo_base * (1 - γ * I_profit)，其中 I_profi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N112, N113

## Claim

演化假设在强逐利行为下的置信度修正公式：C_evo_corrected = C_evo_base * (1 - γ * I_profit)，其中 I_profit 为逐利行为强度指数（定义为卖家主动降价频率与历史平均降价频率的比值），γ 为交互衰减系数，需通过 A/B 测试中控制 I_profit 变量后的 C_evo 变化率回归估计。

## Corrected Claim

演化假设在强逐利行为下的置信度修正公式：C_evo_corrected = C_evo_base * (1 - γ * I_profit)，其中 I_profit 为逐利行为强度指数（定义为卖家主动降价频率与历史平均降价频率的比值），γ 为交互衰减系数，需通过 A/B 测试中控制 I_profit 变量后的 C_evo 变化率回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

behavioral economics interaction effect evolutionary heuristic profit seeking confidence correction formula
