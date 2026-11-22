# N75: 1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，无需量化即可完整容纳权重与 KV Cache，实测吞吐量稳定在 18-22 t

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，无需量化即可完整容纳权重与 KV Cache，实测吞吐量稳定在 18-22 tokens/s，TCO/Throughput 为 $0.025-$0.030/token，其优势在于零量化误差和极高的长上下文稳定性（P99 延迟方差 < 5ms）。

## Corrected Claim

1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，理论上无需量化即可完整容纳权重与 KV Cache。具体吞吐量、TCO 及延迟稳定性需根据实际推理框架和负载情况实测确定，通常单卡 BF16 推理吞吐量在 10-30 tokens/s 范围内波动。

## Evidence

[质询]该陈述包含具体的硬件性能指标（吞吐量 18-22 tokens/s）、成本数据（$0.025-$0.030/token）及延迟方差（< 5ms），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证这些具体数值的准确性，且不同推理框架（如 vLLM, TGI）和配置下性能差异巨大，单一数值区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持。虽然 1x A100 80GB 在 BF16 下容纳 Qwen3-27B 权重（约 54GB）及 32K 上下文 KV Cache（约 10-15GB，取决于具体实现和 batch size）在容量上是可行的（总占用约 65-70GB < 80GB），但具体的吞吐量、TCO 和 P99 延迟方差属于依赖具体软件栈、硬件驱动及负载情况的经验数据，无来源佐证，故降级。

## Search Query

Qwen3 27B A100 80GB BF16 inference throughput 32k context
