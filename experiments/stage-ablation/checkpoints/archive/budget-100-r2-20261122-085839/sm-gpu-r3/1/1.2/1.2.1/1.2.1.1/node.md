# N128: Qwen3-27B 配置文件中 num_attention_heads（总注意力头数）的具体数值，需从 config.json 获取，常见值为 32 或 40，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

Qwen3-27B 配置文件中 num_attention_heads（总注意力头数）的具体数值，需从 config.json 获取，常见值为 32 或 40，用于计算 Attention 矩阵维度。

## Corrected Claim

Qwen3-27B 配置文件中 num_attention_heads 的具体数值需从 config.json 获取，常见值可能在 32 或 40 左右，用于计算 Attention 矩阵维度。

## Evidence

[质询]具体数值（32或40）属于经验事实，且不同版本或变体可能不同，仅凭逻辑无法确定唯一值，存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_attention_heads
