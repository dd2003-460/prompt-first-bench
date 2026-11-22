# N106: 头部对象(i=1)的驻留概率 x_1 计算：x_1 = min(1, λ_1 * T_resident_1)；基于N50的T_resident_1和λ_1（假设

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

头部对象(i=1)的驻留概率 x_1 计算：x_1 = min(1, λ_1 * T_resident_1)；基于N50的T_resident_1和λ_1（假设λ_max ≈ 5e7 * 0.01 /天 = 5e5/天，基于Pareto(β=0.9)头部占比），计算 x_1 = min(1, 5e5 * T_resident_1)，若T_resident_1为秒级，x_1可能接近1；若T_resident_1为毫秒级，x_1 < 1，需确定具体数值以验证头部对象是否被LRU完全保护。

## Corrected Claim

头部对象(i=1)的驻留概率 x_1 取决于 λ_1 与 T_resident_1 的乘积。若 λ_1 约为 5e5/天（约 5.8/秒），则当 T_resident_1 > 0.17秒 时 x_1 接近 1；若 T_resident_1 为毫秒级，x_1 < 1。需结合具体 T_resident_1 数值确定头部对象是否被完全保护。

## Evidence

[质询]λ_1 的估算值 5e5/天 缺乏具体业务场景支撑，属于任意假设；且 T_resident_1 未给出具体数值，导致 x_1 无法得出确定结论，仅能给出条件性范围。 | 先验知识/题面给定，逻辑校验通过；但 λ_1 为经验假设且 T_resident_1 未定，无法验证具体数值，故降级为定性表述。
