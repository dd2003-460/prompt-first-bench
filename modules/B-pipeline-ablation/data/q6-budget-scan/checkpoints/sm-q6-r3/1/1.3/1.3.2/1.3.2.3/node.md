# N137: 两种计费模式的成本差异量化：Cost_Ratio = C_peak_billing / C_traffic_billing；若 B_peak_committed

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

两种计费模式的成本差异量化：Cost_Ratio = C_peak_billing / C_traffic_billing；若 B_peak_committed = 1Gbps，月租 ¥5,000，则 C_peak_billing = ¥5,000，C_traffic_billing = ¥13,200，此时峰值计费更优；但若 B_peak_committed 需升至 5Gbps（¥25,000），则流量计费更优。临界点 B_break_even = C_traffic_billing / P_bw_peak_per_Gbps_monthly

## Corrected Claim

两种计费模式的成本差异量化：Cost_Ratio = C_peak_billing / C_traffic_billing；若 B_peak_committed = 1Gbps，月租 ¥5,000，则 C_peak_billing = ¥5,000，C_traffic_billing = ¥13,200，此时峰值计费更优；但若 B_peak_committed 需升至 5Gbps（¥25,000），则流量计费更优。临界点 B_break_even = C_traffic_billing / P_bw_peak_per_Gbps_monthly

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（5000 < 13200 且 25000 > 13200），临界点公式推导正确（13200 / 5000 = 2.64 Gbps，符合逻辑），无外部来源矛盾。
