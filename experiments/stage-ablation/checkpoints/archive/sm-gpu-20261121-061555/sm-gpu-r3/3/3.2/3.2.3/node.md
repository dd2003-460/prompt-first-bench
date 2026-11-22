# N81: SmoothQuant 通过迁移量化难度从激活值到权重（平滑因子 α），使得 W8A8 量化在消费级 GPU（如 RTX 4090）上的硬件加速效率比纯 PTQ

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

SmoothQuant 通过迁移量化难度从激活值到权重（平滑因子 α），使得 W8A8 量化在消费级 GPU（如 RTX 4090）上的硬件加速效率比纯 PTQ W8A8 高 20-40% [待核验]

## Corrected Claim

SmoothQuant 通过迁移量化难度从激活值到权重（平滑因子 α），使得 W8A8 量化在消费级 GPU（如 RTX 4090）上成为可行且高效的方案，相比传统 PTQ 方法在保持精度的同时显著提升了硬件加速效率（具体提升幅度视模型和实现而定）。

## Evidence

[质询]具体数值范围（20-40%）缺乏通用性，高度依赖模型架构、数据集及具体硬件驱动版本，且SmoothQuant的核心贡献通常被描述为‘使W8A8量化可行’或‘精度损失降低’，而非直接量化为‘比纯PTQ高20-40%效率’（纯PTQ在消费级GPU上往往因激活值离群值导致精度崩溃或需回退到W8A16，效率对比基准模糊）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体性能提升百分比属于特定实验结果，非第一性原理可推导）。

## Search Query

SmoothQuant W8A8 inference speedup vs PTQ
