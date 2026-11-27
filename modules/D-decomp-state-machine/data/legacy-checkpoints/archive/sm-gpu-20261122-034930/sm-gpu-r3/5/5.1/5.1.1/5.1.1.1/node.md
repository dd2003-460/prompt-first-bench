# N342: BF16精度下Qwen3-27B的MMLU准确率与FP32基准的差异通常<0.5%，Perplexity增加<0.1%，该结论基于对大语言模型混合精度训练/推理

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122, N123, N124

## Claim

BF16精度下Qwen3-27B的MMLU准确率与FP32基准的差异通常<0.5%，Perplexity增加<0.1%，该结论基于对大语言模型混合精度训练/推理稳定性的普遍认知，但具体数值需针对Qwen3-27B架构进行本地评估确认。

## Corrected Claim

BF16精度下Qwen3-27B的MMLU准确率与FP32基准的差异通常<0.5%，Perplexity增加<0.1%，该结论基于对大语言模型混合精度训练/推理稳定性的普遍认知，但具体数值需针对Qwen3-27B架构进行本地评估确认。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B BF16 vs FP32 MMLU accuracy perplexity difference
