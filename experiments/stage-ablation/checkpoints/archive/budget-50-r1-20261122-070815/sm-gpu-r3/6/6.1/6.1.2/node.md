# N362: Qwen3-27B 的总参数量（Total Parameters）是否确为 27.4B 或 27.0B，需通过计算模型结构（Embedding + 64 Lay

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N127

## Claim

Qwen3-27B 的总参数量（Total Parameters）是否确为 27.4B 或 27.0B，需通过计算模型结构（Embedding + 64 Layers * (QKV + FFN + Norm) + Output Head）或查阅官方技术报告中的参数量表格来验证，以确认 '27B' 标签的准确性。

## Corrected Claim

Qwen3-27B 的总参数量约为 27B，具体数值（如 27.4B 或 27.0B）需查阅官方技术报告确认。

## Evidence

[质询]该陈述包含具体的硬件/模型规格参数（27.4B/27.0B），属于经验事实，无法仅通过逻辑推导或第一性原理得出确切数值，且缺乏官方技术报告或可靠来源的直接支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体参数量数值）

## Search Query

Qwen3-27B total parameters count technical report
