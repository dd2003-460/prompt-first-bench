# N271: 决策时间增量 Δt_decision 的计算公式：Δt_decision = t_base * (1 + λ_load * ΔCognitive_Load)，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N73

## Claim

决策时间增量 Δt_decision 的计算公式：Δt_decision = t_base * (1 + λ_load * ΔCognitive_Load)，其中 t_base 为基准决策时间，λ_load 为认知负荷敏感度系数，需通过 A/B 测试中不同数据密度组的响应时间差校准。

## Corrected Claim

决策时间增量 Δt_decision 的计算公式：Δt_decision = t_base * (1 + λ_load * ΔCognitive_Load)，其中 t_base 为基准决策时间，λ_load 为认知负荷敏感度系数，需通过 A/B 测试中不同数据密度组的响应时间差校准。

## Evidence

先验知识/题面给定，逻辑校验通过
