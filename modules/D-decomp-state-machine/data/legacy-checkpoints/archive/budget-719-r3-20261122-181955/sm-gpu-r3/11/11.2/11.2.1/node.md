# N375: 修正N127电力成本计算：N127使用TDP 450W直接计算，但N103指出LLM推理负载下平均功耗为TDP的60-80%。采用P_avg = 0.7 * 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N127

## Claim

修正N127电力成本计算：N127使用TDP 450W直接计算，但N103指出LLM推理负载下平均功耗为TDP的60-80%。采用P_avg = 0.7 * 450W = 315W，年电力成本 = 315W * 8760h * $0.14/kWh（N104修正电价）= $387/年，而非N127的$590/年。

## Corrected Claim

修正N127电力成本计算：N127使用TDP 450W直接计算，但N103指出LLM推理负载下平均功耗为TDP的60-80%。采用P_avg = 0.7 * 450W = 315W，年电力成本 = 315W * 8760h * $0.14/kWh（N104修正电价）= $387/年，而非N127的$590/年。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 315W * 8760h * $0.14/kWh ≈ $387.11，与陈述一致；且符合LLM推理负载平均功耗低于TDP的工程常识。
