# N213: AWQ 格式在 vLLM 中的吞吐量损失 < 5% 的前提是：vLLM 版本 ≥ 0.4.0 且启用了 PagedAttention；若使用旧版本或未启用特定优

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

AWQ 格式在 vLLM 中的吞吐量损失 < 5% 的前提是：vLLM 版本 ≥ 0.4.0 且启用了 PagedAttention；若使用旧版本或未启用特定优化，AWQ 的 dequantization 开销可能导致吞吐量下降至 10-15%，需具体版本对比 [待核验]。

## Corrected Claim

AWQ 格式在 vLLM 中的吞吐量表现受版本和优化策略（如 PagedAttention）影响显著；在较新版本且启用相关优化时，量化开销通常较低，但在旧版本或未优化配置下，反量化开销可能导致吞吐量明显下降，具体损失比例需根据实际部署环境进行基准测试。

## Evidence

[质询]具体数值阈值（<5% 和 10-15%）及特定版本界限（vLLM ≥ 0.4.0）属于经验性性能数据，缺乏通用性，且不同硬件、模型大小和负载下波动极大，无法作为绝对事实陈述。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能指标无法从第一性原理推导）。

## Search Query

vLLM AWQ throughput loss version dependency paged attention
