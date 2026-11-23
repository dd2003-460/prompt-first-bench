# N134: 元数据检索延迟 T_meta 取决于数据库引擎及查询复杂度：Redis内存查询约为 1-3ms，MySQL InnoDB主键查询约为 5-10ms，复杂JOIN

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

元数据检索延迟 T_meta 取决于数据库引擎及查询复杂度：Redis内存查询约为 1-3ms，MySQL InnoDB主键查询约为 5-10ms，复杂JOIN查询约为 20-50ms。

## Corrected Claim

元数据检索延迟 T_meta 取决于数据库引擎及查询复杂度：Redis内存查询约为 1-3ms，MySQL InnoDB主键查询约为 5-10ms，复杂JOIN查询约为 20-50ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Redis vs MySQL query latency ms comparison
