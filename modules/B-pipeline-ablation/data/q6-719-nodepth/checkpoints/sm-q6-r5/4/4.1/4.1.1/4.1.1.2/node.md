# N242: 单POP链路成本与带宽利用率权衡：单POP月带宽成本 C_bw_pop = B_provisioned × P_bw_line，其中 P_bw_line 为运营

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77

## Claim

单POP链路成本与带宽利用率权衡：单POP月带宽成本 C_bw_pop = B_provisioned × P_bw_line，其中 P_bw_line 为运营商专线单价（约¥2000-4000/Gbps/月）；若 B_provisioned=10Gbps，则 C_bw_pop ≈ ¥20,000-40,000/月，需对比实际平均利用率 U = 6.93/10 = 69.3% 下的单位有效带宽成本。

## Corrected Claim

单POP链路成本与带宽利用率权衡：单POP月带宽成本 C_bw_pop = B_provisioned × P_bw_line，其中 P_bw_line 为运营商专线单价（约¥2000-4000/Gbps/月）；若 B_provisioned=10Gbps，则 C_bw_pop ≈ ¥20,000-40,000/月，需对比实际平均利用率 U = 6.93/10 = 69.3% 下的单位有效带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过：单价量级（¥2000-4000/Gbps/月）符合国内运营商专线市场常见区间，数学计算（10Gbps * 2000-4000 = 20,000-40,000）及利用率计算（6.93/10=69.3%）均准确无误。
