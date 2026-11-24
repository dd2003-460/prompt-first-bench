# N163: D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策略选择主要由带宽单价决定；当 s < 500KB 时，C_request（请求次数计费）占比上升，公有云按请求计费的劣势凸显

## Corrected Claim

D2 成本排序中的带宽成本主导性判断：当平均对象大小 s > 2MB 时，C_bandwidth / C_total_per_1000req > 0.6，此时策略选择主要由带宽单价决定；当 s < 500KB 时，C_request（请求次数计费）占比上升，公有云按请求计费的劣势凸显

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中定义的两个关键阈值区间（s < 500KB 和 s > 2MB），选取了典型工作点（0.5MB 和 5MB）进行具体量化分析。两者在对象大小维度上互斥，在成本主导因素（请求计费 vs 带宽计费）上逻辑对立且互补，无重复或矛盾。虽然 0.5MB 略大于父节点定义的 500KB 边界，但作为'小对象'的代表性工作点符合上下文语境，且未覆盖中间区间（0.5MB-2MB）属于合理简化，因为父节点主要关注两端的主导性判断，中间区间通常被视为过渡区或非极端主导区。）
