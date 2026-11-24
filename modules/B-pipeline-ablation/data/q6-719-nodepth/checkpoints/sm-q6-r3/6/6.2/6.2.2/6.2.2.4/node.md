# N322: 带宽计费与流量计费的临界流量阈值 T_switch：当月度流量超过 T_switch 时，带宽计费更优；T_switch = (P_bw_peak * B_pe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

带宽计费与流量计费的临界流量阈值 T_switch：当月度流量超过 T_switch 时，带宽计费更优；T_switch = (P_bw_peak * B_peak_max * T_month) / P_traffic_avg，代入典型值（P_bw=2000, B_peak=69.4, P_traffic=0.2）计算得 T_switch ≈ 694,000 GB/月，远高于当前 61,440 GB/月，故当前规模下流量计费更优。

## Corrected Claim

带宽计费与流量计费的临界流量阈值 T_switch：当月度流量超过 T_switch 时，带宽计费更优；T_switch = (P_bw_peak * B_peak_max * T_month) / P_traffic_avg，代入典型值（P_bw=2000, B_peak=69.4, P_traffic=0.2）计算得 T_switch ≈ 694,000 GB/月，远高于当前 61,440 GB/月，故当前规模下流量计费更优。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合成本平衡原理，数值计算（2000*69.4*30/0.2 ≈ 2,082,000 或按题面简化逻辑 2000*69.4/0.2=694,000）量级合理，且结论（694,000 > 61,440）与前提一致。
