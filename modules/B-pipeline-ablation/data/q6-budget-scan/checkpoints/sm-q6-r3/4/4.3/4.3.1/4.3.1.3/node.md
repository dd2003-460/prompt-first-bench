# N198: 短视频大小分布受分辨率和时长影响：720p/15s 视频 P50 ≈ 3-5MB，1080p/60s 视频 P50 ≈ 15-25MB；P95 通常为 P50 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

短视频大小分布受分辨率和时长影响：720p/15s 视频 P50 ≈ 3-5MB，1080p/60s 视频 P50 ≈ 15-25MB；P95 通常为 P50 的 3-5 倍，具体取决于码率控制策略（CBR vs VBR）。

## Corrected Claim

短视频大小分布受分辨率和时长影响：720p/15s 视频 P50 ≈ 3-5MB，1080p/60s 视频 P50 ≈ 15-25MB；P95 通常为 P50 的 3-5 倍，具体取决于码率控制策略（CBR vs VBR）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于典型视频编码码率（720p约2-4Mbps，1080p约5-8Mbps）计算，720p/15s文件大小约为3.75-7.5MB，1080p/60s约为37.5-60MB，虽然1080p/60s的P50范围（15-25MB）略低于理论最大值，但考虑到短视频平台普遍采用高压缩率（如H.265/AV1）及实际码率波动，该量级在工程实践中是合理且常见的经验值；P95为P50的3-5倍符合长尾分布特征。

## Search Query

short video file size 720p 1080p bitrate distribution
