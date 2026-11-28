# N120: 工具调用接口的标准化协议定义：采用JSON-Schema定义的Function Calling接口，每个工具(tool_id)必须包含 `input_schem

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

工具调用接口的标准化协议定义：采用JSON-Schema定义的Function Calling接口，每个工具(tool_id)必须包含 `input_schema` (Pydantic模型) 和 `output_schema`；对于代码执行工具，强制要求返回结构包含 `stdout`, `stderr`, `exit_code` 和 `resource_usage` (CPU_time, mem_peak)，以便后续分析模块进行异常检测，该协议确保工具调用的幂等性与可追溯性。

## Corrected Claim

工具调用接口的标准化协议定义：采用JSON-Schema定义的Function Calling接口，每个工具(tool_id)必须包含 `input_schema` (Pydantic模型) 和 `output_schema`；对于代码执行工具，强制要求返回结构包含 `stdout`, `stderr`, `exit_code` 和 `resource_usage` (CPU_time, mem_peak)，以便后续分析模块进行异常检测，该协议确保工具调用的幂等性与可追溯性。

## Evidence

检索失败: no sources from any channel (all 5 failed)
