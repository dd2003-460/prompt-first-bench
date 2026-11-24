# N51: L_backhaul = L_propagation + L_transmission + L_origin_processing，其中 L_propagati

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

L_backhaul = L_propagation + L_transmission + L_origin_processing，其中 L_propagation = Distance / Speed_of_Light（光速传播延迟，~3ms/1000km），L_transmission = Object_Size / Bandwidth（传输延迟，1.5MB/100Mbps ≈ 120ms），L_origin_processing 为源站处理延迟（10-50ms）。

## Corrected Claim

L_backhaul = L_propagation + L_transmission + L_origin_processing，其中 L_propagation = Distance / Speed_of_Light（光速传播延迟，~3ms/1000km），L_transmission = Object_Size / Bandwidth（传输延迟，1.5MB/100Mbps ≈ 120ms），L_origin_processing 为源站处理延迟（10-50ms）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个独立分量（传播、传输、处理），物理机制和决定因素互不重叠（地理距离、带宽瓶颈、服务器负载），符合正交性；三者之和完整覆盖了回源延迟的构成，符合完备性；虽然涉及具体数值案例，但分别针对不同的物理层瓶颈，不属于同一参数的简单取值冗余。）

## Search Query

backhaul latency components propagation transmission origin server processing time
