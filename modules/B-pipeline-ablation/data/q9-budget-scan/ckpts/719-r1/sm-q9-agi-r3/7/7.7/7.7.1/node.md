# N289: AST解析错误定位模块需提取报错行的行号(line_no)和列号(col_no)，并通过正则匹配或tree-sitter API将错误位置映射到对应的AST节点

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92, N93, N94

## Claim

AST解析错误定位模块需提取报错行的行号(line_no)和列号(col_no)，并通过正则匹配或tree-sitter API将错误位置映射到对应的AST节点ID，该映射过程在10k行代码文件上的平均耗时需<50ms，以确保不显著增加单次反馈延迟

## Corrected Claim

AST解析错误定位模块需提取报错行的行号(line_no)和列号(col_no)，并通过正则匹配或tree-sitter API将错误位置映射到对应的AST节点ID，该映射过程在10k行代码文件上的平均耗时需<50ms，以确保不显著增加单次反馈延迟

## Evidence

先验知识/题面给定，逻辑校验通过
