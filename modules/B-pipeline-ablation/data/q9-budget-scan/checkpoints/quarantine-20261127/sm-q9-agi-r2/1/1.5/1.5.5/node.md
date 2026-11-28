# N49: 外部记忆压缩机制的信息保留率 R_compression 的量化下限，为确保'可发表级'结论的逻辑连贯性，关键事实（Key Facts）的召回率需 > 0.95

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

外部记忆压缩机制的信息保留率 R_compression 的量化下限，为确保'可发表级'结论的逻辑连贯性，关键事实（Key Facts）的召回率需 > 0.95，整体语义相似度余弦值需 > 0.85；低于此阈值将导致推理链断裂。

## Corrected Claim

外部记忆压缩机制需确保关键事实的高召回率和整体语义的高相似度以维持推理链连贯性，具体阈值需根据应用场景实验确定。

## Evidence

[质询]陈述中给出的具体数值阈值（召回率>0.95，余弦相似度>0.85）属于经验性参数，缺乏通用标准或第一性原理支持，且参考来源并未提供这些具体的量化下限数据。 | 来源[2]讨论了记忆保留和压缩，但未提供具体的量化阈值；该事实为经验性设定，逻辑自洽但缺乏直接来源支持具体数值。

## Search Query

LLM context compression information retention rate threshold logical consistency benchmark

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2505.07289v1&rut=34e0e07bf99ae25415ed5fabc856e53a29d7140a64108aeec216bca0ba84e869', 'type': 'ddg', 'title': '[2505.07289v1] Semantic Retention and Extreme Compression in LLMs: Can ...'}
- {'url': 'https://arxiv.org/abs/2502.15957&rut=8fc208b89eaf5240aa0214df9afab9fc2c8fd428828dbf4b860d357c335f5869', 'type': 'ddg', 'title': 'R$^3$Mem: Bridging Memory Retention and Retrieval via Reversible ...'}
