# N40: 源站处理时间 T_origin 包含数据库查询、对象存储IO及元数据检索，对于静态文件通常为 5-20ms；若涉及动态签名URL验证，需增加 2-5ms 的CP

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

源站处理时间 T_origin 包含数据库查询、对象存储IO及元数据检索，对于静态文件通常为 5-20ms；若涉及动态签名URL验证，需增加 2-5ms 的CPU处理时间。

## Corrected Claim

源站处理时间 T_origin 包含数据库查询、对象存储IO及元数据检索，对于静态文件通常为 5-20ms；若涉及动态签名URL验证，需增加 2-5ms 的CPU处理时间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

origin server processing time static file retrieval
