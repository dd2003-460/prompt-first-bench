# N103: 代码规范约束对 FPSR 的提升：在 Prompt 中强制要求使用类型提示（Type Hints）和 Docstring 可将 FPSR 提升 5-8 个百分点

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

代码规范约束对 FPSR 的提升：在 Prompt 中强制要求使用类型提示（Type Hints）和 Docstring 可将 FPSR 提升 5-8 个百分点（从 ~65% 提升至 ~72%），因为静态分析器能在执行前捕获 30% 的潜在类型错误。该优化的一次性 Prompt 工程成本可忽略不计，ROI 极高，应作为默认配置。

## Corrected Claim

在 Prompt 中强制要求使用类型提示（Type Hints）和 Docstring 通常能提升代码质量并降低运行时错误率，因为静态分析器可在执行前捕获部分潜在类型错误。该优化的一次性 Prompt 工程成本较低，建议作为默认配置以提升代码健壮性。

## Evidence

[质询]具体数值（FPSR提升5-8个百分点、静态分析捕获30%错误）缺乏通用基准支持，属于特定实验条件下的经验数据，易受模型版本、任务复杂度及评估指标定义影响，存在过拟合或特定场景偏差风险。 | 逻辑自洽（类型提示有助于静态分析从而减少运行时错误），但具体量化指标（5-8%提升、30%捕获率）为经验事实，无来源支持且非第一性原理可推导，故降级。
