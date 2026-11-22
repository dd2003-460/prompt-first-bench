# N103: 在单流（Batch Size=1）场景下，SGLang 相比 vLLM 的吞吐优势主要源于调度优化，量化指标为：在 RTX 4090 上运行 Qwen3-27B

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

在单流（Batch Size=1）场景下，SGLang 相比 vLLM 的吞吐优势主要源于调度优化，量化指标为：在 RTX 4090 上运行 Qwen3-27B FP8 时，SGLang 的 Tokens/s 比 vLLM 高约 15%-25%（基于历史 LLaMA-70B 测试数据的线性外推，需针对 27B 模型重新验证）。

## Corrected Claim

在单流（Batch Size=1）场景下，SGLang 相比 vLLM 的吞吐优势主要源于调度优化。基于历史 LLaMA-70B 测试数据的线性外推，在 RTX 4090 上运行 Qwen3-27B FP8 时，SGLang 的 Tokens/s 预计比 vLLM 高约 15%-25%，但该数值为理论外推，实际性能需针对 27B 模型进行重新验证。

## Evidence

[质询]该陈述明确标注为“基于历史 LLaMA-70B 测试数据的线性外推”，且承认“需针对 27B 模型重新验证”。将 70B 模型的调度优势线性外推至 27B 模型在逻辑上存在显著风险，因为不同参数量级的模型在计算瓶颈（Compute-bound vs Memory-bound）和显存占用上差异巨大，调度优化的边际收益并非线性关系，且 15%-25% 的具体数值缺乏当前模型下的实证支持。 | 先验知识/题面给定，逻辑校验通过（陈述内部自洽，明确指出了外推性质和验证需求，无硬逻辑错误），但具体数值为未验证的外推结果，故降级。
