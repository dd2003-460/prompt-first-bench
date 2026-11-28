# N12: V100不支持FP8原生指令，vLLM中fp8 KV cache需在CPU端或通过软件模拟进行量化/反量化，额外增加约5-10%的内存访问开销，且无法利用Ten

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

V100不支持FP8原生指令，vLLM中fp8 KV cache需在CPU端或通过软件模拟进行量化/反量化，额外增加约5-10%的内存访问开销，且无法利用Tensor Core加速FP8 GEMM，导致推理吞吐相比A100/H100下降约40-60%。

## Corrected Claim

V100不支持FP8原生指令，vLLM中fp8 KV cache需在CPU端或通过软件模拟进行量化/反量化，额外增加内存访问开销，且无法利用Tensor Core加速FP8 GEMM，导致推理吞吐相比A100/H100显著下降。

## Evidence

[质询]数值量级存疑：V100不支持FP8是事实，但'推理吞吐相比A100/H100下降约40-60%'这一具体百分比缺乏普遍适用性，实际性能差距高度依赖于模型架构、序列长度及具体工作负载，通常V100与H100在LLM推理上的差距远超此范围（往往数倍），且'5-10%内存访问开销'的具体数值也缺乏通用基准支持。 | 先验知识/题面给定，逻辑校验通过：V100确实不支持FP8原生指令，需软件模拟，这会导致额外开销和无法利用Tensor Core加速FP8 GEMM，逻辑自洽；但具体的性能下降百分比（40-60%）和内存开销（5-10%）属于经验事实，在无外部来源支持的情况下，虽逻辑方向正确，但具体数值缺乏严谨支撑，故降级。

## Search Query

V100 FP8 support emulation overhead
