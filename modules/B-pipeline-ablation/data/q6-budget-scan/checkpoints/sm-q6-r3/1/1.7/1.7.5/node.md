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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点中提到的三个主要组成部分（对象存储IO/基准、动态签名验证、元数据检索），彼此独立且无重叠；覆盖了父节点提及的所有关键延迟来源；虽然涉及具体技术栈（如S3、Redis等），但这些是父节点中'对象存储'、'数据库查询'的具体实现案例，属于合理的细化而非冗余参数，因为不同后端对延迟影响显著，需作为独立变量考量。）

## Search Query

origin server processing time static file retrieval
