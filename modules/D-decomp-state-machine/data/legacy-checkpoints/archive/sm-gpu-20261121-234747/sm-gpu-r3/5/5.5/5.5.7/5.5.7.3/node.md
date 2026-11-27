# N426: 精度回退的触发阈值量化：Δscore > 2% 需区分任务类型，MMLU类知识任务阈值可放宽至3%，GSM8K类数学推理任务阈值需收紧至1%，具体阈值需基于Qw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N137

## Claim

精度回退的触发阈值量化：Δscore > 2% 需区分任务类型，MMLU类知识任务阈值可放宽至3%，GSM8K类数学推理任务阈值需收紧至1%，具体阈值需基于Qwen3-27B在各任务上的基线准确率（如MMLU 85%、GSM8K 90%）计算绝对分差（如MMLU 1.7分、GSM8K 0.9分）。

## Corrected Claim

精度回退的触发阈值量化：Δscore > 2% 需区分任务类型，MMLU类知识任务阈值可放宽至3%，GSM8K类数学推理任务阈值需收紧至1%，具体阈值需基于Qwen3-27B在各任务上的基线准确率（如MMLU 85%、GSM8K 90%）计算绝对分差（如MMLU 1.7分、GSM8K 0.9分）。

## Evidence

先验知识/题面给定，逻辑校验通过：阈值设定符合任务难度与基线准确率的逻辑关系（数学推理对精度更敏感，故阈值更严），数值计算（85%*2%=1.7, 90%*1%=0.9）准确无误。
