# N55: 贝叶斯建议价的误差结构：算法建议价 P_suggest 与真实市场均衡价 P_equilibrium 的偏差 ε = |P_suggest - P_equili

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N18

## Claim

贝叶斯建议价的误差结构：算法建议价 P_suggest 与真实市场均衡价 P_equilibrium 的偏差 ε = |P_suggest - P_equilibrium| 服从正态分布 N(0, σ_est^2)，其中 σ_est 取决于历史成交数据的样本量 n 和波动率 σ_market，量化为 σ_est = σ_market / sqrt(n)。

## Corrected Claim

贝叶斯建议价的误差结构通常近似服从正态分布，其标准差 σ_est 与历史成交数据的样本量 n 的平方根成反比，并受市场波动率 σ_market 及先验信息强度的共同影响，简化形式可表示为 σ_est ≈ σ_market / sqrt(n)（在强先验或大样本近似下）。

## Evidence

[质询]该陈述将复杂的贝叶斯定价误差结构简化为单一的正态分布 N(0, σ_est^2)，且假设标准差仅由 σ_market/sqrt(n) 决定。这忽略了贝叶斯推断中先验分布（Prior）对后验分布（Posterior）的收缩效应（Shrinkage），即实际误差方差通常小于纯频率派估计的方差，且受先验强度影响；此外，市场均衡价本身是动态且非平稳的，简单正态假设在金融/经济数据中往往不成立（存在厚尾、异方差等）。 | source=knowledge，逻辑上量纲自洽（σ_market 为价格单位，sqrt(n) 无量纲，结果为单位价格），符合大数定律下标准误的基本形式；但作为经验事实/模型假设，缺乏来源支持其具体分布形式和参数化方式的普适性，故降级。
