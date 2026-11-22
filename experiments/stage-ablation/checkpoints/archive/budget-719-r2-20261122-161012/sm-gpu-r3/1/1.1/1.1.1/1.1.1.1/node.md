# N139: Qwen3-27B 的总参数量由 Embedding 层、64 层 Transformer Block (Attention + FFN) 及 LM Head 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B 的总参数量由 Embedding 层、64 层 Transformer Block (Attention + FFN) 及 LM Head 组成，精确参数计数需查阅 Hugging Face 模型配置或官方技术报告以确认 27.1B 是否包含 Embedding 权重

## Corrected Claim

Qwen3-27B 采用标准 Transformer 架构，包含 Embedding 层、64 层 Transformer Block 及 LM Head；其标称参数量 27B 通常指总参数量，具体是否精确为 27.1B 及是否包含 Embedding 权重需以官方技术报告或 Hugging Face 配置为准。

## Evidence

[质询]陈述中关于'精确参数计数需查阅...以确认'属于元数据/操作建议，而非可验证的事实断言；且参考来源主要讨论Qwen3.8-27B（视觉语言模型）或ONNX部署，未直接提供Qwen3-27B（纯文本模型）的精确参数构成细节或27.1B是否包含Embedding的明确结论，存在来源与具体事实节点（纯文本模型参数细节）不完全匹配的问题。 | 逻辑上Transformer架构确实由Embedding、Transformer Blocks和LM Head组成，该陈述在架构描述上自洽；但参考来源[1][2]主要涉及Qwen3.8-27B（VL模型）或ONNX格式，未直接证实Qwen3-27B纯文本模型的具体参数计数细节及27.1B的精确构成，属于间接支持或无关，故降级。

## Search Query

Qwen3-27B parameter count breakdown embedding layers huggingface config

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00936/article/details/168246892&rut=0b57483ac0e72443e69ac92bea322d1674a6992ebad75530985f411d7aed98ba', 'type': 'ddg', 'title': '如何读懂Qwen3.8-27B ONNX模型：64层混合注意力与256K长上下文架构完整指南-CSDN博客'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e5459bd6ec62e1937706a05f835d37baa128ee9ce9105b7cdd4ee711d207a8ed', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
