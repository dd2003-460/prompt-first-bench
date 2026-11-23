# N120: 有效单位带宽成本 C_eff_per_TB 的计算公式为 C_eff_per_TB = (P_peak_cap × P_lease) / (Daily_Traf

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

有效单位带宽成本 C_eff_per_TB 的计算公式为 C_eff_per_TB = (P_peak_cap × P_lease) / (Daily_Traffic_TB × 30)，其中 P_peak_cap 为峰值带宽（Gbps），P_lease 为月租单价，Daily_Traffic_TB 为日均流量，该值直接反映利用率低导致的成本放大效应，当 U_avg < 50% 时，C_eff_per_TB 通常高于公有云 CDN 流量单价。

## Corrected Claim

有效单位带宽成本 C_eff_per_TB 的计算公式为 C_eff_per_TB = (P_peak_cap × P_lease) / (Daily_Traffic_TB × 30)，其中 P_peak_cap 为峰值带宽（Gbps），P_lease 为月租单价，Daily_Traffic_TB 为日均流量，该值直接反映利用率低导致的成本放大效应，当 U_avg < 50% 时，C_eff_per_TB 通常高于公有云 CDN 流量单价。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（成本/流量），且低利用率导致单位成本高于公有云CDN符合经济学直觉。
