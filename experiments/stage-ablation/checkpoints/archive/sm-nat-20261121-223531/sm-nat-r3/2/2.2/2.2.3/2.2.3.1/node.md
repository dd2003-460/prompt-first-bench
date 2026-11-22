# N128: 静态热度阈值模型与动态LRU行为的偏差量化：偏差项 $\Delta H_{LRU-Static} = H_{LRU} - H_{Static}$，其中 $H_{

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

静态热度阈值模型与动态LRU行为的偏差量化：偏差项 $\Delta H_{LRU-Static} = H_{LRU} - H_{Static}$，其中 $H_{Static}$ 基于累计热度排名，$H_{LRU}$ 基于最近访问序列。在Pareto分布下，该偏差主要来源于高频对象的访问间隔方差 $\sigma_{interval}^2$，偏差量级约为 $O(\sigma_{interval} / \mu_{interval})$，通常小于 2%。

## Corrected Claim

静态热度阈值模型与动态LRU行为的偏差量化：偏差项 ΔH_LRU-Static = H_LRU - H_Static，其中 H_Static 基于累计热度排名，H_LRU 基于最近访问序列。在Pareto分布下，该偏差主要来源于高频对象的访问间隔方差 σ_interval^2，偏差量级约为 O(σ_interval / μ_interval)，具体数值取决于工作负载特征，并非恒定的 2%。

## Evidence

[质询]偏差量级 O(σ/μ) 与 '通常小于 2%' 的断言缺乏普适性：在 Pareto 分布下，高频对象的访问间隔方差通常很大（σ/μ 往往远大于 0.02），且 LRU 与静态热度模型的偏差取决于具体工作负载特征，并非恒定的数学常数，'通常小于 2%' 属于未经证实的经验性过度概括。 | 先验知识/题面给定，逻辑校验通过，但 '通常小于 2%' 为经验性断言，缺乏来源支持且存在反例可能，故降级。
