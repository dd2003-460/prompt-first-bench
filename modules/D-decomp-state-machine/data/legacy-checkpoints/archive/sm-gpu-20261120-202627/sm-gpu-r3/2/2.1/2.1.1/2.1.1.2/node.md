# N206: Qwen3-27B 在 BF16 精度下的基准困惑度对上下文长度的敏感性分析：在 32K 长上下文场景下，困惑度是否随序列长度增加而显著上升（通常长文本生成中困

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

Qwen3-27B 在 BF16 精度下的基准困惑度对上下文长度的敏感性分析：在 32K 长上下文场景下，困惑度是否随序列长度增加而显著上升（通常长文本生成中困惑度会略高于短文本基准），需量化该差异（如 +0.5-1.0 ppl）

## Corrected Claim

Qwen3-27B 在 BF16 精度下，32K 长上下文场景的困惑度通常略高于短文本基准，但具体差异幅度需实测数据确认，无法仅凭逻辑推断出 +0.5-1.0 ppl 的精确范围。

## Evidence

[质询]该陈述包含具体的经验性数值范围（+0.5-1.0 ppl）和特定模型（Qwen3-27B）在特定精度（BF16）下的表现，属于硬件/模型规格类的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽（长上下文困惑度通常略高符合直觉）但缺来源支持，且具体数值范围无依据。

## Search Query

LLM perplexity sensitivity to context length 32k tokens long context degradation
