# N240: P(D2 | H_signal) = 0.7 的机制验证：成交周期缩短20%需通过搜索成本降低来解释。设基准搜索成本 C_search = 10分钟/件，信号机

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

P(D2 | H_signal) = 0.7 的机制验证：成交周期缩短20%需通过搜索成本降低来解释。设基准搜索成本 C_search = 10分钟/件，信号机制下 C_search' = C_search * (1 - η_eff)。若 η_eff = 0.25（25%效率提升），则 C_search' = 7.5分钟。成交周期 T ∝ C_search，故 T' = T * (1 - 0.25) = 0.75T，即缩短25%。但题面数据为缩短20%，故 η_eff 需校准为 0.20。需验证：在 η_eff=0.20 时，P(D2 | H_signal) 是否仍为 0.7？若 D2 定义为‘周期缩短≥20%’，则需计算 T'/T 的分布，假设 T 服从对数正态分布，P(T'/T ≤ 0.8 | H) 需通过蒙特卡洛模拟估算，而非直接设定为 0.7。

## Corrected Claim

P(D2 | H_signal) = 0.7 的机制验证：成交周期缩短20%需通过搜索成本降低来解释。设基准搜索成本 C_search = 10分钟/件，信号机制下 C_search' = C_search * (1 - η_eff)。若 η_eff = 0.25（25%效率提升），则 C_search' = 7.5分钟。成交周期 T ∝ C_search，故 T' = T * (1 - 0.25) = 0.75T，即缩短25%。但题面数据为缩短20%，故 η_eff 需校准为 0.20。需验证：在 η_eff=0.20 时，P(D2 | H_signal) 是否仍为 0.7？若 D2 定义为‘周期缩短≥20%’，则需计算 T'/T 的分布，假设 T 服从对数正态分布，P(T'/T ≤ 0.8 | H) 需通过蒙特卡洛模拟估算，而非直接设定为 0.7。

## Evidence

先验知识/题面给定，逻辑校验通过：推导过程自洽，正确识别了直接设定概率与基于分布模拟估算概率之间的方法论差异，且数值量级合理。

## Search Query

search cost reduction transaction time elasticity marketplace
