# N156: 视频转码延迟 t_encode 的具体数值取决于分辨率、码率与转码算法，对于 1080p H.264 转码，t_encode ≈ 50-150ms/秒视频；对于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

视频转码延迟 t_encode 的具体数值取决于分辨率、码率与转码算法，对于 1080p H.264 转码，t_encode ≈ 50-150ms/秒视频；对于 720p H.265，t_encode ≈ 30-80ms/秒视频；需根据源站实际转码配置确定。

## Corrected Claim

视频转码延迟 t_encode 的具体数值取决于分辨率、码率与转码算法，对于 1080p H.264 转码，t_encode ≈ 50-150ms/秒视频；对于 720p H.265，t_encode ≈ 30-80ms/秒视频；需根据源站实际转码配置确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

video transcoding latency 1080p H.264
