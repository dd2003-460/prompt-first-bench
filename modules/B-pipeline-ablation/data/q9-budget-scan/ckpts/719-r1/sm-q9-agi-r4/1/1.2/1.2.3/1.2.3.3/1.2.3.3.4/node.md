# N400: Syntax_Error_Rate 的自动检测器精度：使用 tree-sitter 解析代码块，语法错误率 Syntax_Err = Parse_Failure

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131, N134, N135

## Claim

Syntax_Error_Rate 的自动检测器精度：使用 tree-sitter 解析代码块，语法错误率 Syntax_Err = Parse_Failures / Total_Code_Blocks；在 HumanEval 数据集上，tree-sitter 的 False Positive Rate（将正确代码误判为错误）约为 0.5%-1%，False Negative Rate 约为 0.1%-0.3%，需校准阈值以消除解析器噪音

## Corrected Claim

Syntax_Error_Rate 的自动检测器精度：使用 tree-sitter 解析代码块，语法错误率 Syntax_Err = Parse_Failures / Total_Code_Blocks；在 HumanEval 数据集上，tree-sitter 存在少量误报（False Positive）和漏报（False Negative），需根据具体编程语言和代码特征校准阈值以消除解析器噪音。

## Evidence

[质询]具体的 FPR (0.5%-1%) 和 FNR (0.1%-0.3%) 数值缺乏公开权威基准支持，属于特定实验条件下的经验数据，不同语言、代码复杂度及 tree-sitter 版本下波动较大，直接断言固定区间存在过度精确化风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值非第一性原理可推导）。

## Search Query

tree-sitter parser error detection accuracy code generation benchmark
