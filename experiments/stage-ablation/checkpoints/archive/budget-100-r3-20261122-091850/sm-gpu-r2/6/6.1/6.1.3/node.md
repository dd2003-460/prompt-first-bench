# N99: 模型结构参数溯源：Qwen3-27B 的 num_layers, hidden_dim, num_kv_heads 等参数应直接引用 Hugging Face 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

模型结构参数溯源：Qwen3-27B 的 num_layers, hidden_dim, num_kv_heads 等参数应直接引用 Hugging Face 模型卡或官方论文，标记为 high confidence (source: knowledge/derived from official docs)。若无法找到官方文档，则标记为 medium confidence 并基于 27B 参数量反推验证。

## Corrected Claim

模型结构参数溯源：Qwen3-27B 的 num_layers, hidden_dim, num_kv_heads 等参数应直接引用 Hugging Face 模型卡或官方论文，标记为 high confidence (source: knowledge/derived from official docs)。若无法找到官方文档，则标记为 medium confidence 并基于 27B 参数量反推验证。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B model architecture parameters num_layers hidden_dim
