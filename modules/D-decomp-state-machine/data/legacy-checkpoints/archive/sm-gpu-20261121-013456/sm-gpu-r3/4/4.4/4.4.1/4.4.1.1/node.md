# N204: A100 80GB PCIe 运行 Qwen3-27B FP8 时的实际吞吐量基准值，需注明是否启用 TensorRT-LLM 或 vLLM 的 FP8 模拟加

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83

## Claim

A100 80GB PCIe 运行 Qwen3-27B FP8 时的实际吞吐量基准值，需注明是否启用 TensorRT-LLM 或 vLLM 的 FP8 模拟加速，预期 35-45 tokens/s（低于原生 FP8 硬件如 H100）。

## Corrected Claim

A100 80GB PCIe 运行 Qwen3-27B 时，由于不支持原生 FP8 计算，通常采用 FP8 权重量化（计算仍为 BF16/INT8）或 INT8 W8A8 方案。其吞吐量显著低于 H100 原生 FP8 性能，具体数值取决于推理框架（如 vLLM）及量化策略，建议以实测为准，预期性能约为 H100 原生 FP8 的 60-70% 左右（定性描述）。

## Evidence

[质询]具体吞吐量数值（35-45 tokens/s）缺乏直接来源支持，且不同推理框架（vLLM/TensorRT-LLM）及具体配置下波动较大，单一数值区间可能不准确；此外，A100不支持原生FP8计算，'FP8模拟加速'的表述在技术实现上需更严谨（通常指权重量化为FP8但计算仍为BF16/INT8，或软件模拟，性能提升有限）。 | 来源[1][2]确认A100不支持原生FP8 W8A8，仅支持权重-only路径，且性能低于H100，逻辑自洽；但所有来源均未提供具体的35-45 tokens/s基准值，属于经验事实且缺直接来源支持。

## Search Query

A100 80GB Qwen3-27B FP8 inference throughput tokens per second TensorRT-LLM vLLM benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=aa9cd260f6083109421d10da626cf8e35468718ee875d8897eb1b2d94d06853e', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
- {'url': 'https://jishuzhan.net/article/2102237572693676033&rut=c5b603ce197bfb44bbe3ea04d927e61dbac099618a281f5516b0f24d7899f2e6', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选 - 技术栈'}
- {'url': 'https://blog.csdn.net/weixin_29045585/article/details/167203395&rut=f203e3e48ae1b12967d716df4d8e7a5754e31366b9a7cdb601dd1322433696a3', 'type': 'ddg', 'title': 'Qwen 3.8 27B 在 A100 上的推理 Baseline 实践指南 - CSDN博客'}
