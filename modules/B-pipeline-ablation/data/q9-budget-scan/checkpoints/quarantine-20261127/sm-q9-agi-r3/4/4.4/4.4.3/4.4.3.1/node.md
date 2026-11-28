# N209: MacBook M1 Max 运行 Llama-3-8B (INT8) 处理'文献摘要提取'任务的单次吞吐量为 15 tokens/sec，相比 27B 的 5

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

MacBook M1 Max 运行 Llama-3-8B (INT8) 处理'文献摘要提取'任务的单次吞吐量为 15 tokens/sec，相比 27B 的 5 tokens/sec 提升 3 倍，单次处理 500 tokens 摘要耗时从 100s 降至 33s，节省 67s 服务器时间。

## Corrected Claim

MacBook M1 Max 运行 Llama-3-8B (INT8) 处理'文献摘要提取'任务的单次吞吐量约为 15 tokens/sec（基于特定优化配置），相比 27B 模型的 5 tokens/sec 提升约 3 倍，单次处理 500 tokens 摘要耗时从 100s 降至 33s，节省 67s 服务器时间。

## Evidence

[质询]吞吐量数值（15 tokens/sec for 8B INT8 on M1 Max）属于特定硬件与软件栈下的经验性能指标，非第一性原理可推导；且M1 Max实际峰值内存带宽约400GB/s，8B INT8模型权重约8GB，理论极限吞吐远高于15 tokens/sec（通常可达30-50+ tokens/sec），该数值可能偏低或依赖特定低效实现，缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持；数值量级在合理范围内但未达理论上限，需具体基准测试佐证。

## Search Query

Llama-3-8B int8 m1 max inference speed tokens per second benchmark
