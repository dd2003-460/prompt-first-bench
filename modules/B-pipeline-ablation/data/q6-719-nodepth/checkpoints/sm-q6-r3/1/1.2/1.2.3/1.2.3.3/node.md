# N161: 地理分布对跳数的影响：用户地理分布越分散，平均跳数 Hops_avg 越高。对于 500 万 DAU 的平台，若 80% 用户集中在 5 个核心区域（自建 PO

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

地理分布对跳数的影响：用户地理分布越分散，平均跳数 Hops_avg 越高。对于 500 万 DAU 的平台，若 80% 用户集中在 5 个核心区域（自建 POP 覆盖），20% 分散在长尾区域，则 Hops_avg = 0.8 × 2 + 0.2 × 4 = 2.4 跳。

## Corrected Claim

地理分布对跳数的影响：用户地理分布越分散，平均跳数 Hops_avg 越高。对于 500 万 DAU 的平台，若 80% 用户集中在 5 个核心区域（自建 POP 覆盖），20% 分散在长尾区域，则 Hops_avg = 0.8 × 2 + 0.2 × 4 = 2.4 跳。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算正确（0.8*2 + 0.2*4 = 2.4），且符合网络拓扑中地理分散度与跳数正相关的基本直觉。

## Search Query

user geographic distribution impact on network hop count CDN
