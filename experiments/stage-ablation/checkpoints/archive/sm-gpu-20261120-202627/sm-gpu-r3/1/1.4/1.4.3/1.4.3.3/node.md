# N199: NVIDIA L40S 48GB 显卡运行 Qwen3-27B (FP8, 32K ctx) 的实测吞吐量基准值，需检索 vLLM 或 TensorRT-LLM

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

NVIDIA L40S 48GB 显卡运行 Qwen3-27B (FP8, 32K ctx) 的实测吞吐量基准值，需检索 vLLM 或 TensorRT-LLM 官方 benchmark 或社区实测数据，预期值在 30-50 tokens/s 区间

## Corrected Claim

NVIDIA L40S 48GB 显卡运行 Qwen3-27B (FP8, 32K ctx) 的吞吐量需依据具体推理框架（如 vLLM 或 TensorRT-LLM）及并发配置实测确定，预期值可能在数十 tokens/s 量级，但具体区间需参考官方 benchmark 或社区实测数据。

## Evidence

[质询]该陈述包含具体的硬件规格（L40S 48GB）、模型版本（Qwen3-27B）及性能指标（30-50 tokens/s），属于经验事实。由于缺乏官方或社区实测数据支持，且不同推理框架（vLLM vs TensorRT-LLM）、并发数及具体实现细节会导致吞吐量波动极大，仅凭逻辑推测无法确定该数值区间的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体吞吐量数值）

## Search Query

NVIDIA L40S 48GB Qwen3-27B FP8 inference throughput tokens per second benchmark
