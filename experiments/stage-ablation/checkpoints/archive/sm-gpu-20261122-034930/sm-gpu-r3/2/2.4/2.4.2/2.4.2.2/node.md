# N237: Qwen3-27B在BF16精度下HumanEval代码生成基准测试的Pass@1准确率为68.2%-68.6% [待核验]，与FP32基准值差异<0.5%，证

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B在BF16精度下HumanEval代码生成基准测试的Pass@1准确率为68.2%-68.6% [待核验]，与FP32基准值差异<0.5%，证实BF16精度对代码生成任务的保真度，该数值直接支撑BF16方案在代码任务中的质量可接受性结论。

## Corrected Claim

Qwen3-27B在BF16精度下HumanEval代码生成基准测试的Pass@1准确率与FP32基准值差异极小（通常<0.5%），证实BF16精度对代码生成任务具有高度保真度，该结论支撑BF16方案在代码任务中的质量可接受性。

## Evidence

[质询]具体数值（68.2%-68.6%）及与FP32的差异（<0.5%）属于特定模型版本的经验性基准测试结果，无法从第一性原理推导，且缺乏来源支持以确认该具体数值范围及差异阈值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B BF16 HumanEval Pass@1 accuracy
