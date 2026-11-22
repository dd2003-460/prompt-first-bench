# N50: 咨询到达率衰减模型：降价后的咨询到达率 λ_consult_after 与降价前 λ_consult_before 的关系为 λ_consult_after =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N12

## Claim

咨询到达率衰减模型：降价后的咨询到达率 λ_consult_after 与降价前 λ_consult_before 的关系为 λ_consult_after = λ_consult_before * exp(-β * S_neg)，其中 β 为衰减系数，需通过 60% 无咨询率（即 P(0 consults in 48h) = 0.6）反推 β 的具体数值。

## Corrected Claim

咨询到达率衰减模型：降价后的咨询到达率 λ_consult_after 与降价前 λ_consult_before 的关系为 λ_consult_after = λ_consult_before * exp(-β * S_neg)，其中 β 为衰减系数，需通过 60% 无咨询率（即 P(0 consults in 48h) = 0.6）反推 β 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布性质 P(0)=exp(-λ) 与指数衰减模型结合，逻辑自洽且量纲合理。
