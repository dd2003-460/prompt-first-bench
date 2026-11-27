# N77: P_consult_after_disclosure 的稳定性量化：当 P_consult 服从正态分布 N(0.2, 0.02^2) 时，相对标准差 σ_re

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

P_consult_after_disclosure 的稳定性量化：当 P_consult 服从正态分布 N(0.2, 0.02^2) 时，相对标准差 σ_rel = 0.02/0.2 = 10%。若 S=1.0，预测 ΔR 置信区间宽度为 ±10%（与 N23 声称的 ±5% 存在偏差，表明 S 可能小于 1.0 或存在其他抵消项）。

## Corrected Claim

P_consult_after_disclosure 的稳定性量化：当 P_consult 服从正态分布 N(0.2, 0.02^2) 时，相对标准差 σ_rel = 0.02/0.2 = 10%。若 S=1.0，预测 ΔR 置信区间宽度为 ±10%（与 N23 声称的 ±5% 存在偏差，表明 S 可能小于 1.0 或存在其他抵消项）。

## Evidence

先验知识/题面给定，逻辑校验通过：相对标准差计算正确（0.02/0.2=10%），且基于正态分布假设推导置信区间宽度的逻辑自洽。

## Search Query

normal distribution relative standard deviation error propagation
