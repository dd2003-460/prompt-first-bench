# N9: 传输延迟T_transmission的带宽瓶颈判定：若s/B_link < RTT_base，则为延迟受限（latency-bound），否则为带宽受限（ban

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

传输延迟T_transmission的带宽瓶颈判定：若s/B_link < RTT_base，则为延迟受限（latency-bound），否则为带宽受限（bandwidth-bound）；短视频平均对象大小s_video ≈ 5-10MB，图片s_img ≈ 0.5-2MB [待核验]

## Corrected Claim

传输延迟T_transmission的带宽瓶颈判定：若s/B_link < RTT_base，则为延迟受限（latency-bound），否则为带宽受限（bandwidth-bound）；短视频平均对象大小s_video ≈ 5-10MB，图片s_img ≈ 0.5-2MB [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：传输延迟判定公式符合网络通信基本原理（带宽瓶颈 vs 延迟瓶颈的临界条件），短视频与图片的典型大小量级符合当前互联网媒体内容的普遍经验值。

## Search Query

average video file size MB CDN delivery 2024
