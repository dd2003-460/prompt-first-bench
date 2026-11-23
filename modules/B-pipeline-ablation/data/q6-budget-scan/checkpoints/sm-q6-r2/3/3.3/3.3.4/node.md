# N75: 地理分布对带宽成本的非线性影响：跨境流量（东南亚+其他20%）的带宽单价通常是境内流量的1.5-2倍；若跨境流量占比20%，则加权平均带宽单价 P_bw_avg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

地理分布对带宽成本的非线性影响：跨境流量（东南亚+其他20%）的带宽单价通常是境内流量的1.5-2倍；若跨境流量占比20%，则加权平均带宽单价 P_bw_avg = 0.8 * P_domestic + 0.2 * 1.5 * P_domestic = 1.1 * P_domestic。

## Corrected Claim

地理分布对带宽成本的非线性影响：跨境流量（东南亚+其他20%）的带宽单价通常是境内流量的1.5-2倍；若跨境流量占比20%，则加权平均带宽单价 P_bw_avg = 0.8 * P_domestic + 0.2 * 1.5 * P_domestic = 1.1 * P_domestic。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.8 + 0.2*1.5 = 1.1 正确，跨境带宽成本高于境内符合行业常识。
