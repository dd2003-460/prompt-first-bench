# N290: H100 PCIe 在 Qwen3-27B FP8 下的实测吞吐量为 85 tokens/s，BF16 为 45 tokens/s，提升系数为 1.89x（来源

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

H100 PCIe 在 Qwen3-27B FP8 下的实测吞吐量为 85 tokens/s，BF16 为 45 tokens/s，提升系数为 1.89x（来源：NVIDIA H100 Tensor Core 官方规格及 vLLM 0.4.0 基准测试）。

## Corrected Claim

H100 SXM 在 Qwen3-27B FP8 下的实测吞吐量约为 85 tokens/s（基于来源[1][2]的 SXM 数据），BF16 约为 45 tokens/s，提升系数约为 1.89x。H100 PCIe 版本因互联带宽差异，吞吐量可能略低于此数值。

## Evidence

[质询]硬件型号混淆：参考来源[1]和[2]明确测试的是 H100 SXM，而陈述声称是 H100 PCIe。虽然两者算力相近，但 PCIe 版本通常因带宽限制（PCIe 4.0/5.0 vs NVLink）在推理吞吐上略低于 SXM 版本，直接引用 SXM 数据作为 PCIe 的实测值存在口径偏差。此外，来源[3]虽提及 vLLM 和 H100，但未提供具体的 85 tokens/s 数值以直接支持该特定数值。 | 来源[1][2]提供了 H100 SXM 上 Qwen3.5-27B FP8 的基准测试，但未直接覆盖 H100 PCIe 的具体数值 85 tokens/s；逻辑上 FP8 相比 BF16 提升约 1.8-2 倍符合预期，但具体数值缺乏针对 PCIe 版本的直接来源支持，且存在 SXM/PCIe 硬件差异。

## Search Query

H100 PCIe Qwen3-27B FP8 inference throughput tokens per second benchmark

## Retrieval Sources

- {'url': 'https://cdn.millstoneai.cloud/benchmarks/qwen3-5-27b-fp8-1x-h100-sxm/qwen3-5-27b-fp8-1x-h100-sxm.pdf&rut=1cc974b68d3880cc54a3f607a2dbb16fb9ba43d519a4df77436d4a87d351c239', 'type': 'ddg', 'title': 'PDF Inference Benchmark - qwen3-5-27b-fp8 on 1x H100 SXM'}
- {'url': 'https://www.millstoneai.com/inference-benchmark/qwen3-5-27b-fp8-1x-h100-sxm&rut=209ed8e45c8008925fc25892f7715f557ac04515331430bd94a7aa063d1e800b', 'type': 'ddg', 'title': 'Qwen3.5-27B on 1x H100 SXM Benchmark — FP8 | Millstone AI'}
- {'url': 'https://markaicode.com/benchmarks/cuda-qwen-3-h100-latency-benchmark/&rut=87d8c24a7bb4935b5ee6f4eb22c1b112882c6779814ca2b915757b3efe7b66c8', 'type': 'ddg', 'title': 'Qwen3 H100 Benchmarks 2026: Real vLLM Throughput Data'}
