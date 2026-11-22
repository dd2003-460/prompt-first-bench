# N129: 预期信誉价值损失 V_reputation_loss 的分解计算：V_reputation_loss = ∑_{t=1}^{T_penalty} δ^t × (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

预期信誉价值损失 V_reputation_loss 的分解计算：V_reputation_loss = ∑_{t=1}^{T_penalty} δ^t × (λ_base - λ_punished_t) × p_conv × R_short，其中 T_penalty 为风控持续期，λ_punished_t 为受罚期间的预期咨询率，R_short 为单笔边际收益。

## Corrected Claim

预期信誉价值损失 V_reputation_loss 的分解计算：V_reputation_loss = ∑_{t=1}^{T_penalty} δ^t × (λ_base - λ_punished_t) × p_conv × R_short，其中 T_penalty 为风控持续期，λ_punished_t 为受罚期间的预期咨询率，R_short 为单笔边际收益。

## Evidence

先验知识/题面给定，逻辑校验通过
