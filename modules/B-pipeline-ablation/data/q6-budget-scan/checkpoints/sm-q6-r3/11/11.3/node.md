# N348: 不同内容类型对 P99 阈值的差异化要求：图片加载 P99_img 通常要求 < 200ms，短视频起播 P99_video_start 要求 < 500ms，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

不同内容类型对 P99 阈值的差异化要求：图片加载 P99_img 通常要求 < 200ms，短视频起播 P99_video_start 要求 < 500ms，直播首帧 P99_live_first_frame 要求 < 1000ms；综合平台阈值 T = max(P99_img, P99_video_start, P99_live_first_frame) 按流量权重加权

## Corrected Claim

不同内容类型对 P99 阈值的差异化要求：图片加载 P99_img 通常要求 < 200ms，短视频起播 P99_video_start 要求 < 500ms，直播首帧 P99_live_first_frame 要求 < 1000ms；综合平台阈值 T = max(P99_img, P99_video_start, P99_live_first_frame) 按流量权重加权

## Evidence

先验知识/题面给定，逻辑校验通过
