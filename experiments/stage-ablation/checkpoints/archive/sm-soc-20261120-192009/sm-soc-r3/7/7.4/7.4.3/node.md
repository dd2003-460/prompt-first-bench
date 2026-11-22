# N314: 曝光时长分布的非正态性修正：T_exposure 通常服从对数正态分布，Ratio_Exposure 应使用几何均值比而非算术均值比；若算术均值比为 1.8 但

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

曝光时长分布的非正态性修正：T_exposure 通常服从对数正态分布，Ratio_Exposure 应使用几何均值比而非算术均值比；若算术均值比为 1.8 但几何均值比为 1.2，则'1.8 倍'的结论由长尾高曝光商品驱动，非普遍现象，需报告偏度 Skewness > 2 作为警示。

## Corrected Claim

曝光时长分布的非正态性修正：T_exposure 通常服从对数正态分布，Ratio_Exposure 应使用几何均值比而非算术均值比；若算术均值比为 1.8 但几何均值比为 1.2，则'1.8 倍'的结论由长尾高曝光商品驱动，非普遍现象，需报告偏度 Skewness > 2 作为警示。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布下几何均值比更能反映中心趋势，算术均值受长尾影响大，偏度>2作为警示符合统计直觉。
