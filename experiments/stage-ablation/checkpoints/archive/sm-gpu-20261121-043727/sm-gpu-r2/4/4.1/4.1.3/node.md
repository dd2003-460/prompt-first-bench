# N64: 分析 Grouped Query Attention (GQA) 对显存占用的缩减系数：若 Qwen3-27B 采用 GQA，KV Cache 占用 = MHA

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

分析 Grouped Query Attention (GQA) 对显存占用的缩减系数：若 Qwen3-27B 采用 GQA，KV Cache 占用 = MHA_Occupancy * (Num_KV_Heads / Num_Query_Heads)；需确认该比例因子（例如 1:4 或 1:8），并量化其相对于标准 MHA 节省的显存 GB 数。

## Corrected Claim

GQA 通过共享 KV Head 减少显存占用，其占用量与 KV Head 数量成正比。具体到 Qwen3-27B 的比例因子及节省的显存 GB 数需查阅该模型的具体技术报告或配置文档，当前来源未提供此量化数据。

## Evidence

[质询]该陈述包含具体的经验事实参数（Qwen3-27B 的 GQA 比例因子及具体节省的显存 GB 数），这些无法从第一性原理推导，且参考来源仅提供了 GQA 的通用原理，未提供 Qwen3-27B 的具体配置数据或量化结果，存在来源缺失风险。 | 逻辑自洽：GQA 通过共享 KV Head 减少显存占用，公式 KV_Occupancy = MHA_Occupancy * (Num_KV_Heads / Num_Query_Heads) 符合定义。但参考来源 [1] 仅解释 GQA 原理，未提供 Qwen3-27B 的具体比例（如 1:4 或 1:8）及量化节省的 GB 数，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B GQA ratio num_query_heads num_key_value_heads

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1983147571192026634&rut=47cc625bc7f8283cda24cef2ea4bb3040e47b6843e3150bc8a16e7f0f3d81c37', 'type': 'ddg', 'title': 'GQA（Grouped Query Attention）：为什么它能显著减少显存？'}
