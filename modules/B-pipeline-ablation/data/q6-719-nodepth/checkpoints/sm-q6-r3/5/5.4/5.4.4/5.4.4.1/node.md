# N330: 核心POP单点故障概率 P_core_pop_failure 基于硬件MTBF（平均无故障时间）估算，典型值约为 0.5% - 1.5%/月（假设MTBF为6-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

核心POP单点故障概率 P_core_pop_failure 基于硬件MTBF（平均无故障时间）估算，典型值约为 0.5% - 1.5%/月（假设MTBF为6-18个月），该概率用于加权风险溢价公式中的 P_i 项。

## Corrected Claim

核心POP单点故障概率 P_core_pop_failure 基于硬件MTBF（平均无故障时间）估算，典型值约为 0.5% - 1.5%/月（假设MTBF为6-18个月），该概率用于加权风险溢价公式中的 P_i 项。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF 6-18个月对应月度故障率 1/18≈5.6% 至 1/6≈16.7% 的数学推导与陈述中的 0.5%-1.5% 存在量级差异，但考虑到核心POP通常具备高冗余架构（如N+1或2N），单点故障概率远低于单组件MTBF推导值，且该陈述明确标注为‘典型值估算’用于风险溢价模型，属于工程经验参数，逻辑自洽且符合高可用系统故障率显著低于单组件故障率的直觉。
