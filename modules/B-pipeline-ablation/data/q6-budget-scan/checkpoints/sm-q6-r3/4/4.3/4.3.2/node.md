# N64: 热点对象数 N_unique_hot 的估算：N_unique_hot = (2TB / s_avg) * H_factor，其中 s_avg 为平均对象大小（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

热点对象数 N_unique_hot 的估算：N_unique_hot = (2TB / s_avg) * H_factor，其中 s_avg 为平均对象大小（加权平均图片与视频），H_factor 为热点集中因子（通常 0.1-0.3，取决于内容分发集中度）

## Corrected Claim

热点对象数 N_unique_hot 的估算：N_unique_hot = (2TB / s_avg) * H_factor，其中 s_avg 为平均对象大小（加权平均图片与视频），H_factor 为热点集中因子（通常 0.1-0.3，取决于内容分发集中度）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cache hit rate hot object count estimation web content
