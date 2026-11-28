# N637: LLM-as-a-Judge 在分类任务上的 Cohen's Kappa 系数 κ_LLM 与人类标注者之间的相关性：κ_LLM ≈ 0.75-0.85（基于 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N227

## Claim

LLM-as-a-Judge 在分类任务上的 Cohen's Kappa 系数 κ_LLM 与人类标注者之间的相关性：κ_LLM ≈ 0.75-0.85（基于 GPT-4o 在 MMLU 子集上的表现），若 κ_LLM <0.8，则需引入 2 个独立 LLM 实例进行二次投票，错误率进一步降低至 ~5%

## Corrected Claim

LLM-as-a-Judge 在分类任务上的 Cohen's Kappa 系数通常较高，若低于阈值（如0.8），引入多实例投票机制有助于降低错误率。

## Evidence

[质询]该陈述包含具体的经验参数（κ值范围0.75-0.85、错误率~5%）和特定模型/数据集组合（GPT-4o/MMLU），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

LLM as a judge inter-annotator agreement kappa coefficient
