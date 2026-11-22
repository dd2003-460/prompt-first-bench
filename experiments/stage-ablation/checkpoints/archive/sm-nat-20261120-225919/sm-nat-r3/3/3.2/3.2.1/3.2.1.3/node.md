# N160: LFU 滞后时间 τ_lag 的物理定义：指频率计数器从初始值收敛到稳态分布所需的时间常数，在指数遗忘因子 λ 下，τ_lag = 1/λ，需确定 λ 与访问频

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N55, N56, N57

## Claim

LFU 滞后时间 τ_lag 的物理定义：指频率计数器从初始值收敛到稳态分布所需的时间常数，在指数遗忘因子 λ 下，τ_lag = 1/λ，需确定 λ 与访问频率 R_avg 及波动率 σ_f 的具体耦合公式

## Corrected Claim

LFU 滞后时间 τ_lag 的物理定义：指频率计数器从初始值收敛到稳态分布所需的时间常数，在指数遗忘因子 λ 下，τ_lag = 1/λ，需确定 λ 与访问频率 R_avg 及波动率 σ_f 的具体耦合公式

## Evidence

先验知识/题面给定，逻辑校验通过：在指数遗忘模型中，时间常数 τ 定义为 1/λ 符合物理直觉与数学定义，且 LFU 滞后时间的概念在缓存理论中成立。

## Search Query

LFU cache eviction lag time constant frequency decay
