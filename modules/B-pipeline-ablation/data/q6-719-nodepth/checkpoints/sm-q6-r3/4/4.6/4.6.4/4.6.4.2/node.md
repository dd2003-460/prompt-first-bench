# N391: L2 缓存未命中率 Miss_rate_L2 与 L1 未命中流量的关系：Miss_rate_L2 作用于 L1 未命中的流量部分，即 Origin_Traff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

L2 缓存未命中率 Miss_rate_L2 与 L1 未命中流量的关系：Miss_rate_L2 作用于 L1 未命中的流量部分，即 Origin_Traffic = Q_day * (1 - Hit_rate_L1) * (1 - Hit_rate_L2)。由于 L2 容量大且聚合了多 L1 请求，其 Hit_rate_L2 通常高达 95-99%，导致最终回源率极低。

## Corrected Claim

L2 缓存未命中率 Miss_rate_L2 与 L1 未命中流量的关系：Miss_rate_L2 作用于 L1 未命中的流量部分，即 Origin_Traffic = Q_day * (1 - Hit_rate_L1) * (1 - Hit_rate_L2)。由于 L2 容量大且聚合了多 L1 请求，其 Hit_rate_L2 通常高达 95-99%，导致最终回源率极低。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合缓存层级原理，L2高命中率（95-99%）符合工程常识

## Search Query

CDN L2 cache hit rate origin traffic reduction ratio
