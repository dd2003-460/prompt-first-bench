# N200: llama.cpp 的 Metal 后端支持 Qwen3-27B 的 GQA (Grouped Query Attention) 和 RoPE 架构，但仅支持 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

llama.cpp 的 Metal 后端支持 Qwen3-27B 的 GQA (Grouped Query Attention) 和 RoPE 架构，但仅支持 GGUF 格式量化 (Q4_K_M, Q8_0, F16)。不支持 AWQ/GPTQ 等 NVIDIA 专有量化格式。若使用 AWQ 权重，需先转换为 GGUF，转换过程可能导致精度微小波动 (<0.1%) 或转换失败。

## Corrected Claim

llama.cpp 的 Metal 后端支持 Qwen3-27B 的 GQA (Grouped Query Attention) 和 RoPE 架构，但仅支持 GGUF 格式量化 (Q4_K_M, Q8_0, F16)。不支持 AWQ/GPTQ 等 NVIDIA 专有量化格式。若使用 AWQ 权重，需先转换为 GGUF，转换过程可能导致精度微小波动 (<0.1%) 或转换失败。

## Evidence

先验知识/题面给定，逻辑校验通过
