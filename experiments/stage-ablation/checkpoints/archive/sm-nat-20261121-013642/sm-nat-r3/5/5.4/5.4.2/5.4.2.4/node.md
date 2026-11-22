# N222: 方差缩减技术（Variance Reduction）在 Monte Carlo 仿真中的应用：使用控制变量法（Control Variates）以已知解析解 H

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N75

## Claim

方差缩减技术（Variance Reduction）在 Monte Carlo 仿真中的应用：使用控制变量法（Control Variates）以已知解析解 H_LRU_lower 为基准，将仿真估计值 H_hat 修正为 H_hat_cv = H_hat + c * (H_LRU_lower - H_LRU_sim)，其中 c 为回归系数，可使方差降低 50%-70%，从而将所需样本量 N_samples 从 10^6 降至 3e5-5e5。

## Corrected Claim

方差缩减技术（Variance Reduction）在 Monte Carlo 仿真中的应用：使用控制变量法（Control Variates）以已知解析解 H_LRU_lower 为基准，将仿真估计值 H_hat 修正为 H_hat_cv = H_hat + c * (H_LRU_lower - H_LRU_sim)，其中 c 为回归系数，可显著降低方差，从而减少所需样本量。

## Evidence

[质询]方差缩减的具体比例（50%-70%）及由此推导的样本量缩减范围（10^6 降至 3e5-5e5）属于高度依赖具体场景（如相关性系数、分布形态）的经验性数值，并非通用常数，且缺乏来源支持该特定量级。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

variance reduction Monte Carlo simulation cache hit rate heavy-tailed distribution
