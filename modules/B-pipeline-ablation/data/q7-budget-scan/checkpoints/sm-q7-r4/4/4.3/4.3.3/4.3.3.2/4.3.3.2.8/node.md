# N739: 云对象存储API速率限制对恢复带宽的影响：AWS S3 GetObject请求默认限制为3500 req/s（标准存储）或更低（GLACIER）。若对象平均大小

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256, N257, N258

## Claim

云对象存储API速率限制对恢复带宽的影响：AWS S3 GetObject请求默认限制为3500 req/s（标准存储）或更低（GLACIER）。若对象平均大小为1MB，3500 req/s * 1MB = 3.5GB/s，远高于1Gbps带宽，故API限制非瓶颈。但若对象极小（如1KB），3500 req/s * 1KB = 3.5MB/s，则API限制成为瓶颈，导致带宽利用率极低。需根据平均对象大小判断瓶颈在带宽还是API限流。

## Corrected Claim

云对象存储API速率限制对恢复带宽的影响：AWS S3 GetObject请求默认限制为3500 req/s（标准存储）或更低（GLACIER）。若对象平均大小为1MB，3500 req/s * 1MB = 3.5GB/s，远高于1Gbps带宽，故API限制非瓶颈。但若对象极小（如1KB），3500 req/s * 1KB = 3.5MB/s，则API限制成为瓶颈，导致带宽利用率极低。需根据平均对象大小判断瓶颈在带宽还是API限流。

## Evidence

先验知识/题面给定，逻辑校验通过：AWS S3 标准存储默认 QPS 限制确为 3500 req/s，单位换算（3500*1MB=3.5GB/s > 1Gbps≈0.125GB/s）及瓶颈分析逻辑自洽。

## Search Query

AWS S3 GetObject request rate limit small object size bandwidth bottleneck
