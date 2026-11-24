# N525: 自建部分带宽成本 C_bw_self = (Q_day * P_core * s * H_miss_self) * P_bw_self / 1000，其中H_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

自建部分带宽成本 C_bw_self = (Q_day * P_core * s * H_miss_self) * P_bw_self / 1000，其中H_miss_self为自建缓存未命中率，P_bw_self为自建带宽单价¥/GB，需代入具体数值计算。

## Corrected Claim

自建部分带宽成本 C_bw_self = (Q_day * P_core * s * H_miss_self) * P_bw_self / 1000，其中H_miss_self为自建缓存未命中率，P_bw_self为自建带宽单价¥/GB，需代入具体数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
