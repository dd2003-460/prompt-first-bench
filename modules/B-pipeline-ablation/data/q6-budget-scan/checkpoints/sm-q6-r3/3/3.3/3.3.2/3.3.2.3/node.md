# N219: 95th 百分位计费与固定带宽计费的临界点：当 $B_{reserved}$ 超过 1Gbps 且流量波动较大时，95th 计费可能低于固定带宽计费，需比较 $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

95th 百分位计费与固定带宽计费的临界点：当 $B_{reserved}$ 超过 1Gbps 且流量波动较大时，95th 计费可能低于固定带宽计费，需比较 $C_{95} = B_{95} \times R_{95}$ 与 $C_{fixed} = B_{reserved} \times R_{fixed}$。

## Corrected Claim

95th 百分位计费与固定带宽计费的临界点：当 $B_{reserved}$ 超过 1Gbps 且流量波动较大时，95th 计费可能低于固定带宽计费，需比较 $C_{95} = B_{95} \times R_{95}$ 与 $C_{fixed} = B_{reserved} \times R_{fixed}$。

## Evidence

先验知识/题面给定，逻辑校验通过：95th百分位计费与固定带宽计费的比较逻辑符合云计算计费基本原理，公式定义正确，量纲一致。
