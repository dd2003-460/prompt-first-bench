# N19: 量化不确定性传播规则：当最终性价比结论依赖多个带不确定性的参数时，采用蒙特卡洛模拟（N≥1000次）或解析误差传播公式 Δf = Σ(∂f/∂xi * Δxi)

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

量化不确定性传播规则：当最终性价比结论依赖多个带不确定性的参数时，采用蒙特卡洛模拟（N≥1000次）或解析误差传播公式 Δf = Σ(∂f/∂xi * Δxi) 计算最终结论的置信区间；若关键参数（如GPU价格）波动>10%，必须单独列出该参数对排名翻转的敏感度阈值

## Corrected Claim

量化不确定性传播规则：当最终性价比结论依赖多个带不确定性的参数时，采用蒙特卡洛模拟（N≥1000次）或解析误差传播公式 Δf = Σ(∂f/∂xi * Δxi) 计算最终结论的置信区间；若关键参数（如GPU价格）波动>10%，必须单独列出该参数对排名翻转的敏感度阈值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

sensitivity analysis cost performance ranking GPU uncertainty
