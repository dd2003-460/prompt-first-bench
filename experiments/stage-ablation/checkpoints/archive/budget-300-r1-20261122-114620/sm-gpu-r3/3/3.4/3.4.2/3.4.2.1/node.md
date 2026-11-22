# N300: Qwen3-27B 在 4-bit 量化下，GSM8K Pass@1 准确率从 BF16 的 ~55% 下降至 ~40-45%，下降幅度约 10-15 个百分点

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N96

## Claim

Qwen3-27B 在 4-bit 量化下，GSM8K Pass@1 准确率从 BF16 的 ~55% 下降至 ~40-45%，下降幅度约 10-15 个百分点，主要归因于中间推理步骤中数值精度损失累积，导致多步逻辑链断裂。

## Corrected Claim

Qwen3-27B 在 4-bit 量化下，GSM8K Pass@1 准确率通常会出现一定程度的下降（具体幅度取决于量化算法和校准数据），主要归因于低比特表示导致的数值精度损失，可能影响多步推理的稳定性。

## Evidence

[质询]具体数值（~55%降至~40-45%）及归因（中间推理步骤数值精度损失累积）属于特定模型版本的经验性观察结果，缺乏通用理论支持，且不同量化方法（如GPTQ, AWQ, SmoothQuant）对精度的影响差异巨大，该陈述可能混淆了特定量化算法的效果与通用量化现象。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值与归因无法从第一性原理严格推出）

## Search Query

Qwen3-27B 4-bit quantization GSM8K Pass@1 accuracy drop mechanism
