# N232: 长上下文稳定性指标：P99 延迟方差 < 5ms 的实测数据来源及测试条件（如 batch size, sequence length 分布），用于验证其相对于

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N75

## Claim

长上下文稳定性指标：P99 延迟方差 < 5ms 的实测数据来源及测试条件（如 batch size, sequence length 分布），用于验证其相对于多卡方案的稳定性优势。

## Corrected Claim

长上下文稳定性指标：P99 延迟方差显著低于多卡方案（具体阈值如 < 5ms 需依据特定硬件与负载实测数据确认），测试条件需明确 batch size 与 sequence length 分布。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（P99 延迟方差 < 5ms）及特定的测试条件（batch size, sequence length 分布），属于硬件/系统性能实测数据，无法从第一性原理推导，且缺乏来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

A100 80GB LLM inference P99 latency variance 32k context
