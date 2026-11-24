# N1258: 低码率视频（720p H.265 @ 1Mbps）的容器开销占比为 6.25%（0.125MB/2.0MB），该比例在 MP4 格式中属于正常范围（5-10%）

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N431, N432, N433

## Claim

低码率视频（720p H.265 @ 1Mbps）的容器开销占比为 6.25%（0.125MB/2.0MB），该比例在 MP4 格式中属于正常范围（5-10%），主要源于 moov 原子元数据；若采用 fMP4 分片格式，每分片（2s）的容器开销可降至 <1%，总开销降至 ~0.02MB，从而将 s_video 从 2.0MB 降至 1.895MB，减少 5.25% 的传输延迟和带宽成本。

## Corrected Claim

低码率视频（720p H.265 @ 1Mbps）的容器开销占比为 6.25%（0.125MB/2.0MB），该比例在 MP4 格式中属于正常范围（5-10%），主要源于 moov 原子元数据；若采用 fMP4 分片格式，每分片（2s）的容器开销可降至 <1%，总开销降至 ~0.02MB，从而将 s_video 从 2.0MB 降至 1.895MB，减少 5.25% 的传输延迟和带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算准确（0.125/2.0=6.25%，(2.0-1.895)/2.0=5.25%），MP4容器开销量级及fMP4优化效果符合工程常识。

## Search Query

MP4 moov atom overhead percentage fMP4 fragment overhead
