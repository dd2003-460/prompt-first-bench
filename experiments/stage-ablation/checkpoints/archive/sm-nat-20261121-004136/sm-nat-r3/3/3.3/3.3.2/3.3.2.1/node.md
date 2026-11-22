# N126: 工作点1（高性低成/理论上限）：假设 LFU 计数器半衰期 T_half = T_update = 100天，则衰减因子 A_decay = exp(-ln(2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点1（高性低成/理论上限）：假设 LFU 计数器半衰期 T_half = T_update = 100天，则衰减因子 A_decay = exp(-ln(2) * 100/100) = 0.5，此时频率估计无偏但无法区分新旧热度，适用于稳态分析。

## Corrected Claim

工作点1（高性低成/理论上限）：假设 LFU 计数器半衰期 T_half = T_update = 100天，则衰减因子 A_decay = exp(-ln(2) * 100/100) = 0.5，此时频率估计无偏但无法区分新旧热度，适用于稳态分析。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减公式 A = exp(-ln(2) * t / T_half) 在 t=T_half 时确实等于 0.5，且 LFU 半衰期机制的理论描述符合逻辑。
