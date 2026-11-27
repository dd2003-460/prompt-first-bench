# N293: Qwen3-27B 的 `hidden_size` 为 4096，`intermediate_size` (FFN 宽度) 为 13312，用于验证权重参数量估

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

Qwen3-27B 的 `hidden_size` 为 4096，`intermediate_size` (FFN 宽度) 为 13312，用于验证权重参数量估算是否准确。

## Corrected Claim

Qwen3-27B 的 `hidden_size` 和 `intermediate_size` 具体数值需查阅官方模型配置文件（config.json）以确认，当前陈述基于常见大模型架构比例推测，但缺乏直接来源佐证。

## Evidence

[质询]该陈述属于具体的硬件/模型架构规格（经验事实），且参考来源全部缺失，无法通过外部检索直接验证 `hidden_size` 和 `intermediate_size` 的具体数值是否准确。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法排除数值错误的可能性）

## Search Query

Qwen3-27B hidden_size intermediate_size model architecture parameters
