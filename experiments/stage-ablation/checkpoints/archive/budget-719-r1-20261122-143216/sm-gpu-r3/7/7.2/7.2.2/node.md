# N369: Intel Gaudi 2/3 在 HuggingFace Transformers 中的原生支持状态为 'Partial'，主要依赖 ONNX 转换或专用算子

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

Intel Gaudi 2/3 在 HuggingFace Transformers 中的原生支持状态为 'Partial'，主要依赖 ONNX 转换或专用算子，缺乏针对 Qwen3 架构的 FlashAttention-2 优化内核，导致推理吞吐量比 CUDA 栈低 30-50%，需查阅 HuggingFace 官方文档或 Intel 社区论坛确认具体性能差距数据。

## Corrected Claim

Intel Gaudi 2/3 在 HuggingFace Transformers 中的原生支持状态可能为 'Partial'，主要依赖 ONNX 转换或专用算子，可能缺乏针对特定架构（如 Qwen3）的 FlashAttention-2 优化内核，导致推理吞吐量可能比 CUDA 栈低，具体性能差距需查阅 HuggingFace 官方文档或 Intel 社区论坛确认。

## Evidence

[质询]具体数值（30-50%）和特定架构（Qwen3）的优化状态属于经验事实，缺乏来源支持，且'Partial'状态的具体定义和性能差距可能随软件版本更新而变化，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Intel Gaudi 2 3 HuggingFace Transformers Qwen3 performance benchmark CUDA comparison
