# N14: 外部工具集成的错误恢复成本：当工具执行失败（如代码运行时错误、检索无结果）时，Agent需进行错误诊断与重试；定义错误率E_tool（典型值5-15%）和平均重

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

外部工具集成的错误恢复成本：当工具执行失败（如代码运行时错误、检索无结果）时，Agent需进行错误诊断与重试；定义错误率E_tool（典型值5-15%）和平均重试次数R_retry（通常1-2次），则工具环节的有效成功率 = 1 - (1 - (1-E_tool))^R_retry；需量化每次失败导致的额外Token消耗（错误日志+修复Prompt）约为正常步骤的1.5-2倍。

## Corrected Claim

外部工具集成的错误恢复成本：当工具执行失败（如代码运行时错误、检索无结果）时，Agent需进行错误诊断与重试；定义错误率E_tool（典型值5-15%）和平均重试次数R_retry（通常1-2次），则工具环节的有效成功率 = 1 - (1 - (1-E_tool))^R_retry；需量化每次失败导致的额外Token消耗（错误日志+修复Prompt）约为正常步骤的1.5-2倍。

## Evidence

先验知识/题面给定，逻辑校验通过
