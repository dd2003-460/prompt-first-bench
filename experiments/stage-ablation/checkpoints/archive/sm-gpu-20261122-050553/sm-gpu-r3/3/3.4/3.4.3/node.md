# N73: W4 量化在 32K 长上下文场景下的累积误差：当上下文长度从 4K 增加到 32K 时，困惑度 (PPL) 的额外增加量 (ΔPPL_long_ctx) 比短

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N19

## Claim

W4 量化在 32K 长上下文场景下的累积误差：当上下文长度从 4K 增加到 32K 时，困惑度 (PPL) 的额外增加量 (ΔPPL_long_ctx) 比短上下文多 0.5-1.5 [待核验]，导致长文本生成的连贯性显著下降。

## Corrected Claim

W4 量化在 32K 长上下文场景下，随着上下文长度增加，累积误差会导致困惑度 (PPL) 上升，进而影响长文本生成的连贯性。

## Evidence

[质询]该陈述包含具体的经验数值范围（ΔPPL 增加 0.5-1.5），属于硬件/模型性能相关的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

LLM 4-bit quantization long context 32k perplexity degradation cumulative error
