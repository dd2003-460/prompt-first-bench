# N296: Qwen3-27B 在 GPTQ-INT8, group_size=64 配置下，WikiText2 Perplexity 绝对值通常升至 5.9-6.0，相比

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

Qwen3-27B 在 GPTQ-INT8, group_size=64 配置下，WikiText2 Perplexity 绝对值通常升至 5.9-6.0，相比 BF16 基准 (5.6) 增加约 5.4-7.1%，超过 N98 定义的 5% 可接受阈值，需标记为质量损失不可接受。

## Corrected Claim

Qwen3-27B 在 GPTQ-INT8, group_size=64 配置下，WikiText2 Perplexity 通常会出现一定程度的上升（例如从 BF16 基准的约 5.6 升至 5.9-6.0 区间），增幅可能超过 5% 的可接受阈值，具体数值需以实际量化实验结果为准。

## Evidence

[质询]具体数值（5.9-6.0, 5.6）及百分比增幅属于特定实验条件下的经验数据，缺乏通用性，且不同量化实现（如GPTQ vs AWQ）或数据集版本可能导致结果波动，无法仅凭逻辑推导确定具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化后的Perplexity数值属于经验参数，不适用第一性原理推导条款）

## Search Query

Qwen3-27B GPTQ INT8 group_size 64 WikiText2 perplexity degradation
