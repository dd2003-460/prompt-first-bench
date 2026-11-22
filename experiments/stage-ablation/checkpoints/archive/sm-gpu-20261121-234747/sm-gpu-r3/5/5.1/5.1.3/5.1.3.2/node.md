# N329: 2×RTX 4090 在 PCIe 4.0 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量为 24 tokens/s，通信开销占比约为 20

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

2×RTX 4090 在 PCIe 4.0 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量为 24 tokens/s，通信开销占比约为 20%，基于 NCCL 2.14 实测数据

## Corrected Claim

2×RTX 4090 在 PCIe 4.0 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量约为 24 tokens/s，通信开销占比约为 20%（基于特定 NCCL 版本实测，具体数值可能因软件栈而异）。

## Evidence

[质询]该陈述包含具体的硬件配置（2x RTX 4090）、软件版本（NCCL 2.14）及精确的性能指标（24 tokens/s, 20%开销），属于典型的经验事实。在缺乏任何参考来源支持的情况下，无法验证这些具体数值的准确性，且不同实现（如是否使用TensorRT-LLM、vLLM等）会导致结果差异巨大。 | 经验事实，逻辑自洽但缺来源支持。24 tokens/s 对于 27B 模型在消费级显卡上的 Decode 阶段是合理的量级（受限于显存带宽），20% 的通信开销在 PCIe 互联下也符合直觉，但具体数值无法通过第一性原理推导，且无外部来源佐证。

## Search Query

2x RTX 4090 PCIe Qwen3-27B BF16 throughput NCCL overhead
