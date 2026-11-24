# N632: 加权平均对象大小 s_weighted (MB) 的估算：基于图片 (s_img=1MB, 占比 80%) 和短视频 (s_video=10MB, 占比 20%

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N207

## Claim

加权平均对象大小 s_weighted (MB) 的估算：基于图片 (s_img=1MB, 占比 80%) 和短视频 (s_video=10MB, 占比 20%) 的混合负载，s_weighted = 0.8*1 + 0.2*10 = 2.8MB，用于替代单一假设值 2MB 以更准确反映长尾大文件传输耗时。

## Corrected Claim

加权平均对象大小 s_weighted (MB) 的估算：基于图片 (s_img=1MB, 占比 80%) 和短视频 (s_video=10MB, 占比 20%) 的混合负载，s_weighted = 0.8*1 + 0.2*10 = 2.8MB，用于替代单一假设值 2MB 以更准确反映长尾大文件传输耗时。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.8*1 + 0.2*10 = 2.8 正确，量纲一致，符合混合负载估算逻辑。

## Search Query

weighted average object size image video platform bandwidth calculation
