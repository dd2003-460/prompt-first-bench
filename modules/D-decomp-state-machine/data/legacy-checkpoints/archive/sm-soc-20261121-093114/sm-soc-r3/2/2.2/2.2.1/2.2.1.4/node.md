# N151: 后验更新幅度 Δμ_posterior 的计算：Δμ_posterior = (1 - w_signal) * μ_prior + w_signal * μ_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48, N49, N50

## Claim

后验更新幅度 Δμ_posterior 的计算：Δμ_posterior = (1 - w_signal) * μ_prior + w_signal * μ_signal - μ_prior，其中 w_signal = σ_prior² / (σ_prior² + σ_noise²) 为信号权重，μ_signal 为信号隐含的质量估计（如高挂价隐含 μ_signal = μ_prior + k_high * (P_ask/P_market - 1)），该公式量化了单次咨询或观察如何改变买家对商品质量的信念。

## Corrected Claim

后验更新幅度 Δμ_posterior 的计算：Δμ_posterior = (1 - w_signal) * μ_prior + w_signal * μ_signal - μ_prior，其中 w_signal = σ_prior² / (σ_prior² + σ_noise²) 为信号权重，μ_signal 为信号隐含的质量估计（如高挂价隐含 μ_signal = μ_prior + k_high * (P_ask/P_market - 1)），该公式量化了单次咨询或观察如何改变买家对商品质量的信念。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合贝叶斯更新在正态分布假设下的线性形式（后验均值 = 加权平均），权重 w_signal 符合精度加权原则（方差越小权重越大），量纲与逻辑自洽。

## Search Query

Bayesian posterior update formula signal weight prior variance noise variance
