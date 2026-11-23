# N8: 对象大小分布 $P(s)$ 呈双峰或长尾分布，图片类对象大小集中在 0.5MB-2MB，短视频类集中在 5MB-20MB；需定义加权平均大小 $s_{avg} 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

对象大小分布 $P(s)$ 呈双峰或长尾分布，图片类对象大小集中在 0.5MB-2MB，短视频类集中在 5MB-20MB；需定义加权平均大小 $s_{avg} = \sum p_i s_i$ 用于带宽换算，以及最大对象大小 $s_{max}$ 用于计算单流传输时间下限。

## Corrected Claim

对象大小分布 $P(s)$ 呈双峰或长尾分布，图片类对象大小集中在 0.5MB-2MB，短视频类集中在 5MB-20MB；需定义加权平均大小 $s_{avg} = \sum p_i s_i$ 用于带宽换算，以及最大对象大小 $s_{max}$ 用于计算单流传输时间下限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

media platform file size distribution image video statistics
