# N130: 静态语法检查的量化通过标准：使用 AST (Abstract Syntax Tree) 解析器，要求 Parse_Error_Count = 0 且 Undef

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

静态语法检查的量化通过标准：使用 AST (Abstract Syntax Tree) 解析器，要求 Parse_Error_Count = 0 且 Undefined_Name_Count = 0；若检测到 Deprecated_Function_Use > 0，则标记为 Warning 但不阻断，仅当 Critical_Syntax_Error > 0 时触发终止。

## Corrected Claim

静态语法检查的量化通过标准：使用 AST (Abstract Syntax Tree) 解析器，要求 Parse_Error_Count = 0 且 Undefined_Name_Count = 0；若检测到 Deprecated_Function_Use > 0，则标记为 Warning 但不阻断，仅当 Critical_Syntax_Error > 0 时触发终止。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

AST parser syntax check criteria undefined dependencies count
