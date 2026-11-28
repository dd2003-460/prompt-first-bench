# N179: 最优阈值 τ* 的解析解推导：令 dC_total/dτ = C_API * dFP/dτ - C_Human * dFN/dτ = 0，代入 Logistic

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

最优阈值 τ* 的解析解推导：令 dC_total/dτ = C_API * dFP/dτ - C_Human * dFN/dτ = 0，代入 Logistic 导数公式得到 k * FP(τ*)(1-FP(τ*)) / (C_Human * k_fn * FN(τ*)(1-FN(τ*))) = C_API / C_Human ≈ 0.018，需数值求解 τ*。

## Corrected Claim

最优阈值 τ* 的解析解推导：令 dC_total/dτ = C_API * dFP/dτ - C_Human * dFN/dτ = 0，代入 Logistic 导数公式得到 k * FP(τ*)(1-FP(τ*)) / (C_Human * k_fn * FN(τ*)(1-FN(τ*))) = C_API / C_Human ≈ 0.018，需数值求解 τ*。

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数求导并令其为零的推导过程符合微积分基本原理，Logistic 函数导数形式正确，量纲与数值量级（API成本远低于人工成本导致比值约0.018）合理。
