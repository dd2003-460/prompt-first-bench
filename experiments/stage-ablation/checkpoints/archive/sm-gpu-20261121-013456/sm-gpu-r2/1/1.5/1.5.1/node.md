# N57: Qwen3-27B 的 Query 头数 (Num_Heads) 确切值为 32，来源于模型配置文件中 num_attention_heads 字段。

- **status**: degraded
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

[质询]模型名称与参数不匹配：参考来源均指向 'Qwen3.8-27B'（或 Qwen3 系列后续版本），其 Query 头数为 24（来源[1]），而非 32。陈述中的 'Qwen3-27B' 若指代同一模型，则数值错误；若指代早期 Qwen3 版本，来源未覆盖且与当前主流 27B 规格（24头）存在显著差异，且来源明确显示 27B 级别模型采用 24 头配置。 | 来源[1]明确指出 Qwen3.8-27B 的 GQA 配置为 24 个 Q 头，与陈述中的 32 头直接矛盾。

## Search Query

Qwen3-27B num_attention_heads 32

## Retrieval Sources

- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=920149c9eacc4d20f658754f4ff8d599bd3dfa5b96c05e760d3ce5d720c6cea4', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
- {'url': 'https://iqilian.com/learn/qwen38-xianxing-zhuyili-canshu/&rut=e5633a880366b3ed282d560cf8d21faab59c5739f4556886de101e8d155ed385', 'type': 'ddg', 'title': 'Qwen3.8-27B 的线性注意力参数：卷积核宽度与 key/value 头数'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=014253cab1362304bedfb232983060c3a30c933f269dd0e576935f19f65c4b6e', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
