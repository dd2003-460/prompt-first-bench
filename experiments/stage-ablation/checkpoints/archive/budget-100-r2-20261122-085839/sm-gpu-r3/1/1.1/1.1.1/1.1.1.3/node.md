# N123: Qwen3-27B 中 LM Head（输出层）参数量 = hidden_size * vocab_size，若与 Embedding 共享权重（tied em

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Qwen3-27B 中 LM Head（输出层）参数量 = hidden_size * vocab_size，若与 Embedding 共享权重（tied embeddings）则为 0 额外参数，否则与 N94 相同，需确认 config 中 tie_word_embeddings 字段值。

## Corrected Claim

Qwen3-27B 中 LM Head 参数量理论上为 hidden_size * vocab_size。若模型配置中 tie_word_embeddings 为 true，则额外参数量为 0；否则为 hidden_size * vocab_size。具体数值需查阅该模型的 config.json 确认。

## Evidence

[质询]该陈述包含具体的模型架构参数（Qwen3-27B 的 hidden_size 和 vocab_size 具体数值隐含在公式中，且断言了具体的配置行为），属于经验事实。虽然公式 `hidden_size * vocab_size` 是通用的，但针对特定模型 Qwen3-27B 的具体配置（是否 tie embeddings）需要查证具体 config 文件，仅凭逻辑无法确定其具体数值或最终参数量是否为0。 | 经验事实，逻辑自洽但缺来源支持。LM Head 参数量公式正确，但 Qwen3-27B 的具体配置（tie_word_embeddings 值）需外部证据确认，当前无可用来源。

## Search Query

Qwen3-27B tie_word_embeddings lm_head parameters
