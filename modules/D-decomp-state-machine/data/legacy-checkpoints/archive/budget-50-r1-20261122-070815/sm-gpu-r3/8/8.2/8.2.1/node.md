# N401: llama.cpp 在 Metal 后端对 Qwen3 混合注意力架构（Linear Attention + Full Attention）的支持情况：截至 2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139

## Claim

llama.cpp 在 Metal 后端对 Qwen3 混合注意力架构（Linear Attention + Full Attention）的支持情况：截至 2024 年底，llama.cpp 尚未原生支持 Qwen3 的线性注意力层，需将其降级为全注意力处理或报错；若降级处理，KV Cache 占用将从 ~2GB 增加至 ~4-5GB（因所有层均存储 KV），且计算复杂度增加，导致实际 decode 速度下降 15-25%。

## Corrected Claim

llama.cpp 在 Metal 后端对 Qwen3 混合注意力架构的支持情况随版本更新而变化。若未原生支持线性注意力层而将其降级为全注意力处理，KV Cache 占用和计算复杂度将显著增加，导致内存占用上升和 decode 速度下降，具体数值取决于模型规模、序列长度及硬件环境。

## Evidence

[质询]该陈述包含具体的性能量化数据（KV Cache 增加至 4-5GB，速度下降 15-25%），这些数值高度依赖于具体的模型尺寸（如 7B/14B/32B）、序列长度、硬件配置及 llama.cpp 的具体版本实现细节，属于经验事实而非第一性原理可推导的通用结论。此外，Qwen3 的混合注意力架构在 llama.cpp 中的具体支持状态（是报错、自动降级还是部分支持）随版本更新变化极快，2024 年底的静态描述可能已不准确或过于绝对。 | 逻辑上，将线性注意力降级为全注意力确实会导致 KV Cache 存储量增加（从仅存储线性状态变为存储所有层的 K/V）和计算量增加，定性趋势合理；但具体数值（4-5GB, 15-25%）缺乏来源支持且依赖具体配置，属于经验事实，无法仅凭逻辑验证其精确性，故降级。

## Search Query

llama.cpp Metal backend Qwen3 hybrid attention linear attention support status
