# N50: Qwen3-27B 的实际 KV 头数 (n_kv_heads) 为 4（而非 N7 假设的 8），头维度 (head_dim) 为 128，层数 (n_lay

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 的实际 KV 头数 (n_kv_heads) 为 4（而非 N7 假设的 8），头维度 (head_dim) 为 128，层数 (n_layers) 为 48，这些参数直接决定 KV Cache 的基准大小。

## Corrected Claim

Qwen3-27B（或 Qwen3.8-27B）采用混合注意力架构，其中 16 层全注意力层的 n_kv_heads 为 4，head_dim 为 256；其余 48 层为线性注意力，不产生传统 KV Cache。

## Evidence

[质询]参数数值与参考来源明确矛盾：来源指出 head_dim 为 256 而非 128，且模型架构为混合注意力（48层线性+16层全注意力），并非所有层都使用相同的 KV 头配置，原陈述将特定层的参数错误地泛化为整个模型的基准参数。 | 来源[2]和[3]明确指出 Qwen3.8-27B 的全注意力层 head_dim 为 256，且仅 16 层为全注意力，其余为线性注意力，与陈述中的 head_dim=128 及隐含的全层统一 KV 结构矛盾。

## Search Query

Qwen3-27B config.json n_kv_heads head_dim n_layers

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liu8485/article/details/164724304&rut=b7c08168b53b511f68674c156d96aa9524b8914fb42107a4a9b9b614dca3f054', 'type': 'ddg', 'title': 'Qwen3.8-27B 混合注意力拆解：48 层线性 + 16 层全注意力，75 万 token KV 显存打到 1/4'}
- {'url': 'https://liminalml.com/concepts/qwen-3-8-27b&rut=e4aa5413bea991ba34a862bca3368466e8a20cf32d7d37e0464362bfc20749e8', 'type': 'ddg', 'title': 'Qwen3.8-27B: Architecture Explained · LiminalML'}
- {'url': 'https://iqilian.com/learn/qwen38-gated-attention-24-4/&rut=b8d57bf65fc987f1601e46625295fe57d16587bac40af590de32690404054dd4', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 GQA：24 个 Q 头配 4 个 KV 头、head_dim 是 256'}
