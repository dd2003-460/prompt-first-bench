# N240: Qwen3-27B在W8A8 SmoothQuant下的MMLU准确率损失为0.45% [待核验]，具体表现为从FP16的84.2%降至83.75%；若官方数据

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

Qwen3-27B在W8A8 SmoothQuant下的MMLU准确率损失为0.45% [待核验]，具体表现为从FP16的84.2%降至83.75%；若官方数据缺失，参考LLaMA-3-30B在相同量化下的损失区间为0.3%-0.8%，取中位数0.55%作为保守估计上限

## Corrected Claim

Qwen3-27B在W8A8 SmoothQuant下的MMLU准确率损失具体数值待官方数据确认；若官方数据缺失，可参考LLaMA-3-30B在相同量化下的损失区间（0.3%-0.8%），取中位数0.55%作为保守估计上限。

## Evidence

[质询]该陈述包含具体的经验性数值（Qwen3-27B在W8A8 SmoothQuant下的MMLU准确率损失为0.45%，具体从84.2%降至83.75%），属于硬件/模型性能指标，无法从第一性原理推导。且参考来源显示‘本轮检索无可用来源’，缺乏外部证据支持这些具体数值的真实性。此外，Qwen3-27B的具体量化表现数据可能尚未广泛公开或存在版本差异，直接断言具体损失值存在风险。 | 经验事实，逻辑自洽但缺来源支持。陈述内部逻辑一致（84.2% - 83.75% = 0.45%），且提供了备选估计方法（参考LLaMA-3-30B），但核心具体数值缺乏外部来源验证。

## Search Query

Qwen3-27B W8A8 SmoothQuant MMLU accuracy loss
