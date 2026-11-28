# N15: 外部工具调用逻辑需遵循‘最小权限原则’，检索工具返回结果截断至 512 tokens，代码执行结果截断至 2048 tokens，以防止上下文窗口溢出；工具描述

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

外部工具调用逻辑需遵循‘最小权限原则’，检索工具返回结果截断至 512 tokens，代码执行结果截断至 2048 tokens，以防止上下文窗口溢出；工具描述 Prompt 总长度应控制在 500 tokens 以内。

## Corrected Claim

外部工具调用逻辑需遵循‘最小权限原则’，通常会对检索工具和代码执行工具的返回结果进行截断以控制上下文长度，同时建议精简工具描述 Prompt 以避免占用过多上下文窗口。

## Evidence

[质询]具体的截断阈值（512/2048 tokens）和Prompt长度限制（500 tokens）属于特定系统或框架的工程配置参数，并非通用的第一性原理或绝对标准，不同LLM应用架构中这些数值差异巨大，缺乏普适性。 | source=knowledge，逻辑自洽（符合防止上下文溢出的工程直觉），但具体数值为经验性工程参数，非通用真理，且无外部来源支持，故降级为定性表述。

## Search Query

LLM tool use context window management truncation strategy
