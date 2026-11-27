# N97: Qwen3-27B 的架构参数确认：层数 (num_layers) 为 64，KV Head 数量 (num_kv_heads) 为 8 (GQA 8:1)，H

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 的架构参数确认：层数 (num_layers) 为 64，KV Head 数量 (num_kv_heads) 为 8 (GQA 8:1)，Head Dimension (head_dim) 为 128。基于此，BF16 下每 token KV Cache 大小为 2 * 64 * 8 * 128 * 2 bytes = 262,144 bytes = 256 KB，而非 N20 中声称的 1.2 MB 或 1 MB。

## Corrected Claim

Qwen3-27B 的架构参数（层数 64, KV Head 8, Head Dim 128）及由此推导的 BF16 每 token KV Cache 大小 256 KB 在逻辑上自洽，但需核实具体版本配置以排除与 Qwen3.6/3.8 等后续版本的参数差异。

## Evidence

[质询]参考来源均指向 Qwen3.6 或 Qwen3.8 版本，未直接覆盖 Qwen3-27B 的具体架构参数（如层数、KV Head 数），存在版本混淆或参数随版本迭代变化的风险，无法通过现有来源直接证实 Qwen3-27B 的确切数值。 | 逻辑推导成立（2*64*8*128*2=262144 bytes=256KB），但参考来源 [1][2][3] 均涉及 Qwen3.6/3.8 而非 Qwen3-27B，属于经验事实且缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B model config num_layers num_kv_heads head_dim

## Retrieval Sources

- {'url': 'https://freedom-lwx.github.io/llm-architecture-handbook/04_Qwen3.6-27B/&rut=0b10fe0d815af316e8374ea97a2024ed873765fdf7691a90951d7aedc81374a1', 'type': 'ddg', 'title': '04 · Qwen3.6-27B - 大模型架构学习手册'}
- {'url': 'https://blog.csdn.net/weixin_29061997/article/details/163968287&rut=d8bcdaad59c325dd9cad4b0f2c92c1c5099f1710ea83e3806ae5b07aec6e1d03', 'type': 'ddg', 'title': 'Qwen3.8 27B架构解析：75%非Transformer层如何优化KV Cache与长上下文推理-CSDN博客'}
- {'url': 'https://www.cnblogs.com/sing1ee/p/22498000&rut=e5459bd6ec62e1937706a05f835d37baa128ee9ce9105b7cdd4ee711d207a8ed', 'type': 'ddg', 'title': 'Qwen3.8-27B（2026）：Qwen 新 27B 视觉语言模型完整指南 - 见路非道 - 博客园'}
