# N343: S3 GET请求的HTTP头部与协议开销占比：单个GET请求的固定开销约为1KB（HTTP头+ACK），相对于128MB对象，带宽效率 η_protocol =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

S3 GET请求的HTTP头部与协议开销占比：单个GET请求的固定开销约为1KB（HTTP头+ACK），相对于128MB对象，带宽效率 η_protocol = 128MB / (128MB + 1KB) ≈ 99.99%；但在小文件场景（如1MB）下，η_protocol = 1MB / (1MB + 1KB) ≈ 99.9%，需评估是否需启用S3 Transfer Acceleration以减少RTT损耗。

## Corrected Claim

S3 GET请求的HTTP头部与协议开销占比：单个GET请求的固定开销约为1KB（HTTP头+ACK），相对于128MB对象，带宽效率 η_protocol = 128MB / (128MB + 1KB) ≈ 99.99%；但在小文件场景（如1MB）下，η_protocol = 1MB / (1MB + 1KB) ≈ 99.9%，需评估是否需启用S3 Transfer Acceleration以减少RTT损耗。

## Evidence

先验知识/题面给定，逻辑校验通过
