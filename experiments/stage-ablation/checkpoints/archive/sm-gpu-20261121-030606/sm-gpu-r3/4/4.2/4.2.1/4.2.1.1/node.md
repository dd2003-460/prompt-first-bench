# N291: Qwen3-27B模型隐藏层维度 d_model = 4096，注意力头数 n_heads = 32，每头维度 head_dim = 128。来源：Huggin

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

Qwen3-27B模型隐藏层维度 d_model = 4096，注意力头数 n_heads = 32，每头维度 head_dim = 128。来源：Hugging Face config.json中hidden_size=4096, num_attention_heads=32。

## Corrected Claim

Qwen3-27B模型隐藏层维度 d_model = 4096，注意力头数 n_heads = 32，每头维度 head_dim = 128。（注：参考来源指向Qwen3.8-27B，需确认Qwen3-27B具体配置是否一致，建议补充Qwen3-27B官方config.json作为直接证据）

## Evidence

[质询]参考来源[1]指向的是 'Qwen3.8-27B' 模型，而待核验事实针对的是 'Qwen3-27B'。虽然两者参数量级相同（27B），但版本号不同（3.8 vs 3），架构参数（如 hidden_size, n_heads）可能因版本迭代而存在差异，来源未直接覆盖 Qwen3-27B 的具体配置，存在版本混淆风险。 | 逻辑校验通过：4096 / 32 = 128，数值自洽且符合常见大模型架构量级；但参考来源[1]仅提及 Qwen3.8-27B，未提供 Qwen3-27B 的 config.json 具体参数，属于间接/不相关来源，无法直接支持该特定版本的事实。

## Search Query

Qwen3-27B hidden_size num_attention_heads config.json

## Retrieval Sources

- {'url': 'https://github.com/AlibabaCloud-Official/Qwen3.8-27B&rut=6d7c70e3744b57d57ca293389d2609b017e7839b8d066985052a8b1a95bd84ec', 'type': 'ddg', 'title': 'GitHub - AlibabaCloud-Official/Qwen3.8-27B: Native multimodal dense LLM ...'}
