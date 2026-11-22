# N31: Qwen3-27B 架构参数基线：具体层数 (num_layers)、KV头数 (num_kv_heads) 及头维度 (head_dim) 的精确数值，用于将

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 架构参数基线：具体层数 (num_layers)、KV头数 (num_kv_heads) 及头维度 (head_dim) 的精确数值，用于将 KV Cache 公式从定性描述转化为具体的 GB 数值计算（例如：若为 GQA 架构，KV头数通常远小于注意力头数，显著降低显存占用）。

## Corrected Claim

Qwen3-27B（或相关版本如 Qwen3.8-27B）采用 GQA 架构，其 KV 头数小于注意力头数以优化显存，但具体层数、KV头数及头维度需查阅官方模型配置文件（config.json）以获取精确数值。

## Evidence

[质询]参考来源均指向 'Qwen3.8' 或 'Qwen3.8-27B'，而非 'Qwen3-27B'。Qwen3 系列（如 Qwen3-235B-A22B 或 Qwen3-32B）与 Qwen3.8（若存在）或 Qwen2.5 系列在架构参数（如层数、KV头数）上可能存在差异。此外，来源摘要主要讨论 MoE 和线性注意力对 KV Cache 的优化，未直接提供 Qwen3-27B 的具体 num_layers, num_kv_heads, head_dim 数值，存在版本混淆和具体参数缺失的风险。 | 来源 [1][2][3] 均提及 'Qwen3.8' 或 'Qwen3.8-27B'，与事实节点中的 'Qwen3-27B' 名称不完全匹配，且摘要中未包含具体的架构参数数值（num_layers, num_kv_heads, head_dim），无法直接支持该具体数值事实，属于间接相关或版本存疑。

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29051193/article/details/163968270&rut=ade46d5d32e2befed8aa4477708d39cad081b45bcdfd3e9738c3fd952bd590af', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：MoE与线性注意力如何实现百万上下文-CSDN博客'}
- {'url': 'https://blog.csdn.net/weixin_29061997/article/details/163968287&rut=d8bcdaad59c325dd9cad4b0f2c92c1c5099f1710ea83e3806ae5b07aec6e1d03', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：75%非Transformer层如何优化KV Cache与长上下文推理-CSDN博客'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e5459bd6ec62e1937706a05f835d37baa128ee9ce9105b7cdd4ee711d207a8ed', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
