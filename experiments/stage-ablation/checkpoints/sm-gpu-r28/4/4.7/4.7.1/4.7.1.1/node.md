# N236: Qwen3-27B 的架构参数：n_layers = 64, n_heads = 32, head_dim = 128 (基于 Qwen2-72B/27B 系列

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

Qwen3-27B 的架构参数：n_layers = 64, n_heads = 32, head_dim = 128 (基于 Qwen2-72B/27B 系列常见配置推断，需官方确认)，BF16 权重大小 = 27e9 * 2 bytes = 54 GB。

## Corrected Claim

Qwen3-27B 的 BF16 权重大小约为 54 GB（基于 27B 参数量估算）。其具体架构参数（n_layers, n_heads, head_dim）需查阅官方技术报告或模型配置文件确认，当前基于 Qwen2 系列的推断仅供参考。

## Evidence

[质询]该陈述明确标注为“基于推断，需官方确认”，且参考来源中完全未包含 Qwen3-27B 的架构参数（n_layers, n_heads, head_dim）。对于具体的硬件/模型架构规格（经验事实），缺乏直接来源支持，且“推断”本身存在不确定性（例如 Qwen2-72B 的 head_dim 通常为 128，但 n_heads 和 n_layers 的具体组合需核实，且 Qwen3 系列可能引入新的架构变更如 GQA 比例变化等）。 | 经验事实，逻辑自洽（27e9 * 2 bytes = 54 GB 计算正确），但参考来源 [1]-[4] 均与 Qwen3-27B 架构无关，无直接来源支持具体参数值，故降级。

## Search Query

Qwen3-27B model card n_layers n_heads head_dim architecture

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/1712.10314v1', 'type': 'arxiv', 'title': 'Exclusive photoproduction of $π^0$ up to large values of Mandelstam variables $s'}
- {'url': 'http://arxiv.org/abs/2606.30037v1', 'type': 'arxiv', 'title': 'Heads, Not Backbones: Output Heads Dominate Architectures on Fat-Tailed Returns'}
- {'url': 'http://arxiv.org/abs/2504.03889v4', 'type': 'arxiv', 'title': 'Identifying and Evaluating Inactive Heads in Pretrained LLMs'}
