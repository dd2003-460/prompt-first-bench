# N144: Qwen3-27B 的 num_kv_heads 数量：若采用 GQA (Grouped Query Attention)，num_kv_heads 小于 nu

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B 的 num_kv_heads 数量：若采用 GQA (Grouped Query Attention)，num_kv_heads 小于 num_heads，这将直接降低 KV Cache 大小。需确认 Qwen3-27B 的具体 GQA 组数（例如 8 组或 16 组）

## Corrected Claim

若指 Qwen3.8-27B，其采用 GQA，num_kv_heads 为 4（num_heads 为 24）；若指标准 Qwen3 系列其他型号，需具体确认版本号，但 GQA 机制确实会降低 KV Cache 大小。

## Evidence

[质询]参考来源均指向 'Qwen3.8-27B' 而非 'Qwen3-27B'，存在模型版本/命名混淆的风险；且来源 [1] 给出的具体数值（24 Q heads, 4 KV heads）与常见的 Qwen3 系列配置（如 Qwen3-32B 为 64 Q, 8 KV）差异巨大，若 'Qwen3-27B' 实为 'Qwen3-32B' 的误写或 'Qwen3.8' 为特定变体，则直接引用该数值可能错误。 | 来源 [1] 明确给出了 'Qwen3.8-27B' 的 GQA 配置为 24 个 Q 头配 4 个 KV 头，逻辑上支持 GQA 降低 KV Cache 的结论，但模型名称与查询中的 'Qwen3-27B' 不完全一致（多了一个 .8），且缺乏针对 'Qwen3-27B' 这一确切名称的直接独立来源确认，故降级。

## Search Query

Qwen3-27B GQA num_kv_heads configuration

## Retrieval Sources

- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=576e3d11a5501e4ae9573a03f4621866501ddfed510ba56bae9e3f480f4eb106', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
- {'url': 'https://blog.csdn.net/Zidian632/article/details/164885586&rut=126224fc7711d38d76a7862f8fe70255055c3d72f919a7e6c06beea8c5007460', 'type': 'ddg', 'title': 'Qwen3.8-27B 上下文与显存配置对照表：16G-96G 分档计算 + 实测验证（附 KV 占用系数）'}
- {'url': 'https://apxml.com/models/qwen38-27b&rut=1624baae322bf4ddad7e27a6ffb5bbbb009f2d9bd8c585395db6c06a6dc22c74', 'type': 'ddg', 'title': 'Qwen 3.8 27B - VRAM Requirements, Specs & Benchmarks'}
