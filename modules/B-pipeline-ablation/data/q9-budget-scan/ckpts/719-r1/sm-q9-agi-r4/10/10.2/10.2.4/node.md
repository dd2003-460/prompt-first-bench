# N305: 执行日志 (Execution Log) 与结果解析 (Result Analysis) 的 Token 上限：若实验输出为标准 JSON 格式，结果解析平均消

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

执行日志 (Execution Log) 与结果解析 (Result Analysis) 的 Token 上限：若实验输出为标准 JSON 格式，结果解析平均消耗约 1000-1500 tokens；需定义日志截断策略，当原始日志超过 2000 tokens 时仅保留关键异常堆栈和最终数值结果

## Corrected Claim

执行日志 (Execution Log) 与结果解析 (Result Analysis) 的 Token 上限：若实验输出为标准 JSON 格式，结果解析平均消耗约 1000-1500 tokens；需定义日志截断策略，当原始日志超过 2000 tokens 时仅保留关键异常堆栈和最终数值结果

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM context window management execution log truncation strategy
