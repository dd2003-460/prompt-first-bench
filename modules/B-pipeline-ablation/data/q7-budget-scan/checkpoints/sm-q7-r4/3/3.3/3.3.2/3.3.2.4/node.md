# N216: 分层架构的元数据管理开销 C_meta_ops：每日扫描100TB温数据需更新访问日志，假设每1GB数据产生1KB日志，日增日志量=100GB，年增36.5TB

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

分层架构的元数据管理开销 C_meta_ops：每日扫描100TB温数据需更新访问日志，假设每1GB数据产生1KB日志，日增日志量=100GB，年增36.5TB；存储及索引这些元数据的额外HDD/SSD成本及查询延迟影响需量化

## Corrected Claim

分层架构的元数据管理开销 C_meta_ops：每日扫描100TB温数据需更新访问日志，假设每1GB数据产生1KB日志，日增日志量=100GB，年增36.5TB；存储及索引这些元数据的额外HDD/SSD成本及查询延迟影响需量化

## Evidence

父节点级核验未通过：不完备（子节点在计算上存在严重逻辑错误和内部矛盾，导致结果不可信；且父节点明确要求的'查询延迟影响'未在子节点中体现，覆盖不全。）

## Search Query

data lake metadata logging overhead cost estimation
