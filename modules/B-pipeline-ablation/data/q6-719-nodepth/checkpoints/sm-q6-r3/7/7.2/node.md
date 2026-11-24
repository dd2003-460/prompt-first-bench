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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式 s_video = bitrate * duration / 8 在不同参数（分辨率、编码、时长）下的具体实例，存在高度冗余。虽然它们在数值上覆盖了低、中、高范围，但父节点的核心是估算逻辑和典型范围，子节点未覆盖非典型场景（如超短视频或特殊编码），且将单一参数化过程拆解为三个独立节点不符合学术分解的原子性原则，建议合并或重构为参数化定义。）

## Search Query

average short video file size 1080p H.265 MB
