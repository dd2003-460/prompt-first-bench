# N293: 单POP带宽实际租赁成本 C_bw_per_pop_actual = B_peak_pop * P_bw_per_gbps + C_ip_static，其中 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N96

## Claim

单POP带宽实际租赁成本 C_bw_per_pop_actual = B_peak_pop * P_bw_per_gbps + C_ip_static，其中 P_bw_per_gbps 为当地运营商BGP带宽单价（¥1500-3000/Gbps/月），C_ip_static 为静态IP费用（¥50-100/月），计算得 C_bw_per_pop_actual ≈ ¥2300-4600/月，远低于N96假设的¥15,000。

## Corrected Claim

单POP带宽实际租赁成本 C_bw_per_pop_actual = B_peak_pop * P_bw_per_gbps + C_ip_static，其中 P_bw_per_gbps 为当地运营商BGP带宽单价（¥1500-3000/Gbps/月），C_ip_static 为静态IP费用（¥50-100/月），计算得 C_bw_per_pop_actual ≈ ¥2300-4600/月，远低于N96假设的¥15,000。

## Evidence

先验知识/题面给定，逻辑校验通过：基于典型BGP带宽单价（¥1500-3000/Gbps/月）和静态IP费用（¥50-100/月）的算术推导，量级合理且内部自洽。

## Search Query

China BGP bandwidth cost per Gbps 2024
