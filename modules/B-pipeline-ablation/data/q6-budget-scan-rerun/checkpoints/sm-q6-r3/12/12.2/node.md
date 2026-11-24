# N408: 故障期间受影响流量比例 F_affected 的精确计算：F_affected = geo_share_i × (1 - C_neighbor_capacity

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

故障期间受影响流量比例 F_affected 的精确计算：F_affected = geo_share_i × (1 - C_neighbor_capacity / B_fault_demand)，其中 geo_share_i 为第 i 个 POP 的地理流量占比（假设均匀分布则为 0.1），C_neighbor_capacity 为邻近 POP 剩余可用带宽，B_fault_demand 为故障 POP 需转移的带宽需求；若邻近 POP 容量不足，剩余流量回源，回源带宽成本按 N119 公式计算

## Corrected Claim

故障期间受影响流量比例 F_affected 的精确计算：F_affected = geo_share_i × (1 - C_neighbor_capacity / B_fault_demand)，其中 geo_share_i 为第 i 个 POP 的地理流量占比（假设均匀分布则为 0.1），C_neighbor_capacity 为邻近 POP 剩余可用带宽，B_fault_demand 为故障 POP 需转移的带宽需求；若邻近 POP 容量不足，剩余流量回源，回源带宽成本按 N119 公式计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN POP failover traffic redistribution neighbor capacity utilization
