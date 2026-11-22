# N153: A100 80GB SXM4 在 FP8 量化下运行 Qwen3-27B 时，由于 A100 架构 (Ampere) 缺乏原生 FP8 张量核心支持，FP8 权

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37, N38, N39

## Claim

A100 80GB SXM4 在 FP8 量化下运行 Qwen3-27B 时，由于 A100 架构 (Ampere) 缺乏原生 FP8 张量核心支持，FP8 权重需反量化为 BF16 或 INT8 进行计算，导致实际计算吞吐相比 H100 降低的具体比例（通常认为 Ampere 架构处理 FP8 数据需额外转换开销，性能损失约 20-30% 相比原生 FP8 支持架构）

## Corrected Claim

A100 80GB SXM4 在 FP8 量化下运行 Qwen3-27B 时，由于 A100 架构 (Ampere) 缺乏原生 FP8 张量核心支持，FP8 权重需反量化为 BF16 或 INT8 进行计算，导致实际计算吞吐相比 H100 存在显著降低（具体比例取决于软件栈优化程度，通常认为存在额外转换开销）。

## Evidence

[质询]具体数值比例（20-30%）缺乏严谨基准测试支持，且实际性能损失高度依赖于算子实现（如是否使用CUDA Core模拟FP8或仅做权重存储优化），不同框架（vLLM/TensorRT-LLM）下差异巨大，该区间过于武断。 | 先验知识/题面给定，逻辑校验通过：A100确实无原生FP8 Tensor Core，需反量化或模拟，存在额外开销，但具体20-30%的损失比例属于经验估计，缺乏统一标准，故降级为定性表述。
