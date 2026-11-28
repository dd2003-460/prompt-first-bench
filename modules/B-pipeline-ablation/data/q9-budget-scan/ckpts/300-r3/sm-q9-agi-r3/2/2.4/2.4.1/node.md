# N63: code_executor 沙箱的安全隔离开销：基于 Docker/gVisor 容器化启动延迟为 200ms/次，内存隔离开销为 50MB/实例，CPU 限制

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

code_executor 沙箱的安全隔离开销：基于 Docker/gVisor 容器化启动延迟为 200ms/次，内存隔离开销为 50MB/实例，CPU 限制为 2 cores/500MHz，总安全开销占总执行时间比例 < 5%

## Corrected Claim

code_executor 沙箱的安全隔离开销：基于 Docker/gVisor 容器化启动延迟为 200ms/次，内存隔离开销为 50MB/实例，CPU 限制为 2 cores/500MHz，总安全开销占总执行时间比例 < 5%

## Evidence

先验知识/题面给定，逻辑校验通过
