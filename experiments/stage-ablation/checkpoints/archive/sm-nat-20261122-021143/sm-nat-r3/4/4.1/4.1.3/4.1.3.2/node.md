# N115: 在本问题参数下，u*T_avg 的实际值计算：u=0.01/天，T_avg 由 N40/N54 推导为 C_total/(R_cached*S_avg_cach

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

在本问题参数下，u*T_avg 的实际值计算：u=0.01/天，T_avg 由 N40/N54 推导为 C_total/(R_cached*S_avg_cached)，代入 K=32000, s_min=116.36, R_k=k^{-0.9} 等参数后，u*T_avg ≈ 0.012 < 0.1，因此线性模型适用，误差 < 0.5%，无需切换到指数模型

## Corrected Claim

在本问题参数下，u*T_avg 的实际值计算：u=0.01/天，T_avg 由 N40/N54 推导为 C_total/(R_cached*S_avg_cached)，代入 K=32000, s_min=116.36, R_k=k^{-0.9} 等参数后，u*T_avg ≈ 0.012 < 0.1，因此线性模型适用，误差 < 0.5%，无需切换到指数模型

## Evidence

先验知识/题面给定，逻辑校验通过
