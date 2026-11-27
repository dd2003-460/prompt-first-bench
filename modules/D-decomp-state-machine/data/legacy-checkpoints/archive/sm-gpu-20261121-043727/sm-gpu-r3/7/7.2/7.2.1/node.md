# N240: NVIDIA H100 SXM 在 Qwen3-27B FP8 推理负载下的平均功耗实测值：检索 NVIDIA H100 功耗特性文档或数据中心实测数据，确定在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N90

## Claim

NVIDIA H100 SXM 在 Qwen3-27B FP8 推理负载下的平均功耗实测值：检索 NVIDIA H100 功耗特性文档或数据中心实测数据，确定在 32K 上下文、Batch Size 1 的 Decode 阶段，H100 的实际功耗通常在 TDP (700W) 的 50-70% 区间（约 350-490W），因为 Decode 阶段内存带宽受限导致计算单元空闲率较高，以修正年电费计算的负载因子

## Corrected Claim

NVIDIA H100 SXM 在 Qwen3-27B FP8 推理负载（32K 上下文、Batch Size 1 Decode 阶段）下，由于内存带宽受限导致计算单元空闲率较高，实际功耗通常显著低于 TDP (700W)，预计处于 50-70% 区间（约 350-490W），具体数值需依赖特定硬件监控实测。

## Evidence

[质询]参考来源主要提供吞吐量、延迟等性能指标，未直接提供具体的平均功耗实测数值（Watt），且模型版本存在细微差异（Qwen3.5 vs Qwen3），无法直接证实 350-490W 这一具体数值区间。 | 逻辑上 Decode 阶段受内存带宽限制，GPU 计算单元利用率低，功耗低于 TDP (700W) 符合物理直觉；来源 [1][2][3] 证实了 H100 SXM 运行该级别模型的场景，但未提供直接功耗数据，属于经验事实缺直接来源支持。

## Search Query

NVIDIA H100 SXM power consumption LLM inference decode phase average watts

## Retrieval Sources

- {'url': 'https://www.millstoneai.com/inference-benchmark/qwen3-5-27b-fp8-1x-h100-sxm&rut=209ed8e45c8008925fc25892f7715f557ac04515331430bd94a7aa063d1e800b', 'type': 'ddg', 'title': 'Qwen3.5-27B on 1x H100 SXM Benchmark — FP8 | Millstone AI'}
- {'url': 'https://cdn.millstoneai.cloud/benchmarks/qwen3-5-27b-fp8-1x-h100-sxm/qwen3-5-27b-fp8-1x-h100-sxm.pdf&rut=1cc974b68d3880cc54a3f607a2dbb16fb9ba43d519a4df77436d4a87d351c239', 'type': 'ddg', 'title': 'PDF Inference Benchmark - qwen3-5-27b-fp8 on 1x H100 SXM'}
- {'url': 'https://infervisor.ai/gpus/nvidia-h100&rut=8034e7932c0d6525c6026de93720bb1f125e71add2a6fb7ad8e95c2da8472c36', 'type': 'ddg', 'title': 'NVIDIA H100 SXM for LLM inference: specs and measured results'}
