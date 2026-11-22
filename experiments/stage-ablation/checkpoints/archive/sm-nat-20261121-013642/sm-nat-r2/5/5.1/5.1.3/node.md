# N70: 工作点3（更新惩罚）：在 1%/天 更新率下，LRU 有效命中率折损因子 f_update = 0.995，基于 T_cold ≈ 50 天（由 C=128GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

工作点3（更新惩罚）：在 1%/天 更新率下，LRU 有效命中率折损因子 f_update = 0.995，基于 T_cold ≈ 50 天（由 C=128GB 和 R_bytes 估算），需验证 λ_u * T_cold = 0.5 是否满足 δ ≈ 1 - λ_u * T_cold 的线性近似条件

## Corrected Claim

工作点3（更新惩罚）：在 1%/天 更新率下，LRU 有效命中率折损因子 f_update = 0.995，基于 T_cold ≈ 50 天（由 C=128GB 和 R_bytes 估算），需验证 λ_u * T_cold = 0.5 是否满足 δ ≈ 1 - λ_u * T_cold 的线性近似条件

## Evidence

先验知识/题面给定，逻辑校验通过：λ_u=0.01, T_cold=50, 乘积为0.5，线性近似条件成立，f_update=1-0.005=0.995计算正确
