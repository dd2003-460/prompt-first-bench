# N126: 在 Pareto(β=0.9) 热度分布下，排名 i 的对象被请求的期望间隔时间 Δt_i 与总请求率 R 的关系为 Δt_i = 1 / (R * f_i /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

在 Pareto(β=0.9) 热度分布下，排名 i 的对象被请求的期望间隔时间 Δt_i 与总请求率 R 的关系为 Δt_i = 1 / (R * f_i / R_total) = R_total / (R * i^(-β))，该公式用于判断在 1%/天 的更新率下，头部对象是否会在被再次请求前失效。

## Corrected Claim

在 Pareto(β=0.9) 热度分布下，排名 i 的对象被请求的期望间隔时间 Δt_i 与总请求率 R 的关系为 Δt_i = 1 / (R * f_i / R_total) = R_total / (R * i^(-β))，该公式用于判断在 1%/天 的更新率下，头部对象是否会在被再次请求前失效。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布下频率与排名成反比，期望间隔时间与频率成反比，公式推导符合基本概率论原理。
