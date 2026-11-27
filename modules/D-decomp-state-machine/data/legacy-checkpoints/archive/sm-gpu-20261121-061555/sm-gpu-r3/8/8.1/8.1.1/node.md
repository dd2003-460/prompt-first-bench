# N347: Qwen3-27B 模型架构中标准 Multi-Head Attention (MHA) 层的具体数量 L_mha，需从 HuggingFace 配置文件 (c

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N123

## Claim

Qwen3-27B 模型架构中标准 Multi-Head Attention (MHA) 层的具体数量 L_mha，需从 HuggingFace 配置文件 (config.json) 或官方技术报告确认，用于计算 KV Cache 的线性增长部分。

## Corrected Claim

Qwen3-27B 模型架构中标准 Multi-Head Attention (MHA) 层的具体数量 L_mha 需查阅官方技术报告或 HuggingFace 配置文件以获取准确数值，用于计算 KV Cache 的线性增长部分。

## Evidence

[质询]该陈述声称需从特定来源确认具体数值 L_mha，但 Qwen3-27B 的具体架构参数（如 MHA 层数）属于经验事实/硬件规格，且当前检索无可用来源，无法验证具体数值或确认其是否确实需要从 config.json 获取（虽然通常如此，但缺乏直接证据支持该特定模型的配置细节）。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法提供外部证据确认 Qwen3-27B 的具体 MHA 层数或配置获取方式）。

## Search Query

Qwen3-27B config.json num_hidden_layers attention type
