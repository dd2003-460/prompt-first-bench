# N339: Qwen3-27B 在 Hugging Face 上发布的权重文件（safetensors）中，所有线性层权重（`weight`）的数据类型均为 `torch.

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N140

## Claim

Qwen3-27B 在 Hugging Face 上发布的权重文件（safetensors）中，所有线性层权重（`weight`）的数据类型均为 `torch.bfloat16`，未检测到 `float32` 或 `int8` 类型的权重张量；这意味着在加载到 GPU 时，初始权重显存占用严格等于 27.1e9 * 2 bytes = 54.2 GB，不存在因训练时混合精度导致的存储格式偏差。

## Corrected Claim

Qwen3-27B 在 Hugging Face 上发布的标准权重文件（safetensors）中，线性层权重通常以 bfloat16 格式存储，加载到 GPU 时的初始显存占用约为 54.2 GB（基于 27.1e9 参数估算），但具体数据类型和参数量需以实际文件元数据为准。

## Evidence

[质询]该陈述包含具体的经验性参数（如精确参数量 27.1e9、特定文件中的数据类型分布），这些无法从第一性原理推导，且检索无可用来源支持，存在因模型版本差异或量化选项导致事实不符的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B safetensors dtype bfloat16 check mixed precision
