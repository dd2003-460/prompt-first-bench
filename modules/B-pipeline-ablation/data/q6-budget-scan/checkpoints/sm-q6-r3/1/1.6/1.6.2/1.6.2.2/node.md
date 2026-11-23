# N217: 公有云源站处理延迟T_origin_processing_P99的后端瓶颈分解：T_origin = T_db_query + T_app_logic + T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

公有云源站处理延迟T_origin_processing_P99的后端瓶颈分解：T_origin = T_db_query + T_app_logic + T_response_serialization，其中T_db_query取决于数据库索引效率（通常5-50ms），T_app_logic为业务逻辑计算（通常1-10ms），T_response_serialization为JSON/XML序列化（通常<1ms）；P99值需考虑数据库连接池耗尽导致的排队时间，通常比P50高2-5倍

## Corrected Claim

公有云源站处理延迟T_origin_processing_P99的后端瓶颈分解：T_origin = T_db_query + T_app_logic + T_response_serialization，其中T_db_query取决于数据库索引效率（通常5-50ms），T_app_logic为业务逻辑计算（通常1-10ms），T_response_serialization为JSON/XML序列化（通常<1ms）；P99值需考虑数据库连接池耗尽导致的排队时间，通常比P50高2-5倍

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

origin server processing latency breakdown database query application logic serialization P99
