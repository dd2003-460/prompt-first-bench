# N171: MTP 草稿接受率 η 与序列长度 L 的非线性衰减关系：η(L) = η_base * exp(-α * log(L/L_0))，其中 α 为 OOD 敏感度

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

MTP 草稿接受率 η 与序列长度 L 的非线性衰减关系：η(L) = η_base * exp(-α * log(L/L_0))，其中 α 为 OOD 敏感度系数；在 L=10k 时 η≈0.75，L=100k 时 η 预计降至 0.55 以下，导致有效吞吐量 Throughput_eff = Base_TPS * (1 + η*(K-1)) 在长上下文场景下降超过 20%

## Corrected Claim

MTP 草稿接受率 η 通常随序列长度 L 增加而呈现非线性衰减趋势（如遵循 η(L) ∝ exp(-α * log(L/L_0)) 形式的模型），在长上下文场景下（如从 10k 增至 100k tokens），接受率显著下降可能导致有效吞吐量降低，具体降幅取决于模型架构与数据分布，需实测确定。

## Evidence

[质询]该陈述包含具体的经验参数（η_base, α, 特定长度下的具体数值 0.75/0.55）及具体的性能下降阈值（20%），这些属于经验事实而非第一性原理可推导的数学性质。虽然公式形式在逻辑上自洽（对数衰减导致指数衰减），但缺乏外部来源验证其具体数值和实际工程表现，存在将理论模型直接等同于实际系统行为的风险。 | 先验知识/题面给定，逻辑校验通过（公式推导自洽），但作为经验事实缺乏来源直接支持，故降级。

## Search Query

speculative decoding acceptance rate degradation long context length exponential decay
