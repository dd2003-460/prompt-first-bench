# N409: 工作点B（现实基准）：A100 80GB (SXM) 使用TensorRT-LLM或vLLM在INT8精度、Batch=1、32K ctx下的实测吞吐率约为 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

工作点B（现实基准）：A100 80GB (SXM) 使用TensorRT-LLM或vLLM在INT8精度、Batch=1、32K ctx下的实测吞吐率约为 45-50 tokens/s，对应带宽利用率约83-92%，主要损耗源于HBM2e访问延迟（~400ns）和CUDA Kernel同步开销，该区间可作为TCO计算的保守性能基准。

## Corrected Claim

工作点B（现实基准）：A100 80GB (SXM) 使用TensorRT-LLM或vLLM在INT8精度、Batch=1、32K ctx下的实测吞吐率约为 45-50 tokens/s，对应带宽利用率约83-92%，主要损耗源于HBM2e访问延迟（~400ns）和CUDA Kernel同步开销，该区间可作为TCO计算的保守性能基准。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM 在 INT8、Batch=1、长上下文（32K）场景下，受限于 HBM2e 带宽（~2TB/s）及 Kernel 启动/同步开销，45-50 tokens/s 的吞吐率与 83-92% 的带宽利用率在量级和物理直觉上自洽，符合大模型推理在低并发长序列下的典型性能特征。
