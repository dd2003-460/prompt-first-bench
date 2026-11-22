# N59: NVIDIA H100 SXM (80GB) 推理性能基准：Qwen3-27B BF16 单卡吞吐 78 tokens/s (batch=1)，比 A100 高

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

NVIDIA H100 SXM (80GB) 推理性能基准：Qwen3-27B BF16 单卡吞吐 78 tokens/s (batch=1)，比 A100 高 50%；FP8 原生支持使量化吞吐达 112 tokens/s；HBM3 带宽 3.35 TB/s 是 A100 的 2.15x，直接提升 KV cache 读取速度

## Corrected Claim

NVIDIA H100 SXM (80GB) 在 Qwen3-27B BF16 单卡推理中通常显著优于 A100（约 50% 提升），FP8 支持可进一步提升吞吐；HBM3 带宽 3.35 TB/s 约为 A100 的 2.15 倍，有利于 KV cache 读取。

## Evidence

[质询]具体数值（78 tokens/s, 112 tokens/s）属于特定硬件与模型组合下的经验性能数据，受驱动版本、CUDA版本、推理框架（如vLLM/TensorRT-LLM）及具体实现细节影响极大，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 SXM Qwen3-27B FP8 inference benchmark HBM3 bandwidth
