# N10: 时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典型 $K_{peak}$ 在 1.5 到 2.5 之间，需据此计算峰值带宽需求 $B_{peak} = (2 \text{ TB} / 86400 \text{ s}) \times K_{peak}$。

## Corrected Claim

时间峰值系数 $K_{peak}$ 定义为日峰值带宽与日均带宽之比，即 $K_{peak} = B_{peak} / B_{avg}$；对于 C 端媒体平台，典型 $K_{peak}$ 在 1.5 到 2.5 之间，需据此计算峰值带宽需求 $B_{peak} = (2 \text{ TB} / 86400 \text{ s}) \times K_{peak}$。

## Evidence

先验知识/题面给定，逻辑校验通过：定义符合带宽工程常识，C端媒体平台峰值系数1.5-2.5属于典型经验范围，量纲与计算逻辑自洽。

## Search Query

web traffic peak to average ratio media streaming
