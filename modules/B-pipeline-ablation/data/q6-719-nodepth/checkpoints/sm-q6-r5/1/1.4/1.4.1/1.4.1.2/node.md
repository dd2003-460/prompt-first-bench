# N149: 峰值时长对计费模式选择的决策阈值：定义成本差函数 ΔCost = Cost_peak_billing - Cost_traffic_billing。当 D_pe

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N47

## Claim

峰值时长对计费模式选择的决策阈值：定义成本差函数 ΔCost = Cost_peak_billing - Cost_traffic_billing。当 D_peak < 0.08 时，带宽峰值计费通常更优（因为峰值时间极短，平均带宽低）；当 D_peak > 0.15 时，流量计费更优。对于 C 端平台 D_peak ≈ 0.1-0.15 处于临界区，需结合具体单价 P_bw (¥/Gbps/mo) 与 P_traffic (¥/GB) 的比值 R_price = P_bw / (P_traffic * 86400 * 1000) 进行精确计算，若 R_price < 0.6 则选带宽计费。

## Corrected Claim

峰值时长对计费模式选择存在决策阈值：定义成本差函数 ΔCost = Cost_peak_billing - Cost_traffic_billing。通常当峰值占比 D_peak 较低时，带宽峰值计费更优；当 D_peak 较高时，流量计费更优。对于 C 端平台，D_peak 处于临界区（如 0.1-0.15），需结合具体单价比值 R_price 进行精确计算以决定最优计费模式。

## Evidence

[质询]阈值 0.08 和 0.15 以及 R_price < 0.6 的具体数值缺乏通用理论支持，属于特定场景下的经验参数，不同云厂商定价策略差异大，直接作为通用决策阈值可能误导。 | 先验知识/题面给定，逻辑校验通过（成本函数定义及临界区概念符合经济学直觉），但具体阈值数值为经验事实，无外部来源直接支持，故降级。
