# N32: 初始价差 D 的量化定义：D = (P_listing - P_median) / P_median，其中 P_listing 为卖家挂价，P_median 为

- **status**: pending
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

初始价差 D 的量化定义：D = (P_listing - P_median) / P_median，其中 P_listing 为卖家挂价，P_median 为同类商品过去30天成交中位价，D 的取值区间为 [0.15, 0.25]。

## Corrected Claim

初始价差 D 的量化定义：D = (P_listing - P_median) / P_median，其中 P_listing 为卖家挂价，P_median 为同类商品过去30天成交中位价，D 的取值区间为 [0.15, 0.25]。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅描述了D区间两个边界点的具体数值计算，未涵盖D在区间内的一般定义或中间状态，导致不完备；且两个子节点结构高度相似，本质是同一公式在不同参数下的实例化，存在结构性冗余。）
