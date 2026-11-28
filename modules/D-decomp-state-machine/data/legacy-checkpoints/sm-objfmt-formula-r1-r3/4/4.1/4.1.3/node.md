# N79: Qwen3-27B 的 Key Value Head 数量 (num_kv_heads) 确认为 4 (基于 GQA 架构)，用于计算每层 KV 缓存大小

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

Qwen3-27B 的 Key Value Head 数量 (num_kv_heads) 确认为 4 (基于 GQA 架构)，用于计算每层 KV 缓存大小

## Corrected Claim

Qwen3-27B 采用 GQA 架构，其 Key Value Head 数量 (num_kv_heads) 推测为 4（需进一步核实具体配置文件以确认精确数值）。

## Evidence

[质询]具体数值（4）属于经验事实/模型配置参数，无法从第一性原理推导，且当前无可用外部来源验证该特定版本的具体配置，存在与其他变体（如非GQA或不同KV头数配置）混淆的风险。 | 经验事实，逻辑自洽（GQA架构下KV头数少于Query头数是常见设计，4是一个合理的量级），但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B config.json num_key_value_heads
