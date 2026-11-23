# N52: 峰值因子 PF 的精确计算：PF = (Peak_TPS / Avg_TPS) = (Max_Hourly_Traffic / Avg_Hourly_Traff

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

峰值因子 PF 的精确计算：PF = (Peak_TPS / Avg_TPS) = (Max_Hourly_Traffic / Avg_Hourly_Traffic) / 24；对于双峰分布，PF ≈ 1.8 ± 0.2，具体值由早高峰峰值时长 T_peak_am 和晚高峰峰值时长 T_peak_pm 决定，PF = (V_peak_am / T_peak_am + V_peak_pm / T_peak_pm) / (V_dl / 24)

## Corrected Claim

峰值因子 PF 通常定义为峰值流量与平均流量之比。若基于小时流量数据，PF = Max_Hourly_Traffic / Avg_Hourly_Traffic；若基于瞬时 TPS，PF = Peak_TPS / Avg_TPS。对于双峰分布，PF 的具体数值取决于峰值持续时间与总流量的比例，典型值约为 1.5-2.0，但具体公式需明确分子分母的时间粒度一致性。

## Evidence

[质询]公式定义存在逻辑矛盾：PF 通常定义为峰值速率与平均速率之比，若分子是瞬时峰值 TPS，分母是平均 TPS，则不应再除以 24；若分子分母均为小时流量（Hourly Traffic），则 PF = Max_Hourly / Avg_Hourly，无需除以 24。陈述中同时出现 TPS 和 Hourly Traffic 且包含 /24 因子，导致量纲或定义口径混淆。 | 先验知识/题面给定，逻辑校验发现公式定义存在量纲/口径不一致（TPS vs Hourly Traffic 及 /24 因子的冗余或错误），无法确认为精确计算标准。

## Search Query

CDN traffic peak factor calculation dual peak distribution morning evening
