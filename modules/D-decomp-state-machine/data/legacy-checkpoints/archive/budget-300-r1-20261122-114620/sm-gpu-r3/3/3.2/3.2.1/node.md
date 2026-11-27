# N89: FP8 (E4M3) 在 Qwen3-27B 上的 Perplexity 增加具体数值：在 WikiText-103 基准上，FP8 的 PPL 比 BF16 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

FP8 (E4M3) 在 Qwen3-27B 上的 Perplexity 增加具体数值：在 WikiText-103 基准上，FP8 的 PPL 比 BF16 高 0.5-1.0%（例如 BF16 PPL=10.0，FP8 PPL=10.05-10.10）

## Corrected Claim

FP8 (E4M3) 在 Qwen3-27B 上的 Perplexity 相比 BF16 有轻微增加，具体数值需参考特定基准测试报告。

## Evidence

[质询]具体数值（0.5-1.0%）属于经验事实，缺乏直接来源支持，且不同模型/数据集下精度损失波动较大，该具体区间可能不准确或过于具体。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 E4M3 perplexity increase vs BF16
