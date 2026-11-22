# N245: AWQ 量化算法在 27B 参数规模上的校准数据集大小对量化精度的影响：使用 128 条 vs 512 条校准样本时，MMLU 准确率损失的差异约为 0.5%-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N84

## Claim

AWQ 量化算法在 27B 参数规模上的校准数据集大小对量化精度的影响：使用 128 条 vs 512 条校准样本时，MMLU 准确率损失的差异约为 0.5%-1.0%，需确认 Qwen3 官方推荐的校准集规模以最小化偏差。

## Corrected Claim

AWQ 量化算法在 27B 参数规模上，校准数据集大小（如 128 条 vs 512 条）通常会对量化精度产生一定影响，具体 MMLU 准确率损失差异需参考特定模型（如 Qwen3）的官方文档或实验数据以最小化偏差。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU准确率损失差异0.5%-1.0%）和特定模型（Qwen3）的推荐参数，属于经验事实。在缺乏任何参考来源支持的情况下，无法验证这些具体数值的准确性，且不同模型、不同量化位宽下该数值可能波动较大，存在将特定实验结果泛化为普遍规律的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值及Qwen3官方推荐）。

## Search Query

AWQ quantization calibration dataset size impact on MMLU accuracy 27B model
