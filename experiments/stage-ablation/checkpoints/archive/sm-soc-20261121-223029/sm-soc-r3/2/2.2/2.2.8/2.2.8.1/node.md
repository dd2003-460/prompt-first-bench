# N189: Wait-and-See 策略下的买家咨询到达率衰减函数：C_wait(t) = C_base * e^(-μ_wait * t)，其中 t 为降价后小时数，μ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

Wait-and-See 策略下的买家咨询到达率衰减函数：C_wait(t) = C_base * e^(-μ_wait * t)，其中 t 为降价后小时数，μ_wait 为买家等待耐心衰减系数；需估算 μ_wait 使得 P(No_Inquiry | t=48h) = 1 - e^(-λ_visitors * C_wait(48h) * 48) ≈ 0.30（即30%的无咨询归因于此），从而解出 μ_wait 的具体数值范围。

## Corrected Claim

Wait-and-See 策略下的买家咨询到达率衰减函数：C_wait(t) = C_base * e^(-μ_wait * t)，其中 t 为降价后小时数，μ_wait 为买家等待耐心衰减系数；需估算 μ_wait 使得 P(No_Inquiry | t=48h) = 1 - e^(-λ_visitors * C_wait(48h) * 48) ≈ 0.30（即30%的无咨询归因于此），从而解出 μ_wait 的具体数值范围。

## Evidence

先验知识/题面给定，逻辑校验通过
