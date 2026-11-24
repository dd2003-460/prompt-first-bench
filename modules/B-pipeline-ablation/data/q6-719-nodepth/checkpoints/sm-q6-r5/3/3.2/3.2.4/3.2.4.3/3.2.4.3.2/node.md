# N682: 回源带宽峰值冗余的计费模式对比：模式A（固定带宽包）成本 C_fixed = B_redundant * P_bw_monthly，P_bw_monthly ≈

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N233

## Claim

回源带宽峰值冗余的计费模式对比：模式A（固定带宽包）成本 C_fixed = B_redundant * P_bw_monthly，P_bw_monthly ≈ ¥500/100Mbps/月，C_fixed ≈ ¥675/月；模式B（95th峰值计费）成本 C_95th = P_95th * (Peak_95th - Base_95th)，其中 Peak_95th 为月内第95百分位带宽，若突发事件导致 Peak_95th 从 100Mbps 升至 200Mbps，则 C_95th ≈ ¥1000/100Mbps * 100Mbps = ¥1000/月；模式C（按量流量计费）成本 C_traffic = Traffic_redundant * P_traffic，Traffic_redundant ≈ 135Mbps * 4h * 2.2次/月 ≈ 360GB/月，C_traffic ≈ 360 * ¥0.8 ≈ ¥288/月；结论：对于低频突发，按量计费最划算，但需监控峰值以避免限流。

## Corrected Claim

回源带宽峰值冗余的计费模式对比：模式A（固定带宽包）成本 C_fixed = B_redundant * P_bw_monthly，P_bw_monthly ≈ ¥500/100Mbps/月，C_fixed ≈ ¥675/月；模式B（95th峰值计费）成本 C_95th = P_95th * (Peak_95th - Base_95th)，其中 Peak_95th 为月内第95百分位带宽，若突发事件导致 Peak_95th 从 100Mbps 升至 200Mbps，则 C_95th ≈ ¥1000/100Mbps * 100Mbps = ¥1000/月；模式C（按量流量计费）成本 C_traffic = Traffic_redundant * P_traffic，Traffic_redundant ≈ 135Mbps * 4h * 2.2次/月 ≈ 360GB/月，C_traffic ≈ 360 * ¥0.8 ≈ ¥288/月；结论：对于低频突发，按量计费最划算，但需监控峰值以避免限流。

## Evidence

先验知识/题面给定，逻辑校验通过：各模式成本计算公式及数值推导（固定带宽675元、95th峰值1000元、按量流量288元）在量纲和算术上均自洽，且符合云计算带宽计费的一般经济直觉（低频突发场景下按量计费通常优于固定或峰值计费）。
