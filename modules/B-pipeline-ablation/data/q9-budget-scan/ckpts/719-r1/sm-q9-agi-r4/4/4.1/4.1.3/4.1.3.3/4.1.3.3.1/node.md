# N584: 配对样本设计在本地推理优化评估中，效应量 δ 的估计公式为 δ = mean(Y_after - Y_before)，其标准误 SE_paired = std(

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N208

## Claim

配对样本设计在本地推理优化评估中，效应量 δ 的估计公式为 δ = mean(Y_after - Y_before)，其标准误 SE_paired = std(Y_after - Y_before)/sqrt(n)，相比独立样本设计 SE_indep = sqrt(σ^2/n + σ^2/n)，在 σ_paired=0.2σ 时，SE_paired/SE_indep = 0.2/sqrt(2) ≈ 0.141，即精度提升约7倍。

## Corrected Claim

配对样本设计在本地推理优化评估中，效应量 δ 的估计公式为 δ = mean(Y_after - Y_before)，其标准误 SE_paired = std(Y_after - Y_before)/sqrt(n)，相比独立样本设计 SE_indep = sqrt(σ^2/n + σ^2/n)，在 σ_paired=0.2σ 时，SE_paired/SE_indep = 0.2/sqrt(2) ≈ 0.141，即精度提升约7倍。

## Evidence

先验知识/题面给定，逻辑校验通过：配对设计标准误公式及独立样本标准误公式符合统计学定义，代入 σ_paired=0.2σ 计算比值 0.2/√2 ≈ 0.141，倒数约为 7.07，结论准确。
