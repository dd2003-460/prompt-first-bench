# N74: 公有云 CDN 利用率 U_pub 的成本影响函数：Cost_per_1k ∝ 1/U_pub。当 U_pub 从 30% 降至 15% 时，单位成本翻倍。需量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

公有云 CDN 利用率 U_pub 的成本影响函数：Cost_per_1k ∝ 1/U_pub。当 U_pub 从 30% 降至 15% 时，单位成本翻倍。需量化在 B_avg = 26.4 Mbps 固定情况下，不同 B_peak_pub 值（如 50/100/200 Mbps）对应的 U_pub 和每千请求成本。

## Corrected Claim

公有云 CDN 利用率 U_pub 的成本影响函数：Cost_per_1k ∝ 1/U_pub。当 U_pub 从 30% 降至 15% 时，单位成本翻倍。需量化在 B_avg = 26.4 Mbps 固定情况下，不同 B_peak_pub 值（如 50/100/200 Mbps）对应的 U_pub 和每千请求成本。

## Evidence

先验知识/题面给定，逻辑校验通过：成本与利用率成反比（Cost ∝ 1/U）是CDN容量规划的基本经济逻辑，30%降至15%导致成本翻倍符合数学推导。
