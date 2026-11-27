# N515: INT4 KV Cache 相对于 BF16 KV Cache 的精度损失导致长上下文（>16K）下的困惑度（Perplexity）平均增加 2-5%，在 32

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157

## Claim

INT4 KV Cache 相对于 BF16 KV Cache 的精度损失导致长上下文（>16K）下的困惑度（Perplexity）平均增加 2-5%，在 32K 上下文下可能引发注意力分数饱和，需通过 Q-Attention 或量化感知训练（QAT）来缓解。

## Corrected Claim

INT4 KV Cache 相对于 BF16 KV Cache 存在精度损失，在长上下文（>16K）下可能导致困惑度增加（具体幅度取决于模型和量化算法），并可能影响注意力机制的稳定性，需通过 Q-Attention 或量化感知训练（QAT）来缓解。

## Evidence

[质询]数值量级与具体机制缺乏普适性：2-5%的困惑度增加是特定模型和量化算法（如GPTQ/AWQ）下的经验观测值，并非INT4量化的固有物理属性；且'注意力分数饱和'并非INT4 KV Cache在32K上下文下的必然或典型现象，该表述可能混淆了特定低比特量化缺陷与通用量化误差。 | 先验知识/题面给定，逻辑校验通过，但具体数值（2-5%）和特定现象（注意力饱和）属于经验事实，缺乏普适性，降级为定性表述。

## Search Query

INT4 KV cache perplexity degradation long context 32K
