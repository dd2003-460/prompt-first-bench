# N57: Qwen3-27B 的 Query 头数 (Num_Heads) 确切值为 32，来源于模型配置文件中 num_attention_heads 字段。

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 的 Query 头数 (Num_Heads) 确切值为 32，来源于模型配置文件中 num_attention_heads 字段。

## Corrected Claim

Qwen3.8-27B 的 Query 头数 (Num_Heads) 确切值为 24，来源于模型配置文件中 num_attention_heads 字段。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 7 column 5 (char 871)

## Search Query

Qwen3-27B num_attention_heads 32

## Retrieval Sources

- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=920149c9eacc4d20f658754f4ff8d599bd3dfa5b96c05e760d3ce5d720c6cea4', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
- {'url': 'https://iqilian.com/learn/qwen38-xianxing-zhuyili-canshu/&rut=e5633a880366b3ed282d560cf8d21faab59c5739f4556886de101e8d155ed385', 'type': 'ddg', 'title': 'Qwen3.8-27B 的线性注意力参数：卷积核宽度与 key/value 头数'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=014253cab1362304bedfb232983060c3a30c933f269dd0e576935f19f65c4b6e', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
