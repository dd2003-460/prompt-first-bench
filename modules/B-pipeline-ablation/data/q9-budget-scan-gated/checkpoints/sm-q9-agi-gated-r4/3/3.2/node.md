# N15: 代码执行沙箱的资源隔离开销：Docker 容器启动延迟约 200-500ms，CPU 绑定后单核利用率可达 95%；对于轻量级数据处理任务（<10MB 数据），

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

代码执行沙箱的资源隔离开销：Docker 容器启动延迟约 200-500ms，CPU 绑定后单核利用率可达 95%；对于轻量级数据处理任务（<10MB 数据），沙箱开销占总执行时间的 <5%

## Corrected Claim

代码执行沙箱的资源隔离开销：Docker 容器启动延迟约 200-500ms，CPU 绑定后单核利用率可达 95%；对于轻量级数据处理任务（<10MB 数据），沙箱开销占总执行时间的 <5%

## Evidence

先验知识/题面给定，逻辑校验通过
