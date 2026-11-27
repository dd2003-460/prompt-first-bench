# N151: INT8 KV Cache 量化对生成质量的影响量化：在 32K 长上下文下，KV Cache 量化导致的注意力分数误差累积，通常使困惑度（Perplexity

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

INT8 KV Cache 量化对生成质量的影响量化：在 32K 长上下文下，KV Cache 量化导致的注意力分数误差累积，通常使困惑度（Perplexity）增加 0.5-1.5，或在长文本生成任务中导致重复率增加 2-5% [待核验]

## Corrected Claim

INT8 KV Cache 量化在 32K 长上下文下通常会导致生成质量轻微下降，表现为困惑度（Perplexity）小幅增加或长文本生成中重复率上升，具体数值取决于量化算法与模型架构。

## Evidence

[质询]数值量级缺乏普适性：INT8 KV Cache 量化对困惑度（PPL）的影响高度依赖于模型架构（如 GQA vs MHA）、量化策略（如 SmoothQuant, KIVI 等）以及具体任务。在 32K 长上下文下，PPL 增加 0.5-1.5 是一个较大的范围，且对于某些先进量化方法，PPL 增加可能远低于 0.5；同时，'重复率增加 2-5%' 这一具体指标缺乏统一的基准测试支持，不同数据集上的表现差异巨大，直接给出固定区间存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体数值区间属于经验性工程数据，无法从第一性原理严格推导，故降级为定性表述）

## Search Query

INT8 KV cache quantization perplexity degradation long context LLM
