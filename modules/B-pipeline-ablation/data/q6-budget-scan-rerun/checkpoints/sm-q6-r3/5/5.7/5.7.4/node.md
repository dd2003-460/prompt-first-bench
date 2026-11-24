# N119: POP分布对带宽成本的边际效应：增加第N个POP的边际带宽成本 = 新增POP覆盖区域的流量增量 × 带宽单价 - 原POP回源带宽节省量，当POP覆盖区域用户

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

POP分布对带宽成本的边际效应：增加第N个POP的边际带宽成本 = 新增POP覆盖区域的流量增量 × 带宽单价 - 原POP回源带宽节省量，当POP覆盖区域用户密度低于阈值 $\rho_{threshold}$ 时，边际成本 > 边际收益，最优POP数由边际成本=边际收益决定

## Corrected Claim

POP分布对带宽成本的边际效应：增加第N个POP的边际带宽成本 = 新增POP覆盖区域的流量增量 × 带宽单价 - 原POP回源带宽节省量，当POP覆盖区域用户密度低于阈值 $\rho_{threshold}$ 时，边际成本 > 边际收益，最优POP数由边际成本=边际收益决定

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述基于微观经济学中边际成本与边际收益相等的优化原则，公式结构（新增成本-节省成本=净边际成本）符合CDN网络规划的基本经济逻辑，量纲与因果关系自洽。
