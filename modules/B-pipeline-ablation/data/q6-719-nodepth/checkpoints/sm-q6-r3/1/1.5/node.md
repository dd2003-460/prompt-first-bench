# N10: 源站回源延迟 (T_origin) = RTT_to_origin + T_processing + T_transfer，其中 T_transfer = Ob

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

源站回源延迟 (T_origin) = RTT_to_origin + T_processing + T_transfer，其中 T_transfer = Object_Size / Bandwidth_to_origin，Object_Size 由均对象大小 s 决定。

## Corrected Claim

源站回源延迟 (T_origin) = RTT_to_origin + T_processing + T_transfer，其中 T_transfer = Object_Size / Bandwidth_to_origin，Object_Size 由均对象大小 s 决定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的 RTT_to_origin、T_processing 和 T_transfer 三个独立分量，逻辑上互不重叠（正交），且完整覆盖了公式的所有组成部分（完备）。各子节点描述的是不同物理/逻辑层面的延迟因素，不存在多个子节点仅作为同一参数不同取值的情况（无冗余）。）

## Search Query

CDN origin fetch latency components
