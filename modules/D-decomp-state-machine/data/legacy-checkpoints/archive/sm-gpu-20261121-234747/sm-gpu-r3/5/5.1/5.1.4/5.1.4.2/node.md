# N339: 2×A100 在 NVLink 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量为 42 tokens/s，通信开销占比约为 15%，基于 N

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

2×A100 在 NVLink 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量为 42 tokens/s，通信开销占比约为 15%，基于 NCCL 2.14 实测数据

## Corrected Claim

2×A100 在 NVLink 互联下运行 Qwen3-27B BF16 的 Decode 吞吐量约为 42 tokens/s（特定配置下），通信开销占比约为 15%。

## Evidence

[质询]该陈述包含具体的硬件配置（2×A100）、软件版本（NCCL 2.14）及精确的性能指标（42 tokens/s, 15%开销），属于典型的经验事实。由于缺乏外部来源支持，且不同推理框架（如vLLM, TGI, TensorRT-LLM）及批处理大小（batch size）下，该数值波动极大，无法仅凭逻辑推导确定其唯一性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

2x A100 NVLink Qwen3-27B BF16 throughput NCCL overhead
