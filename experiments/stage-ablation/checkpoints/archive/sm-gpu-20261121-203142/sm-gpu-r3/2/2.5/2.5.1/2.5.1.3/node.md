# N203: 若 Acceptance_Score < 1.0 的补偿策略量化：每降低 0.1 分需增加多少硬件成本或降低多少吞吐量才能维持整体 TCO 不变，例如 ΔTCO

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N63

## Claim

若 Acceptance_Score < 1.0 的补偿策略量化：每降低 0.1 分需增加多少硬件成本或降低多少吞吐量才能维持整体 TCO 不变，例如 ΔTCO_compensation = (1 - Score) * Baseline_Cost_per_token * 1.2 [待核验]

## Corrected Claim

若 Acceptance_Score < 1.0，需通过增加硬件成本或降低吞吐量来补偿TCO，具体补偿量取决于系统架构与负载特性，通常可建模为与(1 - Score)成正比的函数，但具体系数需根据实际基准测试确定。

## Evidence

[质询]该公式将复杂的TCO补偿简化为线性关系，且系数1.2缺乏理论或实证依据，属于经验性估算而非严格推导。 | 先验知识/题面给定，逻辑校验通过，但具体系数1.2及线性假设缺乏来源支持，属经验事实。
