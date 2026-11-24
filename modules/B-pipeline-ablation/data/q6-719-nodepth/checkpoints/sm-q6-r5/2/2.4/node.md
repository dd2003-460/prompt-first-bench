# N14: 网络跳数延迟 L_hops = Hops * 5ms，其中 Hops 为用户到边缘节点的平均跳数（2-4 跳），公有云 CDN 通常 3 跳，自建节点 2-3 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

网络跳数延迟 L_hops = Hops * 5ms，其中 Hops 为用户到边缘节点的平均跳数（2-4 跳），公有云 CDN 通常 3 跳，自建节点 2-3 跳，影响 P99 尾部延迟。

## Corrected Claim

网络跳数延迟 L_hops = Hops * 5ms，其中 Hops 为用户到边缘节点的平均跳数（2-4 跳），公有云 CDN 通常 3 跳，自建节点 2-3 跳，影响 P99 尾部延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：5ms/跳符合典型RTT量级，2-4跳范围符合网络拓扑常识，公式线性关系逻辑自洽。
