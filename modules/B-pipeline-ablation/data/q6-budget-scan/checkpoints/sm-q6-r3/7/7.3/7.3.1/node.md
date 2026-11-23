# N335: 95th百分位带宽$B_{95}$的计算公式为：$B_{95} = \text{Percentile}(B_{5min}, 95)$，其中$B_{5min}$为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125

## Claim

95th百分位带宽$B_{95}$的计算公式为：$B_{95} = \text{Percentile}(B_{5min}, 95)$，其中$B_{5min}$为月内所有5分钟采样点的带宽值集合，单位Gbps。

## Corrected Claim

95th百分位带宽$B_{95}$的计算公式为：$B_{95} = \text{Percentile}(B_{5min}, 95)$，其中$B_{5min}$为月内所有5分钟采样点的带宽值集合，单位Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过
