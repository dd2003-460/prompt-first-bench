# N246: Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（如 4096 * 2.7 ≈ 1100

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（如 4096 * 2.7 ≈ 11008），该参数直接决定 FFN 激活内存大小，是计算 Act_Mem 的关键缺失变量，原公式中未包含 d_ff 导致估算偏差。

## Corrected Claim

Qwen3-27B 的 FFN 中间维度 (d_ff) 需从模型配置文件中确认，通常约为 d_model 的 2.7 倍（具体数值需查证），该参数直接决定 FFN 激活内存大小，是计算 Act_Mem 的关键变量。

## Evidence

[质询]该陈述包含具体的经验参数（d_ff ≈ 2.7 * d_model 及具体数值 11008），属于特定模型架构的配置细节，无法从第一性原理推导，且缺乏来源支持以确认 Qwen3-27B 的具体配置值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

Qwen3-27B model config d_ff intermediate size
