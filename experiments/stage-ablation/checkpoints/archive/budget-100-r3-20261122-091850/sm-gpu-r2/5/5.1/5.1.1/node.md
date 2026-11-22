# N84: NVIDIA CUDA 生态兼容性：Qwen3-27B 在 vLLM/llama.cpp 中通过 CUDA 后端运行，支持 BF16/FP8/INT8/W4 全

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N24

## Claim

NVIDIA CUDA 生态兼容性：Qwen3-27B 在 vLLM/llama.cpp 中通过 CUDA 后端运行，支持 BF16/FP8/INT8/W4 全精度；CUDA 12.x 对 Ada Lovelace (4090) 和 Hopper (H100) 提供原生 FP8 加速，性能基准测试显示 CUDA 路径比 ROCm 路径快 10-20% [待核验]。

## Corrected Claim

NVIDIA CUDA 生态兼容性：Qwen3-27B 在 vLLM/llama.cpp 中通过 CUDA 后端运行，支持 BF16/FP8/INT8/W4 全精度；CUDA 12.x 对 Ada Lovelace (4090) 和 Hopper (H100) 提供原生 FP8 加速。

## Evidence

[质询]「CUDA 路径比 ROCm 路径快 10-20%」这一具体性能基准数据缺乏通用性，实际性能差异高度依赖于具体模型架构、序列长度、批处理大小及软件栈版本，且 ROCm 在部分场景下可能持平甚至反超，该固定百分比区间属于过度简化的经验断言。 | 先验知识/题面给定，逻辑校验通过：CUDA 对 Ada/Hopper 架构的原生 FP8 支持及 vLLM/llama.cpp 的兼容性符合技术事实，但具体性能对比数值缺乏来源支持且存在场景依赖性，故降级。

## Search Query

Qwen3 vLLM CUDA performance benchmark FP8
