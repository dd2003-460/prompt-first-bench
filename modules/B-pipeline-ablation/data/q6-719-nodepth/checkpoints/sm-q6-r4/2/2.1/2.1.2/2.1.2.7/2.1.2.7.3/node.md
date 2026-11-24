# N745: 加权平均对象大小 s_weighted 的精确值：基于 N175 中图片对象平均大小 0.5-1.5MB 和短视频对象平均大小 5-20MB，假设图片:短视频=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N249

## Claim

加权平均对象大小 s_weighted 的精确值：基于 N175 中图片对象平均大小 0.5-1.5MB 和短视频对象平均大小 5-20MB，假设图片:短视频=8:2，则 s_weighted = 0.8*1.0MB + 0.2*10MB = 2.8MB，需根据实际上传分布调整。

## Corrected Claim

加权平均对象大小 s_weighted 的精确值：基于 N175 中图片对象平均大小 0.5-1.5MB 和短视频对象平均大小 5-20MB，假设图片:短视频=8:2，则 s_weighted = 0.8*1.0MB + 0.2*10MB = 2.8MB，需根据实际上传分布调整。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.8*1.0 + 0.2*10 = 2.8 正确，量纲一致，符合加权平均定义。
