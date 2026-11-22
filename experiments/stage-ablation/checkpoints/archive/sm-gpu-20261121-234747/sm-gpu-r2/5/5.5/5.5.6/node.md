# N136: 精度-任务敏感度矩阵：列出MMLU/HumanEval/GSM8K各任务对FP8/INT8/NVFP4/W4的敏感度排序，例如GSM8K对INT8敏感（Δ>2%

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

精度-任务敏感度矩阵：列出MMLU/HumanEval/GSM8K各任务对FP8/INT8/NVFP4/W4的敏感度排序，例如GSM8K对INT8敏感（Δ>2%）而MMLU对FP8不敏感（Δ<0.5%），需基于实测数据构建

## Corrected Claim

精度-任务敏感度矩阵：通常GSM8K等数学推理任务对低比特量化（如INT8/W4）较为敏感，而MMLU等知识密集型任务对FP8等较高精度量化相对不敏感，具体敏感度排序及阈值（如Δ值）需基于特定模型架构、量化算法及校准数据集的实测数据构建。

## Evidence

[质询]该陈述声称基于实测数据构建具体数值阈值（如GSM8K对INT8敏感Δ>2%，MMLU对FP8不敏感Δ<0.5%），但缺乏具体模型架构、量化算法（如GPTQ/AWQ）及校准数据集等关键上下文，不同实现下敏感度排序和具体数值可能显著不同，存在以偏概全或数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且具体量化敏感度数值属于依赖实验条件的经验数据，无法从第一性原理严格推出）。

## Search Query

quantization sensitivity MMLU HumanEval GSM8K FP8 INT8 W4
