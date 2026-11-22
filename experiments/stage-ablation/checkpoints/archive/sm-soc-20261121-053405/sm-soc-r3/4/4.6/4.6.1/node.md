# N75: Q_loss_ratio 的估计误差传播公式：ΔR 的相对置信区间宽度 W_R 近似等于 P_consult 的相对标准差 σ_rel 乘以敏感度系数 S，其中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N23, N24, N25

## Claim

Q_loss_ratio 的估计误差传播公式：ΔR 的相对置信区间宽度 W_R 近似等于 P_consult 的相对标准差 σ_rel 乘以敏感度系数 S，其中 S = |∂ln(ΔR)/∂ln(P_consult)|。在基准模型中 S ≈ 1.0，因此 W_R ≈ σ_rel。

## Corrected Claim

Q_loss_ratio 的估计误差传播公式：ΔR 的相对置信区间宽度 W_R 近似等于 P_consult 的相对标准差 σ_rel 乘以敏感度系数 S，其中 S = |∂ln(ΔR)/∂ln(P_consult)|。在基准模型中 S ≈ 1.0，因此 W_R ≈ σ_rel。

## Evidence

先验知识/题面给定，逻辑校验通过：敏感度系数定义符合对数导数标准，基准模型下S≈1.0导致误差直接传递，量纲与逻辑自洽。

## Search Query

error propagation formula sensitivity coefficient economic impact assessment
