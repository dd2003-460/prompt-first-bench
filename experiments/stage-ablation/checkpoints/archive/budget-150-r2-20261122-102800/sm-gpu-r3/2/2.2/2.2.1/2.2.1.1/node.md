# N220: Qwen3-27B 的 num_experts=64 且 num_experts_per_tok=8（MoE架构），导致激活参数约为 27B 总参数的 1/8 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

Qwen3-27B 的 num_experts=64 且 num_experts_per_tok=8（MoE架构），导致激活参数约为 27B 总参数的 1/8 左右，实际计算显存占用需基于激活参数而非总参数估算，但权重存储仍需 27B 全量。

## Corrected Claim

Qwen3-27B 采用 MoE 架构，若其配置为 64 个专家且每 token 激活 8 个，则激活参数约为总参数的 1/8，计算显存基于激活参数估算，而权重存储仍需 27B 全量显存。

## Evidence

[质询]该陈述包含具体的模型架构参数（num_experts=64, num_experts_per_tok=8）及由此推导的激活参数比例，属于经验事实。由于检索失败，无法验证这些具体数值是否准确对应 Qwen3-27B 的实际配置，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持。虽然 MoE 架构中激活参数约为总参数 1/8 的推导在给定参数下逻辑成立，且权重存储需全量显存符合常识，但具体参数值（64/8）无法通过外部来源验证，故降级。

## Search Query

Qwen3-27B HuggingFace config.json num_experts num_experts_per_tok MoE architecture
