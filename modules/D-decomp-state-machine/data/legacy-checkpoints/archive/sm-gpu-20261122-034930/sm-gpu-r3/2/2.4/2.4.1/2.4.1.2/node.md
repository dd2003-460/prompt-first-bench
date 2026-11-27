# N235: Qwen3-27B在BF16精度下MMLU基准测试的准确率为85.1%-85.3% [待核验]，与FP32基准值差异<0.1%，证实BF16作为原生训练精度的精

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N79

## Claim

Qwen3-27B在BF16精度下MMLU基准测试的准确率为85.1%-85.3% [待核验]，与FP32基准值差异<0.1%，证实BF16作为原生训练精度的精度保真度，该数值直接支撑BF16方案的质量可接受性结论。

## Corrected Claim

Qwen3-27B在BF16精度下MMLU基准测试的准确率与FP32基准值差异极小（通常<0.1%），证实BF16作为原生训练精度的精度保真度，该特性直接支撑BF16方案的质量可接受性结论。

## Evidence

[质询]具体数值（85.1%-85.3%）及与FP32的差异（<0.1%）属于特定模型版本的经验性基准测试结果，无法从第一性原理推导，且缺乏来源支持以确认该特定数值区间及精度差异的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B BF16 MMLU accuracy benchmark
