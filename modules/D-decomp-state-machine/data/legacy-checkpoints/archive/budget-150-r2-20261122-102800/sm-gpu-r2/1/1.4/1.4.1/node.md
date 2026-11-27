# N63: Qwen3-27B 架构参数：num_hidden_layers=64, num_key_value_heads=8, head_dim=128 (hidden

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N11

## Claim

Qwen3-27B 架构参数：num_hidden_layers=64, num_key_value_heads=8, head_dim=128 (hidden_size=1024)。

## Corrected Claim

Qwen3-27B 架构参数：num_hidden_layers=64, hidden_size=5120，采用混合架构（包含 Gated DeltaNet 和 Gated Attention 单元）。

## Evidence

[质询]数值量级与架构细节严重错误：参考来源明确指出 Qwen3 系列 27B 模型的 hidden_size 为 5120（而非 1024），且采用混合架构（Gated DeltaNet + Gated Attention），并非陈述中描述的纯 Transformer 架构参数（head_dim=128 等）。 | 来源 [1] 和 [2] 均显示 Qwen3-27B 的 hidden_size 为 5120，层数为 64，但架构为混合布局，与陈述中的 hidden_size=1024 及纯 Transformer 参数描述矛盾。

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads head_dim

## Retrieval Sources

- {'url': 'https://catalog.ngc.nvidia.com/orgs/nim/qwen/models/qwen3.8-27b/&rut=4b010b8cdebd61b7e07ac43df46fbf23a3d08cc308fa4e320e6179be74b40215', 'type': 'ddg', 'title': 'Qwen3.8-27B | NVIDIA NGC'}
- {'url': 'https://zhuanlan.zhihu.com/p/2010079474104963160&rut=336d25a4988526b6be857ced6e5fc040a0f025afaa4a16b40b3bafb074499abe', 'type': 'ddg', 'title': 'Qwen/Qwen3.5-27B模型结构（dense）分析 - 知乎'}
