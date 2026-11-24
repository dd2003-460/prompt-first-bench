# N99: 全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_proce

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_processing，其中 L_edge_self ≈ 5-10ms，H_self 为自建节点缓存命中率（受容量限制，通常 70-85%），需验证 L_p99_self ≤ 200ms。

## Corrected Claim

全自建策略 P99 延迟 L_p99_self = L_edge_self + L_backhaul_self * (1 - H_self) + L_processing，其中 L_edge_self ≈ 5-10ms，H_self 为自建节点缓存命中率（受容量限制，通常 70-85%），需验证 L_p99_self ≤ 200ms。

## Evidence

先验知识/题面给定，逻辑校验通过
