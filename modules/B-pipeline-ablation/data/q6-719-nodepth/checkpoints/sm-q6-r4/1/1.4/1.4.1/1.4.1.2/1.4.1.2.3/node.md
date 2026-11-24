# N526: 视频转码倍数（Transcode Multiplier）：每个原始视频通常生成3-5个分辨率版本（360p/480p/720p/1080p），因此实际存储对象数

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N176

## Claim

视频转码倍数（Transcode Multiplier）：每个原始视频通常生成3-5个分辨率版本（360p/480p/720p/1080p），因此实际存储对象数 N_vid_stored = N_vid_raw × Transcode_Multiplier (3-5)，但唯一内容标识（Content ID）仍为1，影响缓存命中率计算

## Corrected Claim

视频转码倍数（Transcode Multiplier）：每个原始视频通常生成3-5个分辨率版本（360p/480p/720p/1080p），因此实际存储对象数 N_vid_stored = N_vid_raw × Transcode_Multiplier (3-5)，但唯一内容标识（Content ID）仍为1，影响缓存命中率计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

video transcoding resolution versions storage multiplier CDN cache
