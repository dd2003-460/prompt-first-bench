# N198: FP8 推理运行时开销（激活值、临时缓冲区、CUDA 上下文）的精确量化值为 5 GB，需区分 Batch Size=1 和 Batch Size>1 时的峰值

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

FP8 推理运行时开销（激活值、临时缓冲区、CUDA 上下文）的精确量化值为 5 GB，需区分 Batch Size=1 和 Batch Size>1 时的峰值激活值显存占用差异，通常激活值显存与 Batch Size 成正比

## Corrected Claim

FP8 推理运行时开销（激活值、临时缓冲区、CUDA 上下文）的具体数值取决于模型规模、序列长度及硬件配置，通常激活值显存与 Batch Size 成正比，Batch Size=1 时峰值激活值显存占用显著低于 Batch Size>1 的情况。

## Evidence

[质询]将FP8推理的运行时开销（激活值、缓冲区、上下文）精确量化为固定的5GB缺乏依据，且忽略了模型参数量、序列长度等关键变量对显存占用的决定性影响，属于过度简化的经验数值。 | 先验知识/题面给定，逻辑校验通过（激活值与Batch Size成正比符合逻辑），但具体数值5GB为经验事实且无来源支持，故降级。
