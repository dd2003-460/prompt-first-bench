# N328: INT4 量化在 MMLU-Pro 子任务中的损失分布不均匀：在 'Math' 子任务上下降 4.5 个百分点 (从 68.2% 至 63.7%)，在 'Cod

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N118

## Claim

INT4 量化在 MMLU-Pro 子任务中的损失分布不均匀：在 'Math' 子任务上下降 4.5 个百分点 (从 68.2% 至 63.7%)，在 'Coding' 子任务上下降 1.8 个百分点 (从 75.1% 至 73.3%)，在 'General Knowledge' 子任务上下降 1.2 个百分点 (从 79.4% 至 78.2%)，表明量化对推理密集型任务的敏感度高于知识检索型任务，这与 N119 中 GSM8K 下降 5-6 个百分点的观察一致。

## Corrected Claim

INT4 量化在 MMLU-Pro 子任务中的损失分布通常不均匀：在推理密集型任务（如 Math, Coding）上的性能下降幅度通常高于知识检索型任务（如 General Knowledge），这与 GSM8K 等数学基准上观察到的较大量化损失一致。

## Evidence

[质询]具体数值（如68.2%至63.7%）属于特定模型和量化配置下的经验事实，缺乏来源支持，且不同模型/量化方法下数值差异巨大，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 AWQ MMLU-Pro subtask breakdown math coding
