# N126: MTP×4接受率α的硬件依赖量化：在NVFP4量化下，由于draft model与target model权重精度一致但KV Cache为FP8，长上下文（>8

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

MTP×4接受率α的硬件依赖量化：在NVFP4量化下，由于draft model与target model权重精度一致但KV Cache为FP8，长上下文（>8k tokens）下KV Cache累积误差导致logits偏差，α从短上下文的0.85衰减至长上下文的0.45。衰减函数α(n) ≈ 0.85 * exp(-λ*n)，其中λ≈0.00003（基于Qwen3.8-27B实测推测），n为当前上下文长度。

## Corrected Claim

在NVFP4量化下，由于KV Cache精度限制，长上下文可能导致MTP接受率α随上下文长度增加而衰减，但具体衰减函数及参数需基于特定模型的实测数据确定。

## Evidence

[质询]该陈述包含具体的经验参数（如α从0.85衰减至0.45，λ≈0.00003）和特定模型（Qwen3.8-27B）的实测推测，属于经验事实。在缺乏任何外部来源支持的情况下，这些具体数值无法通过第一性原理推导得出，且‘Qwen3.8-27B’这一具体型号及其实测数据缺乏公开权威来源佐证，存在虚构或过度拟合特定实验条件的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值和模型实测数据的真实性）

## Search Query

Qwen3 27B NVFP4 speculative decoding acceptance rate long context decay
