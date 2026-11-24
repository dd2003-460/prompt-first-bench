# N166: T_processing_origin（源站处理时间）包括对象存储读取、元数据查询及签名验证，典型值 5-50ms；对于对象存储（如 S3/OSS），读取延迟通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

T_processing_origin（源站处理时间）包括对象存储读取、元数据查询及签名验证，典型值 5-50ms；对于对象存储（如 S3/OSS），读取延迟通常由 IOPS 决定，假设源站具备 10k IOPS，单请求处理时间约为 1/10000s = 0.1ms，但包含网络栈开销后通常为 5-10ms

## Corrected Claim

T_processing_origin（源站处理时间）包括对象存储读取、元数据查询及签名验证，典型值 5-50ms；对于对象存储（如 S3/OSS），读取延迟通常由 IOPS 决定，假设源站具备 10k IOPS，单请求处理时间约为 1/10000s = 0.1ms，但包含网络栈开销后通常为 5-10ms

## Evidence

先验知识/题面给定，逻辑校验通过
