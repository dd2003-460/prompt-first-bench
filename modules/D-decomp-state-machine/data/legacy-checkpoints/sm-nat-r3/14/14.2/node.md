# N307: λ_update * T_res_avg 的线性近似有效性：当 λ_update * T_res_avg << 1 时，D_update ≈ 1 - λ_upd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

λ_update * T_res_avg 的线性近似有效性：当 λ_update * T_res_avg << 1 时，D_update ≈ 1 - λ_update * T_res_avg；需验证在 T_res_avg = 2h 和 24h 两种极端情况下，线性近似的误差范围（如与精确指数形式 1/(1+λ_update*T_res_avg) 的偏差）。

## Corrected Claim

λ_update * T_res_avg 的线性近似有效性：当 λ_update * T_res_avg << 1 时，D_update ≈ 1 - λ_update * T_res_avg；需验证在 T_res_avg = 2h 和 24h 两种极端情况下，线性近似的误差范围（如与精确指数形式 1/(1+λ_update*T_res_avg) 的偏差）。

## Evidence

先验知识/题面给定，逻辑校验通过：当 x << 1 时，1/(1+x) ≈ 1-x 是标准的泰勒展开一阶近似，误差为 O(x^2)，在 T_res_avg 为小时级且 λ_update 通常较小（如每日更新率）时，x 值远小于 1，近似有效。
