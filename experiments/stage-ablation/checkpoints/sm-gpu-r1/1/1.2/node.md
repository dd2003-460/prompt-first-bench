# N7: 架构兼容性排除：排除不支持当前主流量化格式（如AWQ/GPTQ/FP8）或缺乏CUDA加速库支持的老旧架构（如Pascal/Maxwell），以及非NVIDIA

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

架构兼容性排除：排除不支持当前主流量化格式（如AWQ/GPTQ/FP8）或缺乏CUDA加速库支持的老旧架构（如Pascal/Maxwell），以及非NVIDIA生态中驱动成熟度不足导致推理框架（vLLM/llama.cpp）性能损失>30%的异构方案（如早期AMD MI系列、Intel Arc），除非其TCO优势>50%。

## Corrected Claim

架构兼容性排除：排除不支持当前主流量化格式（如AWQ/GPTQ/FP8）或缺乏CUDA加速库支持的老旧架构（如Pascal/Maxwell），以及非NVIDIA生态中驱动成熟度不足导致推理框架（vLLM/llama.cpp）性能损失>30%的异构方案（如早期AMD MI系列、Intel Arc），除非其TCO优势>50%。

## Evidence

先验知识/题面给定，逻辑校验通过
