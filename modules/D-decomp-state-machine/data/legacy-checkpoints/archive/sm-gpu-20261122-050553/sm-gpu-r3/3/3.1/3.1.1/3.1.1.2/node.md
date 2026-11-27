# N192: Qwen3-27B 的架构参数 N_kv_heads（KV 头数）需确认为 8 个（基于 GQA 分组查询注意力，假设 GQA 组数为 4，即 32 个 Q 头

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

Qwen3-27B 的架构参数 N_kv_heads（KV 头数）需确认为 8 个（基于 GQA 分组查询注意力，假设 GQA 组数为 4，即 32 个 Q 头 / 4 = 8 个 KV 头），需引用官方配置确认 GQA 的具体分组策略。

## Corrected Claim

Qwen3-27B 采用 GQA 架构，若 Q 头数为 32 且 GQA 组数为 4，则 KV 头数为 8；具体数值需以官方模型配置文件为准。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（N_kv_heads=8, GQA组数=4），属于经验事实。虽然逻辑上 32/4=8 自洽，但缺乏官方配置文件的直接证据支持，且不同版本或变体可能存在差异，不能仅凭逻辑推导确认为唯一事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体配置值）

## Search Query

Qwen3-27B num_key_value_heads GQA grouped query attention
