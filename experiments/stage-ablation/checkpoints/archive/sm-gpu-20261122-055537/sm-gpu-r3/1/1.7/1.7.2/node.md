# N57: CUDA Context、cuBLAS workspace及vLLM/llama.cpp框架基础静态显存开销在RTX 4090上约为1.5-2.0GB，在L4上

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

CUDA Context、cuBLAS workspace及vLLM/llama.cpp框架基础静态显存开销在RTX 4090上约为1.5-2.0GB，在L4上约为1.0-1.5GB，该数值不随batch size或seq length线性变化，但受框架版本（如vLLM 0.4.x vs 0.5.x）影响存在±0.5GB波动。

## Corrected Claim

CUDA Context、cuBLAS workspace及vLLM/llama.cpp框架基础静态显存开销在RTX 4090上约为1.5-2.0GB，在L4上约为1.0-1.5GB，该数值不随batch size或seq length线性变化，但受框架版本（如vLLM 0.4.x vs 0.5.x）影响存在±0.5GB波动。

## Evidence

先验知识/题面给定，逻辑校验通过
