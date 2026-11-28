# N208: 对于配对样本设计（如同一模型在优化前后的性能对比），由于消除了个体差异，等效标准差 σ_paired 通常远小于独立样本的总体标准差 σ，若 σ_paired 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

对于配对样本设计（如同一模型在优化前后的性能对比），由于消除了个体差异，等效标准差 σ_paired 通常远小于独立样本的总体标准差 σ，若 σ_paired = 0.2 * σ，则检测相同效应量 δ 所需的样本量仅为独立样本设计的 1/25（因为 n ∝ σ^2），即 n_paired ≈ n_independent / 25。

## Corrected Claim

对于配对样本设计（如同一模型在优化前后的性能对比），由于消除了个体差异，等效标准差 σ_paired 通常远小于独立样本的总体标准差 σ，若 σ_paired = 0.2 * σ，则检测相同效应量 δ 所需的样本量仅为独立样本设计的 1/25（因为 n ∝ σ^2），即 n_paired ≈ n_independent / 25。

## Evidence

先验知识/题面给定，逻辑校验通过：根据样本量公式 n ∝ σ²，若 σ_paired = 0.2σ，则 n_paired/n_independent = (0.2)² = 0.04 = 1/25，推导正确。
