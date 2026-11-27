# N89: 字节命中率分母 D_byte = Σ_{j=1}^{N} R_j * S_j。由于 R 和 S 负相关，分母不能拆解为 (ΣR_j)*(ΣS_j)，必须通过联合

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

字节命中率分母 D_byte = Σ_{j=1}^{N} R_j * S_j。由于 R 和 S 负相关，分母不能拆解为 (ΣR_j)*(ΣS_j)，必须通过联合分布积分 ∫ r*s * f(r,s) dr ds 计算。

## Corrected Claim

字节命中率分母 D_byte = Σ_{j=1}^{N} R_j * S_j。由于 R 和 S 负相关，分母不能拆解为 (ΣR_j)*(ΣS_j)，必须通过联合分布积分 ∫ r*s * f(r,s) dr ds 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率定义为命中字节数除以总请求字节数，分母为总字节数即 Σ(R_j * S_j)；由于 R 和 S 负相关，E[RS] ≠ E[R]E[S]，故不能拆解为乘积，需通过联合分布积分计算，逻辑自洽且符合概率论基本性质。
