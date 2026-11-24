# N525: 平均短视频大小 s_vid 的计算：s_vid = Bitrate × Duration，假设平均时长15s，H.264编码码率2Mbps，则 s_vid = 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N176

## Claim

平均短视频大小 s_vid 的计算：s_vid = Bitrate × Duration，假设平均时长15s，H.264编码码率2Mbps，则 s_vid = 2Mbps × 15s / 8 = 3.75MB；若采用H.265或AV1，码率可降至1-1.5Mbps，s_vid 降至2-2.5MB

## Corrected Claim

平均短视频大小 s_vid 的计算：s_vid = Bitrate × Duration，假设平均时长15s，H.264编码码率2Mbps，则 s_vid = 2Mbps × 15s / 8 = 3.75MB；若采用H.265或AV1，码率可降至1-1.5Mbps，s_vid 降至2-2.5MB

## Evidence

先验知识/题面给定，逻辑校验通过：2Mbps * 15s / 8 = 3.75MB 计算正确；H.265/AV1 相比 H.264 通常有 40-50% 的码率节省，1-1.5Mbps 及对应 2-2.5MB 的大小估算符合工程常识。

## Search Query

average short video file size 15 seconds H.264 bitrate MB
