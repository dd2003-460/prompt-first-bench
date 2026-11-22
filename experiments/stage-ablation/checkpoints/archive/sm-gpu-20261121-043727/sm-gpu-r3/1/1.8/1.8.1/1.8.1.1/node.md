# N152: Qwen3-27B 在 BF16 精度下 WikiText-2 Perplexity (PPL) 的具体数值（参考 Qwen2.5-32B 约为 5.8-6.2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N59

## Claim

Qwen3-27B 在 BF16 精度下 WikiText-2 Perplexity (PPL) 的具体数值（参考 Qwen2.5-32B 约为 5.8-6.2，Qwen3 同级别模型预计 PPL < 6.0，需从官方技术报告获取精确值作为 ΔPPL 计算的基准项 PPL_BF16）

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 WikiText-2 Perplexity 具体数值需查阅官方技术报告获取；参考 Qwen2.5-32B 约为 5.8-6.2，预计 Qwen3 同级别模型 PPL < 6.0，但当前参考来源未提供确切基准值。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B'（一个多模态模型），而非纯文本的 'Qwen3-27B'，且摘要中未包含 WikiText-2 Perplexity 的具体数值，存在模型版本混淆及数据缺失的风险。 | 经验事实，逻辑自洽但缺来源支持；参考来源 [1][2][3] 均涉及 Qwen3.8-27B 且未提供 WikiText-2 PPL 具体数值，无法直接验证 Qwen3-27B 的精确 PPL。

## Search Query

Qwen3-27B WikiText-2 perplexity BF16

## Retrieval Sources

- {'url': 'https://huggingface.co/Qwen/Qwen3.8-27B&rut=3d7831a77a0759778bf5fe7ec23242f552eacd18fef689ac2e5e92ec3eccaa2a', 'type': 'ddg', 'title': 'Qwen/Qwen3.8-27B · Hugging Face'}
- {'url': 'https://huggingface.co/cyankiwi/Qwen3.8-27B-AWQ-BF16-INT4&rut=f53ca4ccb56f332986aa3151bf26382b96dd9d8b30459958d54f9cdaf9dfc344', 'type': 'ddg', 'title': 'cyankiwi/Qwen3.8-27B-AWQ-BF16-INT4 · Hugging Face'}
- {'url': 'https://github.com/AlibabaCloud-Official/Qwen3.8-27B&rut=6d7c70e3744b57d57ca293389d2609b017e7839b8d066985052a8b1a95bd84ec', 'type': 'ddg', 'title': 'GitHub - AlibabaCloud-Official/Qwen3.8-27B: Native multimodal dense LLM ...'}
