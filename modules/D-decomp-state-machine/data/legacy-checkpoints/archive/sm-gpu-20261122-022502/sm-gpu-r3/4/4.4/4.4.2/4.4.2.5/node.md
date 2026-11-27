# N220: 1×A100 80GB 若采用 FP8 量化（权重+激活），理论上可提升吞吐量至 15-20 tokens/s 并降低 TCO/Throughput 至 $0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70, N71, N72

## Claim

1×A100 80GB 若采用 FP8 量化（权重+激活），理论上可提升吞吐量至 15-20 tokens/s 并降低 TCO/Throughput 至 $0.015-$0.018/token，但 A100 对 FP8 的支持依赖特定软件栈（如 TensorRT-LLM 或 vLLM 的 FP8 实现），兼容性不如 BF16，且质量损失通常略高于 BF16（MMLU 下降约 2-3%）。

## Corrected Claim

1×A100 80GB 若采用 FP8 量化（权重+激活），在特定软件栈（如 TensorRT-LLM 或 vLLM）支持下，理论上可提升吞吐量并降低 TCO/Throughput，但 A100 对 FP8 的支持依赖软件实现而非原生硬件加速，兼容性不如 BF16，且质量损失通常略高于 BF16（具体 MMLU 下降幅度视模型而定，常见范围约 2-3%）。

## Evidence

[质询]A100 (Ampere架构) 硬件原生不支持 FP8 计算指令（FP8 支持始于 Hopper 架构 H100），所谓 'A100 采用 FP8 量化' 通常指存储/传输层面的量化或软件模拟，其吞吐量提升幅度（15-20 tokens/s）和 TCO 降低幅度高度依赖具体模型规模、序列长度及软件栈优化程度，属于经验性工程数据而非固定物理常数，且 'MMLU 下降 2-3%' 为特定模型下的统计结果，缺乏普适性。 | 先验知识/题面给定，逻辑校验通过：A100 确实缺乏原生 FP8 硬件加速，FP8 在 A100 上的实现主要依赖软件栈（如 TensorRT-LLM 的 FP8 存储/计算模拟或 vLLM 的特定实现），性能提升和精度损失为经验性工程指标，量级合理但非绝对真理，故降级为定性表述。

## Search Query

A100 FP8 quantization Qwen3-27B throughput TCO quality loss
