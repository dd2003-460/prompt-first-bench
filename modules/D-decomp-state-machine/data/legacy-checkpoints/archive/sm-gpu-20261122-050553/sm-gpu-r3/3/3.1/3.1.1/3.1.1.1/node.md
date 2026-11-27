# N191: Qwen3-27B 的架构参数 N_layers（层数）需确认为 64 层，这是计算 KV Cache 的基础参数，需引用 Qwen3 官方模型配置文件（con

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Qwen3-27B 的架构参数 N_layers（层数）需确认为 64 层，这是计算 KV Cache 的基础参数，需引用 Qwen3 官方模型配置文件（config.json）或技术报告中的具体数值。

## Corrected Claim

Qwen3-27B 的架构参数 N_layers 推测为 64 层（基于 Qwen2.5-32B 架构），需引用 Qwen3 官方模型配置文件（config.json）或技术报告中的具体数值以最终确认。

## Evidence

[质询]该陈述属于具体的硬件/模型架构经验事实（层数），无法从第一性原理推导。虽然 Qwen3-27B 基于 Qwen2.5-32B 架构，层数极大概率为 64，但在缺乏官方 config.json 或技术报告直接引用的情况下，存在因版本迭代或微调导致参数变更的微小可能性，且当前检索无可用来源支持。 | 经验事实，逻辑自洽（基于 Qwen2.5-32B 架构推断）但缺来源支持，检索无可用来源。

## Search Query

Qwen3-27B config.json num_hidden_layers 64
