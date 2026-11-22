# N415: vLLM在RTX 4090上对Qwen3-27B INT8的KV Cache管理采用PagedAttention，其内存碎片化率（Fragmentation R

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N149

## Claim

vLLM在RTX 4090上对Qwen3-27B INT8的KV Cache管理采用PagedAttention，其内存碎片化率（Fragmentation Ratio）在32K长上下文下约为5-8%，导致有效可用显存减少约2-3GB，进而使实际可支持的Max Batch Size从理论值2降至1，这是实测吞吐率低于理论带宽上限的主要非计算因素。

## Corrected Claim

vLLM在RTX 4090上对Qwen3-27B INT8的KV Cache管理采用PagedAttention，在32K长上下文下，内存碎片化和KV Cache占用会导致有效可用显存减少，进而可能使实际可支持的Max Batch Size低于理论值，这是实测吞吐率低于理论带宽上限的非计算因素之一。

## Evidence

[质询]该陈述包含多个具体的经验性数值（碎片化率5-8%、显存减少2-3GB、Batch Size从2降至1），这些数值高度依赖于具体的vLLM版本、Qwen3-27B的精确架构参数（如层数、头数、head_dim）以及RTX 4090的显存管理策略，无法从第一性原理严格推导，且不同配置下结果可能显著不同。 | source=knowledge，逻辑自洽（PagedAttention确实存在碎片化，长上下文下KV Cache占用大，显存受限会降低Batch Size），但具体数值缺乏来源支持，属于经验事实，降级为定性表述。
