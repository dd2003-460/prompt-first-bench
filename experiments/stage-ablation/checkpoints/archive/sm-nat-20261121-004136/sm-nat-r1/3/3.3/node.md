# N14: 工作点3（高成本低性）：LFU 的计数器开销与更新率（1%/天）导致的‘频率老化’效应，量化为有效增益衰减因子 A_decay = exp(-λ * T_upd

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

工作点3（高成本低性）：LFU 的计数器开销与更新率（1%/天）导致的‘频率老化’效应，量化为有效增益衰减因子 A_decay = exp(-λ * T_update)，其中 λ 为频率遗忘率，T_update 为对象平均更新间隔，导致 LFU 实际增益低于理论上限。

## Corrected Claim

工作点3（高成本低性）：LFU 的计数器开销与更新率（1%/天）导致的‘频率老化’效应，量化为有效增益衰减因子 A_decay = exp(-λ * T_update)，其中 λ 为频率遗忘率，T_update 为对象平均更新间隔，导致 LFU 实际增益低于理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过
