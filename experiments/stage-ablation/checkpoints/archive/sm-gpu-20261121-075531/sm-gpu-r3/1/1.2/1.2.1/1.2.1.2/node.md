# N139: Qwen3-27B 的 KV Head 数量 (num_key_value_heads) 确认为 4 个，采用 GQA (Grouped Query Atten

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Qwen3-27B 的 KV Head 数量 (num_key_value_heads) 确认为 4 个，采用 GQA (Grouped Query Attention) 结构，而非 MHA 或假设的 16 个 KV Heads。

## Corrected Claim

Qwen3-27B 采用 GQA (Grouped Query Attention) 结构，其 KV Head 数量 (num_key_value_heads) 通常配置为 4 个（需以官方模型配置文件为准）。

## Evidence

[质询]该陈述属于具体的硬件/模型架构规格（经验事实），且参考来源全部缺失，无法通过外部检索直接验证 num_key_value_heads 的确切数值（4 vs 其他值），存在数值记忆偏差或版本混淆的风险。 | 经验事实，逻辑自洽（GQA结构下KV Heads少于Query Heads符合常规设计），但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B config.json num_key_value_heads GQA
