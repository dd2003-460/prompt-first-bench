# N93: Qwen3-27B 的 n_layers 确认为 64，依据是 config.json 中 hidden_size=4096 与中间层参数量分布推断，官方技术报

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

Qwen3-27B 的 n_layers 确认为 64，依据是 config.json 中 hidden_size=4096 与中间层参数量分布推断，官方技术报告或 HuggingFace 配置文件可验证

## Corrected Claim

Qwen3-27B 的 n_layers 通常为 64，具体数值需以官方发布的 config.json 或技术报告为准。

## Evidence

[质询]该陈述将具体的架构参数（n_layers=64）归因为从 hidden_size 和参数量分布‘推断’得出，这属于经验事实而非第一性原理推导。虽然 Qwen3-27B 确实有 64 层，但‘依据是...推断’这一归因逻辑在缺乏官方文档直接确认的情况下，存在将推测当作确定事实的风险，且检索无来源支持该特定推断路径。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体配置细节及推断依据的准确性）

## Search Query

Qwen3-27B config.json n_layers
