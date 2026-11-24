# N644: 大文件（>100MB）下载应使用 Multipart Download 或 Range Get 并行获取，单线程下载会因TCP窗口限制和HTTP头部开销导致带宽

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N223

## Claim

大文件（>100MB）下载应使用 Multipart Download 或 Range Get 并行获取，单线程下载会因TCP窗口限制和HTTP头部开销导致带宽利用率低于50%；需计算达到 90% 带宽利用率所需的最小并发流数 N_streams ≈ Bandwidth / (Single_Stream_Max_Throughput)。

## Corrected Claim

大文件（>100MB）下载应使用 Multipart Download 或 Range Get 并行获取，单线程下载会因TCP窗口限制和HTTP头部开销导致带宽利用率低于50%；需计算达到 90% 带宽利用率所需的最小并发流数 N_streams ≈ Bandwidth / (Single_Stream_Max_Throughput)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

S3 multipart download optimal concurrency bandwidth utilization
