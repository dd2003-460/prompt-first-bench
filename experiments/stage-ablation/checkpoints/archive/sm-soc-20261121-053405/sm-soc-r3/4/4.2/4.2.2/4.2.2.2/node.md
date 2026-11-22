# N182: E_ratio 的置信区间宽度与样本量关系：E_ratio 的95%置信区间宽度为 2 × 1.96 × (σ_exposure / √n) / μ_expos

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N67

## Claim

E_ratio 的置信区间宽度与样本量关系：E_ratio 的95%置信区间宽度为 2 × 1.96 × (σ_exposure / √n) / μ_exposure，其中 σ_exposure 为曝光量标准差，n 为实验组样本量。若要求置信区间不包含 1.0（即显著大于1.5），最小样本量 n_min 需满足 n > (1.96 σ_exposure / (μ_exposure × (1.5-1.0)))^2，当前缺乏 n 和 σ_exposure 的具体数值，标记为[待核验]。

## Corrected Claim

E_ratio 的置信区间宽度与样本量关系：E_ratio 的95%置信区间宽度为 2 × 1.96 × (σ_exposure / √n) / μ_exposure，其中 σ_exposure 为曝光量标准差，n 为实验组样本量。若要求置信区间不包含 1.0（即显著大于1.5），最小样本量 n_min 需满足 n > (1.96 σ_exposure / (μ_exposure × (1.5-1.0)))^2，当前缺乏 n 和 σ_exposure 的具体数值，标记为[待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合正态分布置信区间标准定义，量纲与逻辑自洽。
