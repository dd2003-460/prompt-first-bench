# N242: Tree-sitter AST 解析 + 符号表构建的预处理耗时 T_pre = 1.5s + 0.05s * n_files，其中 n_files 为参与重构

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

Tree-sitter AST 解析 + 符号表构建的预处理耗时 T_pre = 1.5s + 0.05s * n_files，其中 n_files 为参与重构的文件数量

## Corrected Claim

Tree-sitter AST 解析 + 符号表构建的预处理耗时 T_pre = 1.5s + 0.05s * n_files，其中 n_files 为参与重构的文件数量

## Evidence

先验知识/题面给定，逻辑校验通过
