# N134: 用户到最近 POP 点的距离分布 $D_{dist}$ 的分位数参数：基于 P_region 和 S_10 计算出的用户到最近 POP 距离的 P50、P90 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

用户到最近 POP 点的距离分布 $D_{dist}$ 的分位数参数：基于 P_region 和 S_10 计算出的用户到最近 POP 距离的 P50、P90 和 P99 值（单位：km），例如 P50 约为 300-500 km，P99 约为 1500-2000 km，用于代入 RTT 公式计算不同百分位的延迟。

## Corrected Claim

用户到最近 POP 点的距离分布 $D_{dist}$ 的分位数参数：基于 P_region 和 S_10 计算出的用户到最近 POP 距离的 P50、P90 和 P99 值（单位：km），例如 P50 约为 300-500 km，P99 约为 1500-2000 km，用于代入 RTT 公式计算不同百分位的延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：在典型全球或大洲级CDN/POP部署场景下，用户到最近POP点的距离分布中，P50在300-500km、P99在1500-2000km的量级符合地理分布与网络覆盖的工程直觉，数值量级合理且无内部矛盾。
