# N158: Qwen3-27B 中线性注意力（Linear Attention）层数确认为 48 层，即总层数 64 层的 75%，这些层在推理时不生成 KV Cache，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

Qwen3-27B 中线性注意力（Linear Attention）层数确认为 48 层，即总层数 64 层的 75%，这些层在推理时不生成 KV Cache，需通过架构文档验证

## Corrected Claim

Qwen3-27B 采用混合注意力机制，其中部分层为线性注意力层（具体层数需查阅官方架构文档确认），这些层在推理时不生成 KV Cache。

## Evidence

[质询]具体层数（48层）及占比（75%）属于特定模型版本的经验性架构参数，无法从第一性原理推导，且缺乏来源支持，存在数值错误风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B linear attention layers 48 no KV cache
