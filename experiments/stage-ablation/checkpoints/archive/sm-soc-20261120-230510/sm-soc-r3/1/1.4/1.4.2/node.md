# N42: 筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数，N_search_total 为搜索该商品的总人数；S 与 P_ask 在区间内呈单调递增关系。

## Corrected Claim

筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数，N_search_total 为搜索该商品的总人数；S 与 P_ask 在区间内呈单调递增关系。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了随机源定义（微观机制）、期望值性质（宏观趋势/单调性验证）和方差计算（统计波动），三者逻辑层次清晰且无重叠。虽然子节点2中关于'当 P_ask 接近 V 时 S 趋近于 0.5'的表述在数学上依赖于 V 和 P_ask 的具体关系（若 V=P_ask 则 p=0.5, S=0.5；若 V>P_ask 则 p>0.5, S<0.5），但这属于具体数值案例而非结构性冗余，整体分解合格。）
