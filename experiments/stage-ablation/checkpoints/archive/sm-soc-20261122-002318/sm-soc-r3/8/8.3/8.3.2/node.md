# N267: 后悔成本对长期留存率 (Churn) 的传导机制：ΔChurn = η * P(Regret) * U_regret_normalized。其中 P(Regre

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

后悔成本对长期留存率 (Churn) 的传导机制：ΔChurn = η * P(Regret) * U_regret_normalized。其中 P(Regret) 为买家在 T_days 内发现更低价的概率。在 FOMO 驱动下，买家快速决策导致搜索空间未穷尽，P(Regret) 显著高于理性搜索者。若 P(Regret) 从 10% 升至 30%，且 η (后悔敏感度) 为 0.05，则 ΔChurn 增加 1%。需量化 FOMO 场景下 P(Regret) 的具体提升幅度。

## Corrected Claim

后悔成本对长期留存率 (Churn) 的传导机制：ΔChurn = η * P(Regret) * U_regret_normalized。其中 P(Regret) 为买家在 T_days 内发现更低价的概率。在 FOMO 驱动下，买家快速决策导致搜索空间未穷尽，P(Regret) 显著高于理性搜索者。若 P(Regret) 从 10% 升至 30%，且 η (后悔敏感度) 为 0.05，则 ΔChurn 增加 1%。需量化 FOMO 场景下 P(Regret) 的具体提升幅度。

## Evidence

先验知识/题面给定，逻辑校验通过
