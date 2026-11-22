# N289: FP8 量化在医疗/法律高风险场景下的质量损失边界：基于 N121-N123，FP8 在 MMLU-Pro 下降 <0.5%，Perplexity 增加 <1%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

FP8 量化在医疗/法律高风险场景下的质量损失边界：基于 N121-N123，FP8 在 MMLU-Pro 下降 <0.5%，Perplexity 增加 <1%。在长尾事实性错误 (Long-tail Factual Errors) 方面，FP8 的累积误差在 32K 上下文下可能略高于 BF16，但仍在 <2% 范围内 [待核验]。此损失可接受，故 FP8 为最低可行精度。

## Corrected Claim

FP8 量化在医疗/法律高风险场景下的质量损失通常较小，在长尾事实性错误方面可能略高于 BF16，但总体损失在可接受范围内，故 FP8 常被视为最低可行精度。

## Evidence

[质询]具体数值（MMLU-Pro下降<0.5%，Perplexity增加<1%，长尾错误<2%）属于特定模型和实验条件下的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 E4M3 long context factual error rate 32K
