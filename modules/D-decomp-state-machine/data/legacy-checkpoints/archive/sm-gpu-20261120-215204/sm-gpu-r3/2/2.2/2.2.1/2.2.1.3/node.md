# N205: FP8 量化在长上下文（>16K）场景下，由于 KV Cache 累积误差，可能导致注意力分数分布偏移，使得 MMLU 准确率下降幅度随上下文长度增加而线性增长

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

FP8 量化在长上下文（>16K）场景下，由于 KV Cache 累积误差，可能导致注意力分数分布偏移，使得 MMLU 准确率下降幅度随上下文长度增加而线性增长，预计 32K 上下文下下降幅度可能达到 0.5%-1.0%，高于短上下文下的 0.2%，需作为 [待核验] 风险项。

## Corrected Claim

FP8 量化在长上下文（>16K）场景下，由于 KV Cache 累积误差，可能导致注意力分数分布偏移，使得 MMLU 准确率下降幅度随上下文长度增加而增大，具体下降幅度需实测验证，建议作为 [待核验] 风险项。

## Evidence

[质询]该陈述包含具体的经验性数值预测（0.5%-1.0% vs 0.2%）和特定的线性增长规律，属于硬件/算法性能的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

FP8 KV cache accumulation error long context LLM accuracy degradation
