# N638: 工作点 A（高性低成）：V100 在持续高负载（如大 batch 推理）下实际稳态功耗 P_actual 约为 200-220W，低于 TDP 250W，能效比

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N228

## Claim

工作点 A（高性低成）：V100 在持续高负载（如大 batch 推理）下实际稳态功耗 P_actual 约为 200-220W，低于 TDP 250W，能效比 η_A = P_useful/P_actual 约为 0.85，月电费 Cost_A ≈ 210W × 720h × $0.35/kWh ≈ $53

## Corrected Claim

工作点 A（高性低成）：V100 在持续高负载下实际稳态功耗 P_actual 约为 200-220W，低于 TDP 250W。假设电价为 $0.35/kWh，月电费 Cost_A ≈ 210W × 720h × $0.35/kWh ≈ $53。（注：原陈述中能效比 η_A=0.85 定义不明，建议移除或明确为‘相对于TDP的功率利用率’）

## Evidence

[质询]能效比 η_A = 0.85 的定义模糊且数值存疑：若指电能转化为有用计算功的比例，通常远低于此（大部分转化为热）；若指相对于TDP的利用率，则与功耗描述重复。此外，$0.35/kWh 的电价属于特定地区经验数据，缺乏通用性。 | 经验事实，逻辑自洽但缺来源支持。功耗范围（200-220W < 250W TDP）符合V100在高负载下的典型表现，电费计算公式正确，但能效比定义不清且电价依赖特定假设，无外部来源验证。

## Search Query

V100 sustained power consumption under full load watts
