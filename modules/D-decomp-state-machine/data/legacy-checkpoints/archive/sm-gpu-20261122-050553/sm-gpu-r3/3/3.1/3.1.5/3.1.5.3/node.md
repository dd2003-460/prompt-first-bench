# N209: FP8 KV Cache 在长上下文（>16K）下的性能退化阈值：当上下文长度超过 16K 时，FP8 KV 导致的 MMLU 准确率下降通常从 <1% 线性增

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N67

## Claim

FP8 KV Cache 在长上下文（>16K）下的性能退化阈值：当上下文长度超过 16K 时，FP8 KV 导致的 MMLU 准确率下降通常从 <1% 线性增长至 2-3%（32K 处），而 BF16 KV 保持 <0.5% 下降，因此 32K 场景下混合精度是质量底线。

## Corrected Claim

FP8 KV Cache 在长上下文（>16K）下通常会导致 MMLU 准确率下降，且下降幅度随上下文长度增加而增大；相比之下，BF16 KV 的精度损失通常更小。在 32K 场景下，若对质量要求极高，混合精度或全精度可能是更稳妥的选择。

## Evidence

[质询]该陈述包含具体的经验性数值（如32K处下降2-3%、BF16下降<0.5%）和特定的性能退化阈值（16K），这些属于硬件/模型行为的具体经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

FP8 KV cache long context degradation MMLU benchmark 32k tokens
