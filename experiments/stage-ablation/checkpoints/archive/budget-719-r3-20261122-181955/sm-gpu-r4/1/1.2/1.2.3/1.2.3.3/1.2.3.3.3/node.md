# N467: Qwen3-27B 在 FP8 量化下的 MMLU 基准测试得分损失约为 0.8%（相对于 BF16 基线），满足 <2% 的质量损失阈值，来源：Qwen 官方

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N158

## Claim

Qwen3-27B 在 FP8 量化下的 MMLU 基准测试得分损失约为 0.8%（相对于 BF16 基线），满足 <2% 的质量损失阈值，来源：Qwen 官方技术报告附录及第三方量化评估（如 GPTQ/AWQ 对比数据）

## Corrected Claim

Qwen3-27B 在 FP8 量化下的 MMLU 基准测试得分损失通常小于 2%，具体数值取决于量化算法与校准数据。

## Evidence

[质询]具体数值（0.8%）属于经验事实，且不同量化算法（GPTQ vs AWQ）及校准数据集可能导致结果差异，缺乏具体来源支持该精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 quantization MMLU benchmark accuracy loss
