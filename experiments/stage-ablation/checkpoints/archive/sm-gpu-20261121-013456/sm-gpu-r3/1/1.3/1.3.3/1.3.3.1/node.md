# N151: RTX 4090 上 INT4 推理的反量化开销占比：在 vLLM 0.6.x 版本中，INT4 Dequantization 操作占 GPU 总计算时间的 1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

RTX 4090 上 INT4 推理的反量化开销占比：在 vLLM 0.6.x 版本中，INT4 Dequantization 操作占 GPU 总计算时间的 12-15%，导致实际吞吐量提升系数为 2.1x（相比 BF16），而非理论峰值 4x

## Corrected Claim

在 RTX 4090 上使用 vLLM（如 0.26 版本）进行 INT4 推理时，由于 kernel 启动配置等开销，实际吞吐量提升系数低于理论峰值 4x（具体数值随版本和模型而异，参考案例中未达理论值）。

## Evidence

[质询]版本不匹配：参考来源明确使用的是 vLLM 0.26 版本，而待核验事实声称是 vLLM 0.6.x 版本。不同版本的 vLLM 在 kernel 优化、调度策略及反量化实现上可能存在显著差异，导致具体的性能开销占比（12-15%）和吞吐量提升系数（2.1x）无法直接跨版本通用。 | 来源 [1] 证实了 INT4 量化在 RTX 4090 上因 kernel 启动配置问题导致速度提升低于理论预期（间接支持反量化/计算开销占比高的逻辑），但具体数值（12-15%, 2.1x）及特定版本号（0.6.x）缺乏直接证据支持，且来源版本为 0.26，存在版本差异风险。

## Search Query

RTX 4090 INT4 dequantization overhead vLLM benchmark

## Retrieval Sources

- {'url': 'https://github.com/muhos/vLLM-Artifact&rut=9022b58e8d704724f701bc39443a295529cf499679230de00c34a16f63d678ec', 'type': 'ddg', 'title': 'LLM inference on one RTX 4090 - GitHub'}
