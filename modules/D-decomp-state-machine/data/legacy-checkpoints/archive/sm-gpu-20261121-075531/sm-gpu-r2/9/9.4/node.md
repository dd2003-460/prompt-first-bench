# N120: H100 80GB SXM 与 H100 80GB PCIe 版本在 27B 模型 FP8/INT8 推理下的性能差距及能效比差异，特别是 FP8 Tensor

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33, N34

## Claim

H100 80GB SXM 与 H100 80GB PCIe 版本在 27B 模型 FP8/INT8 推理下的性能差距及能效比差异，特别是 FP8 Tensor Core 利用率对 PCIe 版带宽瓶颈的影响量化。

## Corrected Claim

H100 80GB SXM 与 PCIe 版本在 27B 模型 FP8/INT8 推理下存在性能与能效差异，主要受限于 PCIe 版本的内存带宽瓶颈，但具体量化差距及 FP8 Tensor Core 利用率影响需参考包含 PCIe 版本实测数据的专项基准测试。

## Evidence

[质询]参考来源仅涵盖 H100 SXM 版本的规格与基准测试，完全缺失 H100 PCIe 版本的数据，且未提供针对 27B 模型在 FP8/INT8 精度下的具体量化对比（如具体的 TFLOPS 利用率百分比或能效比数值），无法直接支持陈述中关于‘量化差距’和‘FP8 Tensor Core 利用率对 PCIe 版带宽瓶颈影响’的具体结论。 | 来源 [1][2][3] 仅确认了 H100 SXM 的硬件规格（80GB HBM3, 3.35 TB/s, FP8 算力），未包含 PCIe 版本对比或特定模型推理的量化性能差距数据，属于经验事实且缺乏直接来源支持。

## Search Query

H100 SXM vs PCIe FP8 inference benchmark performance gap

## Retrieval Sources

- {'url': 'https://awesomeagents.ai/hardware/nvidia-h100/&rut=18f9c324643d59f00a52590199ce39305d63802fa82b8b515167bb2eddbccce1', 'type': 'ddg', 'title': 'NVIDIA H100 SXM - The AI Training Benchmark | Awesome Agents'}
- {'url': 'https://inferencex.semianalysis.com/chips/h100&rut=6288999ef3b04c4335f2b673fee144f9b1eb96492fdfd67f32bbcbb9abd5b818', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs: ~$1.17/hr, 80 GB HBM3 | InferenceX'}
- {'url': 'https://infervisor.ai/gpus/nvidia-h100&rut=8034e7932c0d6525c6026de93720bb1f125e71add2a6fb7ad8e95c2da8472c36', 'type': 'ddg', 'title': 'NVIDIA H100 SXM for LLM inference: specs and measured results'}
