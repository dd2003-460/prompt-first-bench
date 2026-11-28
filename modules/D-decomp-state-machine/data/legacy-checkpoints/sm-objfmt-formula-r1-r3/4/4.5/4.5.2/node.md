# N93: FP8 量化对 HumanEval 代码生成任务的影响机制：由于代码生成对 token 概率分布敏感，FP8 的较低动态范围可能导致关键代码 token 的概率

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

FP8 量化对 HumanEval 代码生成任务的影响机制：由于代码生成对 token 概率分布敏感，FP8 的较低动态范围可能导致关键代码 token 的概率漂移，HumanEval Pass@1 从 BF16 的 70% 降至 FP8 的 67-68%（下降 2-3 个百分点）[待核验]

## Corrected Claim

FP8 量化对 HumanEval 代码生成任务有负面影响，通常导致 Pass@1 出现小幅下降（约 1-5 个百分点），具体幅度取决于模型规模和量化策略。

## Evidence

[质询]具体数值（70%降至67-68%）缺乏来源支持，且不同模型架构和量化实现下性能下降幅度差异较大，该具体区间可能不具备普适性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 quantization HumanEval Pass@1 performance degradation
