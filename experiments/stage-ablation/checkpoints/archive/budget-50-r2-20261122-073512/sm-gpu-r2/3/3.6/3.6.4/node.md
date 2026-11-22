# N141: 量化质量损失可接受性的量化阈值公式：若 (1 - Acc_quantized/Acc_BF16) < 0.02 且 (PPL_quantized/PPL_BF1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

量化质量损失可接受性的量化阈值公式：若 (1 - Acc_quantized/Acc_BF16) < 0.02 且 (PPL_quantized/PPL_BF16 - 1) < 0.05，则判定质量损失可接受；其中 Acc 为 MMLU 准确率，PPL 为 WikiText-2 困惑度。

## Corrected Claim

量化质量损失可接受性的量化阈值公式：若 (1 - Acc_quantized/Acc_BF16) < 0.02 且 (PPL_quantized/PPL_BF16 - 1) < 0.05，则判定质量损失可接受；其中 Acc 为 MMLU 准确率，PPL 为 WikiText-2 困惑度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM quantization quality acceptance threshold accuracy drop perplexity increase
