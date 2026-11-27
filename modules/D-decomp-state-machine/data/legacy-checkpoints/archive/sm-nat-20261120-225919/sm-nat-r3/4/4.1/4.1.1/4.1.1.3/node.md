# N176: 针对子问 (c) 的‘打几折’，具体折损因子 D_update = e^(-λ * T_res)，若假设最热对象访问频率足以使 T_res ≈ 10 天（即平均

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

针对子问 (c) 的‘打几折’，具体折损因子 D_update = e^(-λ * T_res)，若假设最热对象访问频率足以使 T_res ≈ 10 天（即平均 10 天访问一次），则 D_update = e^(-0.1) ≈ 0.905，即命中率需打 90.5 折；若 T_res = 1 天，则 D_update ≈ 0.990，仅打 99 折。

## Corrected Claim

针对子问 (c) 的‘打几折’，具体折损因子 D_update = e^(-λ * T_res)，若假设最热对象访问频率足以使 T_res ≈ 10 天（即平均 10 天访问一次），则 D_update = e^(-0.1) ≈ 0.905，即命中率需打 90.5 折；若 T_res = 1 天，则 D_update ≈ 0.990，仅打 99 折。

## Evidence

先验知识/题面给定，逻辑校验通过：指数函数计算 e^(-0.1)≈0.9048 和 e^(-0.1*1)≈0.9900 数值准确，逻辑自洽。
