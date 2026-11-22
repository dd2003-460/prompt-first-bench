# N93: Qwen3-27B 在 GPTQ-INT8 量化下，HumanEval (代码生成) 的 Pass@1 准确率通常从 BF16 的 ~65-70% 下降至 ~6

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 GPTQ-INT8 量化下，HumanEval (代码生成) 的 Pass@1 准确率通常从 BF16 的 ~65-70% 下降至 ~60-65%，下降幅度约为 5-10 个百分点；若使用 GPTQ-INT4 则下降更显著，此处特指 INT8 对称/非对称量化对代码逻辑连贯性的影响。

## Corrected Claim

Qwen3-27B 在 GPTQ-INT8 量化下，HumanEval (代码生成) 的 Pass@1 准确率通常会出现一定程度的下降（具体幅度取决于量化实现与校准数据），若使用 GPTQ-INT4 则下降通常更显著。

## Evidence

[质询]具体数值区间（65-70%降至60-65%）属于经验事实，缺乏通用基准数据支持，不同量化实现（如GPTQ vs AWQ）及校准数据集可能导致结果差异较大，且Qwen3-27B的具体公开评测数据可能未覆盖此特定量化配置。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GPTQ INT8 HumanEval Pass@1 accuracy drop
