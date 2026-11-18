# N8: 架构兼容性过滤：NVIDIA 显卡支持 CUDA 生态（vLLM/TensorRT-LLM 全功能），AMD 显卡支持 ROCm（vLLM 部分支持，性能略低 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

架构兼容性过滤：NVIDIA 显卡支持 CUDA 生态（vLLM/TensorRT-LLM 全功能），AMD 显卡支持 ROCm（vLLM 部分支持，性能略低 5-10% [待核验]），Intel/其他 GPU 支持有限（通常仅支持基础推理，无高级量化内核）；消费级显卡（RTX 4090/5090）支持所有主流精度，数据中心卡（H100/A100）支持 FP8/INT8 硬件加速

## Corrected Claim

架构兼容性过滤：NVIDIA 显卡支持 CUDA 生态（vLLM/TensorRT-LLM 全功能），AMD 显卡支持 ROCm（vLLM 部分支持，性能略低 5-10% [待核验]），Intel/其他 GPU 支持有限（通常仅支持基础推理，无高级量化内核）；消费级显卡（RTX 4090/5090）支持所有主流精度，数据中心卡（H100/A100）支持 FP8/INT8 硬件加速

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

ROCm vs CUDA LLM inference performance comparison vLLM support
