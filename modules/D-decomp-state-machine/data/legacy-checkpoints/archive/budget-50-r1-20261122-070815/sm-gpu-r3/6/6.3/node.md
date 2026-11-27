# N129: 在 BF16 精度下，若 Qwen3-27B 为纯 GQA 全注意力模型，32K 上下文 KV Cache 显存占用精确计算为 2 (K+V) * 4 (hea

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

在 BF16 精度下，若 Qwen3-27B 为纯 GQA 全注意力模型，32K 上下文 KV Cache 显存占用精确计算为 2 (K+V) * 4 (heads) * 64 (layers) * 128 (dim) * 32768 (seq) * 2 (bytes) = 2,147,483,648 bytes ≈ 2.0 GB；若含线性层，需按比例折减

## Corrected Claim

在 BF16 精度下，若假设 Qwen3-27B 为纯 GQA 全注意力模型（参数：4 heads, 64 layers, 128 dim），32K 上下文 KV Cache 显存占用计算为 2.0 GB；但实际 Qwen3-27B 采用混合注意力机制，实际 KV Cache 占用需根据具体 GQA 层比例及线性层特性重新计算，通常低于纯全注意力模型。

## Evidence

[质询]Qwen3-27B 并非纯 GQA 全注意力模型，而是采用了混合注意力机制（包含 GQA 和线性注意力/SSM 层），且其具体架构参数（如层数、头数、维度）需依据官方技术报告确认，直接套用纯 GQA 全注意力假设会导致计算前提错误。 | 经验事实，逻辑自洽但缺来源支持；模型架构假设与已知 Qwen3 系列混合架构特性存在潜在冲突，无法通过第一性原理完全排除架构差异带来的误差。
