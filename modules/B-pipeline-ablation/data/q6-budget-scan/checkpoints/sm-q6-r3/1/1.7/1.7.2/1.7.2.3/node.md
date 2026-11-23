# N228: 源站P99排队延迟 T_origin_queue_P99：源站连接池或线程池的等待时间，在高并发回源时可能显著增加，典型值为0-50ms，需基于回源率R_ori

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

源站P99排队延迟 T_origin_queue_P99：源站连接池或线程池的等待时间，在高并发回源时可能显著增加，典型值为0-50ms，需基于回源率R_origin估算

## Corrected Claim

源站P99排队延迟 T_origin_queue_P99：源站连接池或线程池的等待时间，在高并发回源时可能显著增加，典型值为0-50ms，需基于回源率R_origin估算

## Evidence

先验知识/题面给定，逻辑校验通过
