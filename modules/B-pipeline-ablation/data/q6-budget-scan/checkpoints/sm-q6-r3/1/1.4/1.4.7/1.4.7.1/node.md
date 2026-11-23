# N147: 计算自建节点带宽冗余导致的闲置成本：冗余带宽量 R_bw = (PF - 1) * BW_avg，闲置时长占比 U_idle = 1 - (T_peak_am 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

计算自建节点带宽冗余导致的闲置成本：冗余带宽量 R_bw = (PF - 1) * BW_avg，闲置时长占比 U_idle = 1 - (T_peak_am + T_peak_pm)/24，年化闲置机会成本 C_idle = R_bw * P_bw_peak * 12 * U_idle。

## Corrected Claim

计算自建节点带宽冗余导致的闲置成本：冗余带宽量 R_bw = (PF - 1) * BW_avg，闲置时长占比 U_idle = 1 - (T_peak_am + T_peak_pm)/24，年化闲置机会成本 C_idle = R_bw * P_bw_peak * 12 * U_idle。

## Evidence

先验知识/题面给定，逻辑校验通过
