# N113: P_opportunity_cost 的量化公式：P_opportunity_cost = P_base * r_risk_free * T_wait/365，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

P_opportunity_cost 的量化公式：P_opportunity_cost = P_base * r_risk_free * T_wait/365，其中 r_risk_free 为无风险利率（典型值 3%），T_wait 为预期等待天数；例如 T_wait=30天，P_base=100元，则机会成本约为 0.25元，远低于典型值 30，说明典型值 30 可能包含了流动性风险溢价。

## Corrected Claim

P_opportunity_cost 的量化公式：P_opportunity_cost = P_base * r_risk_free * T_wait/365，其中 r_risk_free 为无风险利率（典型值 3%），T_wait 为预期等待天数；例如 T_wait=30天，P_base=100元，则机会成本约为 0.25元，远低于典型值 30，说明典型值 30 可能包含了流动性风险溢价。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确（100*0.03*30/365≈0.247），量级合理，且正确指出了纯时间机会成本与包含流动性风险溢价的典型值之间的差异。
