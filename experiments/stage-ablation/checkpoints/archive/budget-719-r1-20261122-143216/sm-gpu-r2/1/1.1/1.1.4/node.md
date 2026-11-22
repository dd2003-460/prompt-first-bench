# N39: Qwen3-27B 的 head_dim（头维度）具体数值，通常由 hidden_size / num_attention_heads 得出，需确认是否为标准 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的 head_dim（头维度）具体数值，通常由 hidden_size / num_attention_heads 得出，需确认是否为标准 128 或非标准值。

## Corrected Claim

Qwen3-27B 的 head_dim 通常由 hidden_size / num_attention_heads 得出，具体数值需查阅官方模型配置以确认是否为标准 128 或非标准值。

## Evidence

[质询]该陈述涉及具体模型（Qwen3-27B）的架构参数（head_dim），属于经验事实。虽然通常由 hidden_size / num_attention_heads 计算得出，但不同模型版本或特定配置下可能存在非标准值（如 GQA 或 MLA 架构下的差异），且当前无来源确认 Qwen3-27B 的具体 hidden_size 和 num_heads 数值，无法排除其为非标准值（如 128 以外的值）的可能性。 | 经验事实，逻辑自洽（head_dim 通常由 hidden_size / num_heads 决定）但缺来源支持，无法确认具体数值是否为 128。

## Search Query

Qwen3-27B head_dim hidden_size num_attention_heads config.json
