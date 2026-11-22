# N125: Qwen3-27B 的 num_layers（层数）具体数值，需从 HuggingFace 官方模型卡 config.json 或技术报告中检索，该值是计算 K

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

Qwen3-27B 的 num_layers（层数）具体数值，需从 HuggingFace 官方模型卡 config.json 或技术报告中检索，该值是计算 KV Cache 显存占用的核心参数之一。

## Corrected Claim

Qwen3-27B 的 num_layers 是计算 KV Cache 显存占用的核心参数之一，具体数值需查阅 HuggingFace 官方模型卡 config.json 或技术报告。

## Evidence

[质询]该陈述声称具体数值需从外部检索，属于经验事实（具体参数值），且当前无可用来源支持，无法验证其具体数值或确认其是否为计算KV Cache的核心参数（虽然逻辑上合理，但缺乏实证）。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B config.json num_layers
