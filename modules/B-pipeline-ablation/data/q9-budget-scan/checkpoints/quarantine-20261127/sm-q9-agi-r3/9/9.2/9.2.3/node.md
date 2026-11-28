# N287: 报错解析与反馈构建时间 T_feedback = T_parse + T_context_build，其中 T_parse (正则/AST 解析 traceba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

报错解析与反馈构建时间 T_feedback = T_parse + T_context_build，其中 T_parse (正则/AST 解析 traceback) < 0.05s，T_context_build (将错误信息格式化并注入 prompt 的 token 计数) < 0.02s，合计 T_feedback < 0.1s，可忽略不计；但若错误信息超过 2000 tokens 需截断，截断逻辑耗时增加 0.01s。

## Corrected Claim

报错解析与反馈构建时间 T_feedback = T_parse + T_context_build，其中 T_parse (正则/AST 解析 traceback) < 0.05s，T_context_build (将错误信息格式化并注入 prompt 的 token 计数) < 0.02s，合计 T_feedback < 0.1s，可忽略不计；但若错误信息超过 2000 tokens 需截断，截断逻辑耗时增加 0.01s。

## Evidence

先验知识/题面给定，逻辑校验通过
