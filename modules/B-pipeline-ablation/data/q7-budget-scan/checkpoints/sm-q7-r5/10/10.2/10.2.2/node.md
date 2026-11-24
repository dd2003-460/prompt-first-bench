# N287: 自建数据中心若要匹配云 99.99% 可用性，需部署双活集群，其电力冗余系数 k_self = 2.0（主备同时在线）+ 10%（N+1 电源/UPS 冗余）=

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134

## Claim

自建数据中心若要匹配云 99.99% 可用性，需部署双活集群，其电力冗余系数 k_self = 2.0（主备同时在线）+ 10%（N+1 电源/UPS 冗余）= 2.2 倍；若采用三副本跨机柜，k_self ≈ 3.3 倍。该系数用于修正自建方案在 TCO 中的电力项：P_actual = P_base * k_self。

## Corrected Claim

自建数据中心若要匹配云 99.99% 可用性，需部署双活集群，其电力冗余系数 k_self = 2.0（主备同时在线）+ 10%（N+1 电源/UPS 冗余）= 2.2 倍；若采用三副本跨机柜，k_self ≈ 3.3 倍。该系数用于修正自建方案在 TCO 中的电力项：P_actual = P_base * k_self。

## Evidence

先验知识/题面给定，逻辑校验通过：双活架构通常涉及两套完整系统运行，基础功耗约为单套的2倍，加上N+1冗余带来的约10%额外开销，系数2.2符合工程估算逻辑；三副本跨机柜意味着数据存三份，若每份对应独立计算/存储单元，系数3.3亦在合理量级范围内。

## Search Query

self-hosted data center dual-active redundancy power factor 99.99% availability
