# N22: 代码解释器工具的标准接口定义为 execute_code(code_str, timeout_sec) -> {stdout, stderr, exit_cod

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

代码解释器工具的标准接口定义为 execute_code(code_str, timeout_sec) -> {stdout, stderr, exit_code}，其中 timeout_sec 默认值为 300秒，exit_code=0 表示成功

## Corrected Claim

代码解释器工具的标准接口定义为 execute_code(code_str, timeout_sec) -> {stdout, stderr, exit_code}，其中 timeout_sec 默认值为 300秒，exit_code=0 表示成功

## Evidence

先验知识/题面给定，逻辑校验通过
