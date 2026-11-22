# N233: NVFP4 量化在 32K 长上下文下额外增加的困惑度误差项 ΔPPL_long 需通过对比同一模型在 1K 和 32K 上下文下的 PPL 差值（PPL_32

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N60

## Claim

NVFP4 量化在 32K 长上下文下额外增加的困惑度误差项 ΔPPL_long 需通过对比同一模型在 1K 和 32K 上下文下的 PPL 差值（PPL_32K - PPL_1K）与 BF16 基线的对应差值之差来量化，以验证 [0.5%, 1.0%] 的累积误差假设

## Corrected Claim

NVFP4 量化在 32K 长上下文下额外增加的困惑度误差项 ΔPPL_long 可通过对比同一模型在 1K 和 32K 上下文下的 PPL 差值（PPL_32K - PPL_1K）与 BF16 基线的对应差值之差来量化，以验证累积误差假设（具体数值范围需实验确定）。

## Evidence

[质询]该陈述描述了一种具体的实验方法论（通过对比1K和32K上下文下的PPL差值之差来量化NVFP4量化在长上下文下的额外误差），并提出了一个具体的数值假设（[0.5%, 1.0%]）。这属于经验事实/实验设计范畴，无法从第一性原理直接推出，且缺乏来源支持其方法论的普适性或数值假设的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

long context LLM quantization KV cache error accumulation perplexity delta 32k tokens
