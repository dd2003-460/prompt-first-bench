# N42: 全局最大对象大小 $s_{max}$ 定义为所有请求中对象大小的 99.9% 分位数，估算值为 50 MB（短视频长尾端），用于计算最坏情况下的单流传输时间下限

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

全局最大对象大小 $s_{max}$ 定义为所有请求中对象大小的 99.9% 分位数，估算值为 50 MB（短视频长尾端），用于计算最坏情况下的单流传输时间下限 $T_{transfer} = s_{max} / B_{link}$。

## Corrected Claim

全局最大对象大小 $s_{max}$ 定义为所有请求中对象大小的 99.9% 分位数，估算值为 50 MB（短视频长尾端），用于计算最坏情况下的单流传输时间下限 $T_{transfer} = s_{max} / B_{link}$。

## Evidence

先验知识/题面给定，逻辑校验通过：99.9%分位数作为长尾上限估算值50MB在短视频场景下量级合理，传输时间公式量纲正确。

## Search Query

maximum object size media platform 99.9th percentile
