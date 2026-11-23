# N182: 源站数据库查询延迟 P99 的分解：T_db_p99 = T_index_scan + T_join + T_network_db，其中 T_index_sca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

源站数据库查询延迟 P99 的分解：T_db_p99 = T_index_scan + T_join + T_network_db，其中 T_index_scan ≈ 1-5ms（B+ 树索引查找，取决于数据量与磁盘 IO），T_join ≈ 5-20ms（多表关联，取决于优化器选择与内存缓冲），T_network_db ≈ 1-5ms（源站内部网络 RTT），总 P99 10-50ms（有缓存）或 50-200ms（无缓存全表扫描）。

## Corrected Claim

源站数据库查询延迟 P99 的分解：T_db_p99 = T_index_scan + T_join + T_network_db，其中 T_index_scan ≈ 1-5ms（B+ 树索引查找，取决于数据量与磁盘 IO），T_join ≈ 5-20ms（多表关联，取决于优化器选择与内存缓冲），T_network_db ≈ 1-5ms（源站内部网络 RTT），总 P99 10-50ms（有缓存）或 50-200ms（无缓存全表扫描）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

database query P99 latency breakdown index scan join network milliseconds
