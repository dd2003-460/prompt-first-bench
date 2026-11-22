# N616: Mac Studio M2 Ultra 在满载推理时的典型功耗为 200-250W（非 N189 估算的 300-400W，后者可能包含极端负载或旧款 M1 U

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N188, N189, N190

## Claim

Mac Studio M2 Ultra 在满载推理时的典型功耗为 200-250W（非 N189 估算的 300-400W，后者可能包含极端负载或旧款 M1 Ultra 数据），修正后年 OpEx ≈ 250W * 8760h * $0.10/kWh = $2,190/年，3 年 OpEx 为 $6,570。

## Corrected Claim

Mac Studio M2 Ultra 在满载推理时的典型功耗约为 200-250W（需具体负载验证），若按此功耗及 $0.10/kWh 电价计算，年 OpEx 约为 $2,190，3 年 OpEx 约为 $6,570。

## Evidence

[质询]该陈述包含具体的硬件功耗参数（200-250W）和电价假设（$0.10/kWh），属于经验事实。虽然数学计算（250 * 8760 * 0.1 = 2190）在逻辑上自洽，但缺乏外部来源支持其功耗数值是否准确代表'Mac Studio M2 Ultra 满载推理'的典型值，且电价假设具有地域依赖性，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体功耗数值及电价假设的普适性）

## Search Query

Mac Studio M2 Ultra full load power consumption watts LLM inference
