# N163: D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策略选择主要由带宽单价决定；当 s < 500KB 时，C_request（请求次数计费）占比上升，公有云按请求计费的劣势凸显

## Corrected Claim

D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策略选择主要由带宽单价决定；当 s < 500KB 时，C_request（请求次数计费）占比上升，公有云按请求计费的劣势凸显

## Evidence

先验知识/题面给定，逻辑校验通过：带宽成本与对象大小成正比，请求成本固定，因此大对象（>2MB）带宽占比高，小对象（<500KB）请求占比高，符合云计算计费基本逻辑。
