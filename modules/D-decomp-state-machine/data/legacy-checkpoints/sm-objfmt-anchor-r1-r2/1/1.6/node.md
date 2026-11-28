# N11: 架构兼容性约束：消费级 GPU (RTX 系列) 主要支持 CUDA 生态，适合 vLLM/TGI 等主流推理框架；Apple Silicon (Metal) 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

架构兼容性约束：消费级 GPU (RTX 系列) 主要支持 CUDA 生态，适合 vLLM/TGI 等主流推理框架；Apple Silicon (Metal) 需使用 MLX 或 llama.cpp Metal backend，软件栈成熟度略低于 CUDA；老旧数据中心卡 (P40/V100) 需确认驱动对新框架的支持情况。

## Corrected Claim

架构兼容性约束：消费级 GPU (RTX 系列) 主要支持 CUDA 生态，适合 vLLM/TGI 等主流推理框架；Apple Silicon (Metal) 需使用 MLX 或 llama.cpp Metal backend，软件栈成熟度略低于 CUDA；老旧数据中心卡 (P40/V100) 需确认驱动对新框架的支持情况。

## Evidence

先验知识/题面给定，逻辑校验通过
