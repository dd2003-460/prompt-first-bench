# N303: 推理引擎（如 vLLM/TensorRT-LLM）的系统固定显存开销 (Overhead) 估算：包括 CUDA Context、Workspace、Atten

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

推理引擎（如 vLLM/TensorRT-LLM）的系统固定显存开销 (Overhead) 估算：包括 CUDA Context、Workspace、Attention 中间缓冲等，通常占据 1-2 GB 显存，不随 Batch Size 线性增长但会减少可用于 KV Cache 的余量。

## Corrected Claim

推理引擎（如 vLLM/TensorRT-LLM）的系统固定显存开销 (Overhead) 估算：包括 CUDA Context、Workspace、Attention 中间缓冲等，通常占据 1-2 GB 显存，不随 Batch Size 线性增长但会减少可用于 KV Cache 的余量。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM fixed memory overhead CUDA context workspace size
