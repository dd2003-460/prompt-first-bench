# N286: 单台服务器 CPU 算力需求验证：假设单请求 CPU 开销为 0.5ms（Nginx+图片处理），日均 2TB 下载对应约 1000万-2000万请求（假设平均

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

单台服务器 CPU 算力需求验证：假设单请求 CPU 开销为 0.5ms（Nginx+图片处理），日均 2TB 下载对应约 1000万-2000万请求（假设平均对象 1-2MB），峰值 QPS = (1500万/86400)*k_peak(4) ≈ 700 QPS/POP；10台服务器分摊 70 QPS/台，Xeon Gold 6338 (32C) 单核处理能力远高于此，CPU 利用率 <10%，配置冗余主要为了故障隔离而非算力瓶颈

## Corrected Claim

单台服务器 CPU 算力需求验证：假设单请求 CPU 开销为 0.5ms（Nginx+图片处理），日均 2TB 下载对应约 1000万-2000万请求（假设平均对象 1-2MB），峰值 QPS = (1500万/86400)*k_peak(4) ≈ 700 QPS/POP；10台服务器分摊 70 QPS/台，Xeon Gold 6338 (32C) 单核处理能力远高于此，CPU 利用率 <10%，配置冗余主要为了故障隔离而非算力瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：日均2TB/1.5MB≈1333万请求，峰值QPS≈700，10台分摊70QPS/台，Xeon Gold 6338单核处理能力远超此负载，CPU利用率<10%结论合理

## Search Query

Nginx CPU usage per request static file serving benchmark
