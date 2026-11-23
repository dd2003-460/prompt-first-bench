# N52: 峰值因子 PF 的精确计算：PF = (Peak_TPS / Avg_TPS) = (Max_Hourly_Traffic / Avg_Hourly_Traff

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

峰值因子 PF 的精确计算：PF = (Peak_TPS / Avg_TPS) = (Max_Hourly_Traffic / Avg_Hourly_Traffic) / 24；对于双峰分布，PF ≈ 1.8 ± 0.2，具体值由早高峰峰值时长 T_peak_am 和晚高峰峰值时长 T_peak_pm 决定，PF = (V_peak_am / T_peak_am + V_peak_pm / T_peak_pm) / (V_dl / 24)

## Corrected Claim

峰值因子 PF 通常定义为峰值流量与平均流量之比。若基于小时流量数据，PF = Max_Hourly_Traffic / Avg_Hourly_Traffic；若基于瞬时 TPS，PF = Peak_TPS / Avg_TPS。对于双峰分布，PF 的具体数值取决于峰值持续时间与总流量的比例，典型值约为 1.5-2.0，但具体公式需明确分子分母的时间粒度一致性。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 矛盾/非正交：父节点公式 PF = (Max_Hourly / Avg_Hourly) / 24 存在量纲和逻辑错误（通常 PF=Max/Avg，除以24无物理意义，除非Max是全天总和而非峰值速率，但此处定义为Hourly Traffic），而子节点3推导的公式 PF = (1 + T_peak*(K-1))/24 同样存在严重的数学逻辑错误（量纲不匹配，左侧无量纲，右侧除以24导致数值缩小24倍，且K_peak定义循环依赖）。子节点1计算的是平均带宽，与父节点关注的“峰值因子”概念层级不同。2. 不完备：子节点未解释为何父节点公式中要除以24，也未修正该公式的错误。3. 冗余：子节点3中的公式推导混乱，K_peak的定义试图自我引用PF，逻辑闭环错误。）

## Search Query

CDN traffic peak factor calculation dual peak distribution morning evening
