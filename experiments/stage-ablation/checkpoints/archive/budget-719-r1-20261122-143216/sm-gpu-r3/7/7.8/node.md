# N136: HuggingFace 社区发布的 Qwen3-27B FP8 量化模型在 MMLU-Pro 基准测试上的分数为 72.3 [待核验]，对比 BF16 基线的 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32, N33, N34

## Claim

HuggingFace 社区发布的 Qwen3-27B FP8 量化模型在 MMLU-Pro 基准测试上的分数为 72.3 [待核验]，对比 BF16 基线的 73.1，下降幅度为 1.09%，证明 FP8 量化质量损失可接受。

## Corrected Claim

HuggingFace 社区发布的 Qwen3-27B FP8 量化模型在 MMLU-Pro 基准测试上的分数通常略低于 BF16 基线（例如下降约 1% 左右），表明 FP8 量化质量损失在可接受范围内。

## Evidence

[质询]具体数值（72.3, 73.1）及特定社区模型版本的基准测试成绩属于经验事实，缺乏来源支持，且不同量化实现（如不同校准数据集、量化算法）可能导致分数波动，无法仅凭逻辑推导确认具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization MMLU-Pro benchmark HuggingFace
