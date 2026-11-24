# N145: 自建节点边缘处理延迟 T_edge_processing_self 的硬件瓶颈分析：在 2x Xeon Gold 6338 + 512GB RAM 配置下，单核

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

自建节点边缘处理延迟 T_edge_processing_self 的硬件瓶颈分析：在 2x Xeon Gold 6338 + 512GB RAM 配置下，单核处理 QPS 上限约为 50,000 req/s；当单 POP 峰值 QPS 超过 20,000 时，CPU 上下文切换和内存带宽竞争导致 T_edge_processing 从基准 15ms 上升至 30-50ms；该延迟增加直接贡献于 P99 尾延迟。

## Corrected Claim

在 2x Xeon Gold 6338 + 512GB RAM 配置下，单核处理 QPS 上限约为 50,000 req/s（视具体业务逻辑而定）；当单 POP 峰值 QPS 超过 20,000 时，CPU 上下文切换和内存带宽竞争可能导致 T_edge_processing 从基准 15ms 上升至 30-50ms；该延迟增加直接贡献于 P99 尾延迟。

## Evidence

[质询]具体数值（50,000 req/s 上限、15ms 基准、30-50ms 峰值）属于特定负载下的经验性能数据，缺乏通用性，且未指明具体处理逻辑（如仅转发 vs 复杂计算），不同实现下差异巨大。 | 先验知识/题面给定，逻辑校验通过：高并发下 CPU 上下文切换和内存带宽竞争确实会导致延迟上升，量级符合工程直觉，但具体数值为经验估计，无外部来源直接支持。

## Search Query

Xeon Gold 6338 single core QPS limit context switch latency high load
