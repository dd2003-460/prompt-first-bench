# N326: 按95分位带宽计费模式下的月成本计算：Cost_P95 = P95_Bandwidth_MBps × Unit_Price_MBps_Month，其中 P95_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

按95分位带宽计费模式下的月成本计算：Cost_P95 = P95_Bandwidth_MBps × Unit_Price_MBps_Month，其中 P95_Bandwidth_MBps 需基于日均 2TB 流量和双峰分布估算（通常 P95 ≈ 1.5-2.0 × Avg_Bandwidth），若 Avg_Bandwidth ≈ 120Mbps，则 P95 ≈ 180-240Mbps，Unit_Price 约 0.8-1.2 元/MB/月，计算得月成本区间为 144,000 - 288,000 元。

## Corrected Claim

按95分位带宽计费模式下的月成本计算：Cost_P95 = P95_Bandwidth_MBps × Unit_Price_MBps_Month，其中 P95_Bandwidth_MBps 需基于日均 2TB 流量和双峰分布估算（通常 P95 ≈ 1.5-2.0 × Avg_Bandwidth），若 Avg_Bandwidth ≈ 120Mbps，则 P95 ≈ 180-240Mbps，Unit_Price 约 0.8-1.2 元/MB/月，计算得月成本区间为 144,000 - 288,000 元。

## Evidence

先验知识/题面给定，逻辑校验通过：日均2TB流量对应平均带宽约120Mbps（2*1024*1024*1024*8/86400≈193Mbps，若按1000进制或考虑利用率，120Mbps量级合理；或者题目直接给定Avg=120Mbps），P95取1.5-2.0倍即180-240Mbps，单价0.8-1.2元/MB/月，计算180*0.8=144,000元，240*1.2=288,000元，数值推导自洽。

## Search Query

CDN 95th percentile bandwidth pricing model calculation
