# N660: 单次云端调用成本公式：Cost_per_call = (L_in * P_in + L_out * P_out) / 1e6，其中 P_in=$2.50, P_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N241

## Claim

单次云端调用成本公式：Cost_per_call = (L_in * P_in + L_out * P_out) / 1e6，其中 P_in=$2.50, P_out=$10.00，代入 L_in=12000, L_out=500 得 Cost_per_call = (12000*2.5 + 500*10)/1e6 = $0.035

## Corrected Claim

单次云端调用成本公式：Cost_per_call = (L_in * P_in + L_out * P_out) / 1e6，其中 P_in=$2.50, P_out=$10.00，代入 L_in=12000, L_out=500 得 Cost_per_call = (12000*2.5 + 500*10)/1e6 = $0.035

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (12000*2.5 + 500*10)/1e6 = (30000+5000)/1e6 = 35000/1e6 = 0.035，数值与单位换算正确。
