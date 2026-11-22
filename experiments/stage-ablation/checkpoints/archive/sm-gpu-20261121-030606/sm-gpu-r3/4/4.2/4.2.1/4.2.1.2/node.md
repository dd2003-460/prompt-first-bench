# N292: Qwen3-27B模型MLP中间层维度 d_ff = 11008（通常为d_model的2.5-3倍，具体值需从config.json的intermediate

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

Qwen3-27B模型MLP中间层维度 d_ff = 11008（通常为d_model的2.5-3倍，具体值需从config.json的intermediate_size字段获取）。来源：Hugging Face config.json。

## Corrected Claim

Qwen3-27B 模型 MLP 中间层维度 d_ff 通常为 d_model 的 2.5-3 倍（具体值需从 config.json 的 intermediate_size 字段获取，常见值为 11008 或 11264，需以官方配置为准）。

## Evidence

[质询]参考来源指向的是 'Qwen3.8-27B' 模型，而事实陈述针对的是 'Qwen3-27B'。虽然两者参数量级相同，但不同版本/系列的模型架构参数（如 intermediate_size）可能存在差异，且来源摘要中未直接提供 config.json 的具体数值，无法直接证实 d_ff=11008 这一具体经验参数。 | 经验事实，逻辑自洽（11008 约为 4096 的 2.68 倍，符合常见 Transformer 架构比例），但参考来源 [1][2] 指向 Qwen3.8-27B 且未直接展示 config.json 数值，缺乏直接来源支持。

## Search Query

Qwen3-27B intermediate_size mlp hidden layer dimension config.json

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=3d7831a77a0759778bf5fe7ec23242f552eacd18fef689ac2e5e92ec3eccaa2a', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
- {'url': 'https://github.com/AlibabaCloud-Official/Qwen3.8-27B&rut=6d7c70e3744b57d57ca293389d2609b017e7839b8d066985052a8b1a95bd84ec', 'type': 'ddg', 'title': 'GitHub - AlibabaCloud-Official/Qwen3.8-27B: Native multimodal dense LLM ...'}
