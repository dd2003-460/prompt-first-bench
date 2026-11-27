# N186: 周期敏感度系数 γ_time 的量化：在 Retention = Retention_base * exp(-γ_time * (T_deal/T_median

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

周期敏感度系数 γ_time 的量化：在 Retention = Retention_base * exp(-γ_time * (T_deal/T_median - 1)) 中，γ_time 反映成交周期延长对留存的指数衰减影响，需通过用户流失日志回归确定（如 γ_time ∈ [0.2, 0.8]）。

## Corrected Claim

周期敏感度系数 γ_time 的量化：在 Retention = Retention_base * exp(-γ_time * (T_deal/T_median - 1)) 中，γ_time 反映成交周期延长对留存的指数衰减影响，需通过用户流失日志回归确定（具体数值范围依业务场景而定，无通用固定区间）。

## Evidence

[质询]参考来源均讨论气相色谱（GC）中的保留时间（Retention Time），与用户留存（User Retention）及成交周期敏感度系数完全无关，属于严重的领域混淆；且该系数具体数值范围 [0.2, 0.8] 为经验参数，缺乏通用理论支持。 | 逻辑上指数衰减模型自洽，但参考来源 [1][2][3] 均为化学分析领域，与用户行为建模无关，无法提供外部支持；作为经验事实，缺乏直接来源支持，故降级。

## Search Query

impact of transaction time on user retention churn rate elasticity

## Retrieval Sources

- {'url': 'https://www.phenomenex.com/resources/knowledge-center/gc-knowledge-center/understanding-retention-time&rut=910c2802397fe165beb2e5310c49a25d3968cb6b59e94bf65fb8de3c8e30cd58', 'type': 'ddg', 'title': 'Retention Time & Relative Retention Time in GC | Phenomenex'}
- {'url': 'https://www.shimadzu.com/an/service-support/technical-support/gas-chromatograph-mass-spectrometry/analysis-results/retention/retention.html&rut=ed9b0dc329201fc517894c1859eeaeb975961f6ecc0b0564569ee460061608a4', 'type': 'ddg', 'title': 'Qualitative Methods of GC/MS Analysis:Retention Time and Retention ...'}
- {'url': 'https://www.agilent.com/cs/library/support/Documents/RT.pdf&rut=0f85ce20751a9f162e1296062c1e0e6d99f1d712994dcbb6318730c3cd7a7d59', 'type': 'ddg', 'title': 'PDF Brief explanation of the terms Retention Time,Retention Factor (k ...'}
