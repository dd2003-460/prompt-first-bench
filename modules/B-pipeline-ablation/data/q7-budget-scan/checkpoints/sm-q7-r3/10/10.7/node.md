# N301: 500TB数据上行至阿里云OSS的并行上传时间计算：单线程10Gbps带宽下耗时 = 500TB / (10Gbps/8) = 500×1024GB / 1.2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N99, N100

## Claim

500TB数据上行至阿里云OSS的并行上传时间计算：单线程10Gbps带宽下耗时 = 500TB / (10Gbps/8) = 500×1024GB / 1.25GB/s ≈ 409,600s ≈ 114小时；若使用10个并行上传节点，总耗时 ≈ 11.4小时，但需考虑OSS API限流（默认10,000 QPS/桶），实际并行度受限于QPS，需分桶上传。

## Corrected Claim

500TB数据上行至阿里云OSS的并行上传时间计算：单线程10Gbps带宽下耗时 = 500TB / (10Gbps/8) = 500×1024GB / 1.25GB/s ≈ 409,600s ≈ 114小时；若使用10个并行上传节点，总耗时 ≈ 11.4小时，但需考虑OSS API限流（默认10,000 QPS/桶），实际并行度受限于QPS，需分桶上传。

## Evidence

先验知识/题面给定，逻辑校验通过：500TB=512000GB，10Gbps=1.25GB/s，512000/1.25=409600s≈113.8h，10并行≈11.4h，计算无误；OSS QPS限制为已知工程约束，逻辑自洽。

## Search Query

Aliyun OSS upload speed limit parallel QPS bucket
