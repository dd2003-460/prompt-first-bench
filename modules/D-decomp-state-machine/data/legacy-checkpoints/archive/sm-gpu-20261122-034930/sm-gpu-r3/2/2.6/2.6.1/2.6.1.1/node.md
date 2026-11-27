# N244: Qwen3-27B (或同规模Llama-3-8B/13B/70B作为代理参考) 在 W4A16 AWQ 量化下，MMLU 基准测试的准确率损失具体数值为 1.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N84

## Claim

Qwen3-27B (或同规模Llama-3-8B/13B/70B作为代理参考) 在 W4A16 AWQ 量化下，MMLU 基准测试的准确率损失具体数值为 1.5% - 2.5% (绝对值)，来源为 MIT Han Lab AWQ 论文及 HuggingFace Optimum 基准测试报告；若损失 > 5%，则触发回退至 W8 的决策阈值。

## Corrected Claim

Qwen3-27B 在 W4A16 AWQ 量化下，MMLU 基准测试的准确率损失通常在 1.5% - 2.5% 范围内（基于同规模模型代理参考）；若实测损失显著超过 5%，建议评估回退至 W8 量化。

## Evidence

[质询]该陈述包含具体的经验性数值（1.5%-2.5%）和特定的决策阈值（>5%），且引用了特定来源（MIT Han Lab AWQ 论文及 HuggingFace Optimum 报告）。然而，AWQ 原始论文主要关注的是量化算法本身及在特定模型（如 LLaMA-7B/13B）上的表现，并未直接提供 Qwen3-27B 在 W4A16 下的 MMLU 具体损失数值，也未定义通用的“回退至 W8 的决策阈值”。此外，不同模型、不同量化实现（如 GPTQ vs AWQ）及不同数据集版本会导致数值波动，将特定实验结果泛化为固定区间和硬性阈值缺乏普遍性支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且原始 AWQ 论文未直接覆盖 Qwen3-27B 的具体 MMLU 损失数值及通用决策阈值）。

## Search Query

Qwen3-27B AWQ W4A16 MMLU accuracy loss benchmark
