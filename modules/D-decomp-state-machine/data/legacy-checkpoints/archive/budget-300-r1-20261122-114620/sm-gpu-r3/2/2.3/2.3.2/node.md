# N63: Intel Arc A770 在 vLLM 或 llama.cpp 中的官方支持状态：截至 2024 年，vLLM 不支持 Intel Arc (XPU 后端)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

Intel Arc A770 在 vLLM 或 llama.cpp 中的官方支持状态：截至 2024 年，vLLM 不支持 Intel Arc (XPU 后端)，llama.cpp 支持但性能优化程度低于 NVIDIA CUDA，实测吞吐通常仅为同显存 NVIDIA 卡的 50-70% [待核验]

## Corrected Claim

截至 2024 年，vLLM 对 Intel Arc (XPU 后端) 的支持尚不成熟或处于实验阶段，llama.cpp 已提供 Intel Arc 支持，但其性能优化程度通常低于 NVIDIA CUDA 平台，实测吞吐往往低于同显存 NVIDIA 显卡。

## Evidence

[质询]具体数值区间（50-70%）缺乏统一基准，且随模型大小、序列长度及驱动版本波动极大，属于高度依赖具体测试环境的经验数据，难以作为固定事实陈述。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能比值为经验数据，无法从第一性原理严格推出）

## Search Query

Intel Arc A770 vLLM llama.cpp inference performance benchmark 2024
