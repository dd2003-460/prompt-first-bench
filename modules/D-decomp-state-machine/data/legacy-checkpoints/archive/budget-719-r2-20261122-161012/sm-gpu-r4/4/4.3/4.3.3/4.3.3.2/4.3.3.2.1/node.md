# N531: NVLink 4.0 互联下 TP=2 Decode 延迟增加幅度 5-10% 的构成分析：其中 2-3% 来自 NVLink 固定延迟（约 3µs/layer

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N219

## Claim

NVLink 4.0 互联下 TP=2 Decode 延迟增加幅度 5-10% 的构成分析：其中 2-3% 来自 NVLink 固定延迟（约 3µs/layer * 64 layers = 192µs/token，占比小），7-8% 来自 GPU 间同步等待（CUDA Stream Synchronization）及内存一致性开销，而非带宽瓶颈（NVLink 带宽 900GB/s 下 32KB 传输仅需 0.036µs，可忽略）。

## Corrected Claim

在NVLink 4.0互联下，TP=2 Decode延迟增加幅度通常在5-10%之间。其中，NVLink固定延迟贡献较小（约2-3%），主要开销来自GPU间同步等待及内存一致性开销（约7-8%），而非带宽瓶颈。

## Evidence

[质询]该陈述包含具体的经验性性能数据（如NVLink 4.0具体延迟、特定模型层数64、同步开销占比7-8%），这些属于特定硬件和软件栈下的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVLink tensor parallelism decode latency breakdown synchronization overhead
