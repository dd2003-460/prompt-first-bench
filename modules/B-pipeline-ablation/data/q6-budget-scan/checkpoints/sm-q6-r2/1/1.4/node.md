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

父节点级核验通过：正交+完备+无冗余（子节点分别针对图片、视频两个具体案例进行了验证，并给出了通用的临界值公式与计算，三者逻辑互补且不重叠。图片与视频属于不同参数取值下的独立案例，临界值节点提供了通用判定边界，共同完整覆盖了父节点关于‘带宽瓶颈判定’的定义、应用及边界条件。）

## Search Query

average video file size MB CDN delivery 2024
