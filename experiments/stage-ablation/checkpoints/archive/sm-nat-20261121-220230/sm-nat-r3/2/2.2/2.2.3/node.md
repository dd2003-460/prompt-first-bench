# N51: LFU 的累计频率统计滞后误差 Δ_f = |f_LFU(t) - f_true(t)|，其中 f_LFU 是 LFU 估计的频率，f_true 是实际频率；Δ

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

LFU 的累计频率统计滞后误差 Δ_f = |f_LFU(t) - f_true(t)|，其中 f_LFU 是 LFU 估计的频率，f_true 是实际频率；Δ_f 随时间步长 Δt 线性增长，当 Δ_f > f_threshold 时，LFU 决策错误率显著上升。

## Corrected Claim

LFU 的累计频率统计存在滞后误差 Δ_f = |f_LFU(t) - f_true(t)|。随着时间推移，若访问模式发生显著变化，Δ_f 会累积增大；当 Δ_f 超过阈值 f_threshold 时，LFU 决策错误率显著上升。

## Evidence

[质询]「Δ_f 随时间步长 Δt 线性增长」这一具体动力学描述缺乏普遍理论支持。LFU 的误差累积取决于访问模式（如突发流量、周期性访问）和计数器重置策略，并非简单的线性关系；在稳态或特定分布下，误差可能收敛或呈现非线性特征。 | 先验知识/题面给定，逻辑校验通过。虽然 LFU 存在滞后误差且误差过大导致决策错误是合理的定性结论，但「线性增长」这一具体定量关系属于经验性/模型假设，非第一性原理必然推论，且无来源支持，故降级。

## Search Query

LFU frequency estimation error lag time step
