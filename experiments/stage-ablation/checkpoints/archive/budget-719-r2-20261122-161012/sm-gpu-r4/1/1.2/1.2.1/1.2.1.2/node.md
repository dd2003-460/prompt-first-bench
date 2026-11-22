# N145: Qwen3-27B 的 head_dim 维度：通常为 128 或 160，结合 num_kv_heads 可计算出单层 KV Cache 大小，进而乘以 64

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B 的 head_dim 维度：通常为 128 或 160，结合 num_kv_heads 可计算出单层 KV Cache 大小，进而乘以 64 层得到总 KV Cache 大小

## Corrected Claim

Qwen3-27B（或 Qwen3.8-27B）的 head_dim 维度为 256，结合 num_kv_heads（4）可计算出单层 KV Cache 大小，进而乘以 64 层得到总 KV Cache 大小。

## Evidence

[质询]陈述中关于 head_dim 的数值（128 或 160）与参考来源 [3] 中明确指出的 Qwen3.8-27B 的 head_dim 为 256 直接矛盾。 | 来源 [3] 明确指出 Qwen3.8-27B 的 head_dim 是 256，而非陈述中的 128 或 160，导致基于错误 head_dim 计算的 KV Cache 大小也是错误的。

## Search Query

Qwen3-27B head_dim hidden_size configuration

## Retrieval Sources

- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e5459bd6ec62e1937706a05f835d37baa128ee9ce9105b7cdd4ee711d207a8ed', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
- {'url': 'https://blog.csdn.net/yuzhou164/article/details/149415802&rut=67e85dff2744ef68279992ef43bf4d00355905afa718982c679676ba3ebe7a98', 'type': 'ddg', 'title': 'Qwen系列的模型 config 参数理解_qwen3config-CSDN博客'}
- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=576e3d11a5501e4ae9573a03f4621866501ddfed510ba56bae9e3f480f4eb106', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
