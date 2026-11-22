# N130: Qwen3-27B 的 num_hidden_layers 确切值为 64，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 confi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B 的 num_hidden_layers 确切值为 64，依据 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件。

## Corrected Claim

Qwen3-27B 的 num_hidden_layers 通常被报告为 64，但需以 HuggingFace 官方仓库 Qwen/Qwen3-27B 的 config.json 文件实时数据为准。

## Evidence

[质询]无法通过外部检索直接验证 HuggingFace 官方仓库 config.json 的具体数值，存在记忆偏差或版本更新导致数值不符的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法确认具体配置参数）

## Search Query

Qwen3-27B config.json num_hidden_layers site:huggingface.co
