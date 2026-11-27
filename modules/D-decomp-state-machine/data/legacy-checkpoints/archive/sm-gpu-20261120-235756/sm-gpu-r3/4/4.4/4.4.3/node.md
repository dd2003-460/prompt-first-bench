# N93: 量化精度损失的质量评估指标：使用 MMLU、GSM8K 等基准测试，BF16 vs FP8 的准确率下降通常 <0.5%，而 W4A16 的下降可能在 1-3%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

量化精度损失的质量评估指标：使用 MMLU、GSM8K 等基准测试，BF16 vs FP8 的准确率下降通常 <0.5%，而 W4A16 的下降可能在 1-3% 之间，需设定可接受阈值（如 <1%）作为决策边界。

## Corrected Claim

量化精度损失的质量评估指标：使用 MMLU、GSM8K 等基准测试，BF16 vs FP8 的准确率下降通常 <0.5%，而 W4A16 的下降可能在 1-3% 之间，需设定可接受阈值（如 <1%）作为决策边界。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

FP8 vs BF16 LLM accuracy drop MMLU benchmark
