# N55: Qwen3-27B 的权重参数量精确值需确认：'27B' 是约数，实际参数量可能为 26.8B 或 27.2B，BF16 权重占用 = Params * 2 b

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 的权重参数量精确值需确认：'27B' 是约数，实际参数量可能为 26.8B 或 27.2B，BF16 权重占用 = Params * 2 bytes。若 Params=27.2B，则权重占用 54.4 GB。此外，需考虑 Embedding 层和 LM Head 的参数量是否包含在 27B 中，通常不包含，需额外增加约 1-2 GB 显存。

## Corrected Claim

Qwen3-27B 的 '27B' 为约数，实际参数量需查阅官方技术报告确认。BF16 权重占用约为 54 GB 左右。关于 Embedding 层和 LM Head 是否计入总参数量，不同统计口径可能有差异，需额外预留显存空间以应对潜在偏差。

## Evidence

[质询]该陈述包含具体的硬件/模型规格经验事实（如参数量精确值、显存占用计算、Embedding/LM Head 是否计入总参数量的惯例），这些无法从第一性原理严格推导，且缺乏来源支持。特别是关于'通常不包含'Embedding/LM Head的说法，在不同模型架构和统计口径下存在差异，属于经验性断言。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B exact parameter count embedding layer size BF16 memory footprint
