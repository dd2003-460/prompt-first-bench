# N322: 短视频对象平均大小s_video的低成本工作点：s_video = 3.75MB，对应720p H.265，码率2Mbps，时长15s，适用于移动网络差/流量敏

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

短视频对象平均大小s_video的低成本工作点：s_video = 3.75MB，对应720p H.265，码率2Mbps，时长15s，适用于移动网络差/流量敏感用户，带宽成本最低，但画质在低端设备上可能有明显压缩伪影。

## Corrected Claim

短视频对象平均大小s_video的低成本工作点：s_video = 3.75MB，对应720p H.265，码率2Mbps，时长15s，适用于移动网络差/流量敏感用户，带宽成本最低，但画质在低端设备上可能有明显压缩伪影。

## Evidence

先验知识/题面给定，逻辑校验通过：3.75MB ≈ 30Mbit，15s时长对应2Mbps码率，符合720p H.265在移动网络下的典型低成本工作点参数。

## Search Query

short video 720p h265 2mbps 15s size 3.75mb
