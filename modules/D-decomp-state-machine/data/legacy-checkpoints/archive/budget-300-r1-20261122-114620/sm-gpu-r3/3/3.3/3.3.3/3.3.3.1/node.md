# N295: Qwen3-27B 在 AWQ-INT8, group_size=128 配置下，WikiText2 Perplexity 绝对值通常在 5.7-5.8 之间，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

Qwen3-27B 在 AWQ-INT8, group_size=128 配置下，WikiText2 Perplexity 绝对值通常在 5.7-5.8 之间，相比 BF16 基准 (5.6) 增加约 1.8-3.6%，满足 N98 定义的 <5% 阈值。

## Corrected Claim

Qwen3-27B 在 AWQ-INT8, group_size=128 配置下，WikiText2 Perplexity 通常会有轻微上升，相比 BF16 基准的增幅通常小于 5%。

## Evidence

[质询]具体数值（5.7-5.8）及百分比增幅（1.8-3.6%）属于特定模型在特定量化配置下的经验测量结果，无法从第一性原理推导，且缺乏来源支持以确认其精确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT8 group_size 128 WikiText2 perplexity benchmark
