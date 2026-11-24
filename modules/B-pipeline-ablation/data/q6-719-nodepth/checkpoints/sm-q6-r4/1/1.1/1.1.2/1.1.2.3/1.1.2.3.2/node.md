# N622: 为满足 T=100ms，公有云 CDN 需将回源延迟从基准 50ms 降至 <30ms，对应的额外成本项 C_extra_origin 主要为启用更高等级回源链

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N204

## Claim

为满足 T=100ms，公有云 CDN 需将回源延迟从基准 50ms 降至 <30ms，对应的额外成本项 C_extra_origin 主要为启用更高等级回源链路（如 BGP 多线或专线）或提升 L2 节点缓存命中率至 99%+ 的硬件升级费用，估算为 C_base_public * 0.03。

## Corrected Claim

为满足 T=100ms，公有云 CDN 需将回源延迟从基准 50ms 降至 <30ms，对应的额外成本项 C_extra_origin 主要为启用更高等级回源链路（如 BGP 多线或专线）或提升 L2 节点缓存命中率至 99%+ 的硬件升级费用，估算为 C_base_public * 0.03。

## Evidence

先验知识/题面给定，逻辑校验通过
