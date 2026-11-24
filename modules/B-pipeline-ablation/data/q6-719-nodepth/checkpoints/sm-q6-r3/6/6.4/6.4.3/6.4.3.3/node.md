# N518: s_critical的计算公式：s_critical = (C_infra_self * 1000 / Q_day) / (P_bw_pub - P_bw_se

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N171

## Claim

s_critical的计算公式：s_critical = (C_infra_self * 1000 / Q_day) / (P_bw_pub - P_bw_self * H_miss)，其中C_infra_self为自建基础设施日成本，Q_day为日均请求量，P_bw_pub和P_bw_self为带宽单价。

## Corrected Claim

s_critical的计算公式：s_critical = (C_infra_self * 1000 / Q_day) / (P_bw_pub - P_bw_self * H_miss)，其中C_infra_self为自建基础设施日成本，Q_day为日均请求量，P_bw_pub和P_bw_self为带宽单价。

## Evidence

先验知识/题面给定，逻辑校验通过
