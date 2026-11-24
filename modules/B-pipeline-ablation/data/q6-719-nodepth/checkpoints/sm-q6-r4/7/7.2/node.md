# N176: 短视频对象平均大小 s_video (MB) 的典型估算值为 5-15 MB，基于 15-60 秒时长、1080p 分辨率及 H.265/AV1 编码比特率（2

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

短视频对象平均大小 s_video (MB) 的典型估算值为 5-15 MB，基于 15-60 秒时长、1080p 分辨率及 H.265/AV1 编码比特率（2-5 Mbps）的计算：s_video = bit_rate * duration。

## Corrected Claim

短视频对象平均大小 s_video (MB) 的典型估算值为 5-15 MB，基于 15-60 秒时长、1080p 分辨率及 H.265/AV1 编码比特率（2-5 Mbps）的计算：s_video = bit_rate * duration。

## Evidence

父节点级核验未通过：有冗余（子节点代表了同一物理量 s_video 在不同参数配置（分辨率、时长、编码）下的具体实例，而非该变量定义的独立正交维度。它们本质上是同一公式 s_video = bitrate * duration 的不同取值，属于参数化变体而非结构性分解，因此存在概念上的冗余。）

## Search Query

average short video file size 1080p H.265 MB
