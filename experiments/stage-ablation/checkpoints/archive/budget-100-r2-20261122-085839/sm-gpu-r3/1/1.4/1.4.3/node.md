# N42: 框架支持矩阵：vLLM 0.4.x+ 和 SGLang 原生支持 FP8 KV Cache (需硬件支持 FP8 Tensor Core, 如 Ada/Hopp

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

框架支持矩阵：vLLM 0.4.x+ 和 SGLang 原生支持 FP8 KV Cache (需硬件支持 FP8 Tensor Core, 如 Ada/Hopper架构)，而 llama.cpp 支持 Q8_0/Q4_0 KV Cache 量化，但计算效率较低

## Corrected Claim

vLLM 和 SGLang 在较新版本中支持 FP8 KV Cache (需硬件支持 FP8 Tensor Core, 如 Ada/Hopper架构)，而 llama.cpp 支持 Q8_0/Q4_0 KV Cache 量化，但计算效率较低

## Evidence

[质询]具体版本号（vLLM 0.4.x+）和特定框架（SGLang）的FP8 KV Cache支持状态属于经验事实，且不同版本间可能存在差异，缺乏来源直接证实该精确版本界限。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM FP8 KV cache support Qwen3-27B
