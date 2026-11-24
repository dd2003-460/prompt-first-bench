# N606: 单POP带宽月成本 P_bw_pop 的带宽-流量混合计费模型：P_bw_pop = max(B_pop_peak * P_bw_fixed, Traffic_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N198, N199, N200

## Claim

单POP带宽月成本 P_bw_pop 的带宽-流量混合计费模型：P_bw_pop = max(B_pop_peak * P_bw_fixed, Traffic_out_pop * P_bw_usage) + C_ip_rental，其中 P_bw_fixed = ¥1500-2500/Gbps/月（专线），P_bw_usage = ¥0.5-1.0/GB（按量），C_ip_rental = ¥200-500/月（IP资源费），需取两者最大值作为保底成本。

## Corrected Claim

单POP带宽月成本 P_bw_pop 的带宽-流量混合计费模型：P_bw_pop = max(B_pop_peak * P_bw_fixed, Traffic_out_pop * P_bw_usage) + C_ip_rental，其中 P_bw_fixed = ¥1500-2500/Gbps/月（专线），P_bw_usage = ¥0.5-1.0/GB（按量），C_ip_rental = ¥200-500/月（IP资源费），需取两者最大值作为保底成本。

## Evidence

先验知识/题面给定，逻辑校验通过
