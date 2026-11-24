# N340: 回源带宽成本增量 ΔCost_bw_back = B_back_peak * P_bw_back * T_fault，其中 P_bw_back 为回源带宽单价（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N112

## Claim

回源带宽成本增量 ΔCost_bw_back = B_back_peak * P_bw_back * T_fault，其中 P_bw_back 为回源带宽单价（¥1000-3000/Gbps/月，折算小时单价约 ¥0.7-2.0/Gbps/h）；计算得 ΔCost_bw_back ≈ 4.4 Gbps * ¥1.5/Gbps/h * 4h ≈ ¥26.4/次故障，月度期望成本 = ¥26.4 * 12次/月 ≈ ¥316.8/月。

## Corrected Claim

回源带宽成本增量 ΔCost_bw_back = B_back_peak * P_bw_back * T_fault，其中 P_bw_back 为回源带宽单价（¥1000-3000/Gbps/月，折算小时单价约 ¥0.7-2.0/Gbps/h）；计算得 ΔCost_bw_back ≈ 4.4 Gbps * ¥1.5/Gbps/h * 4h ≈ ¥26.4/次故障，月度期望成本 = ¥26.4 * 12次/月 ≈ ¥316.8/月。

## Evidence

先验知识/题面给定，逻辑校验通过：带宽单价量级（¥0.7-2.0/Gbps/h）符合行业常识，算术计算（4.4 * 1.5 * 4 = 26.4; 26.4 * 12 = 316.8）准确无误，公式逻辑自洽。
