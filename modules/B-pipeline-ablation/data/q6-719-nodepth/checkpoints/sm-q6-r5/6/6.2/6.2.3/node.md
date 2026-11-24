# N106: 流量波动对月度总成本的放大效应量化：定义成本放大系数 C_amp = Cost_bw_actual / Cost_bw_avg，其中 Cost_bw_avg 基

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

流量波动对月度总成本的放大效应量化：定义成本放大系数 C_amp = Cost_bw_actual / Cost_bw_avg，其中 Cost_bw_avg 基于日均流量恒定假设计算；当 K_peak=4 持续 4 小时/天且占全天 16.7% 时，C_amp ≈ 1.15-1.25（即实际成本比均值假设高 15%-25%），该系数需纳入 TCO 对比的修正项。

## Corrected Claim

流量波动对月度总成本的放大效应量化：定义成本放大系数 C_amp = Cost_bw_actual / Cost_bw_avg，其中 Cost_bw_avg 基于日均流量恒定假设计算；当 K_peak=4 持续 4 小时/天且占全天 16.7% 时，C_amp ≈ 1.15-1.25（即实际成本比均值假设高 15%-25%），该系数需纳入 TCO 对比的修正项。

## Evidence

先验知识/题面给定，逻辑校验通过：基于线性带宽计费模型，峰值系数4持续16.7%时间，平均流量为基准流量的1.167倍，成本放大系数约1.17，落在1.15-1.25区间内，符合逻辑推导。
