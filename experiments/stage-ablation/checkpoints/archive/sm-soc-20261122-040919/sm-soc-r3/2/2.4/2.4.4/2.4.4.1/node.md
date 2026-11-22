# N235: 共享随机源：平台算法信号权重 w_signal 的估计方差 Var(ŵ_signal)。该方差由平台A/B测试的样本量 n_test 决定，Var(ŵ_si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

共享随机源：平台算法信号权重 w_signal 的估计方差 Var(ŵ_signal)。该方差由平台A/B测试的样本量 n_test 决定，Var(ŵ_signal) = σ²_w / n_test。其中 σ_w 为流量分配权重的波动标准差，通常假设 σ_w ≈ 0.1（基于算法迭代频率）。当 n_test < 500 时，Var(ŵ_signal) > 0.0002，导致后续偏导数估计不稳定。

## Corrected Claim

共享随机源：平台算法信号权重 w_signal 的估计方差 Var(ŵ_signal)。该方差由平台A/B测试的样本量 n_test 决定，Var(ŵ_signal) = σ²_w / n_test。其中 σ_w 为流量分配权重的波动标准差，通常假设 σ_w ≈ 0.1（基于算法迭代频率）。当 n_test < 500 时，Var(ŵ_signal) > 0.0002，导致后续偏导数估计不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式 Var(ŵ) = σ²/n 符合统计学基本原理；数值代入 0.1²/500 = 0.0002 计算正确，量级合理。
