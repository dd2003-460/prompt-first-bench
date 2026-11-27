# N310: 针对 Qwen3-27B INT4 量化质量风险，修正方案为构建混合校准集：其中代码类样本（如 HumanEval/MBPP 子集）占比需 >= 30%，数学类

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

针对 Qwen3-27B INT4 量化质量风险，修正方案为构建混合校准集：其中代码类样本（如 HumanEval/MBPP 子集）占比需 >= 30%，数学类样本（如 GSM8K 子集）占比需 >= 20%，通用文本占比 <= 50%；在此配比下，特定领域 Q_score 可维持在不低于 0.88 的水平。

## Corrected Claim

针对 Qwen3-27B INT4 量化质量风险，建议构建包含代码（如 HumanEval/MBPP）和数学（如 GSM8K）样本的混合校准集以提升特定领域表现，具体占比需根据实际评估结果调整，以确保 Q_score 满足业务需求。

## Evidence

[质询]该陈述包含具体的经验性阈值（代码>=30%, 数学>=20%, Q_score>=0.88），这些数值并非第一性原理可推导，且缺乏公开文献或官方文档支持其作为通用标准或特定模型（Qwen3-27B）的既定事实，属于未经证实的经验参数。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体配比与分数阈值无法从第一性原理推出）

## Search Query

LLM quantization calibration dataset composition ratio code math general text Qwen3 27B
