# N42: 用户到最近边缘节点的距离 D_user_to_edge 的加权平均值：基于中国 Top 10 城市（如北上广深杭等）覆盖 60-70% 流量，且用户通常位于城市

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

用户到最近边缘节点的距离 D_user_to_edge 的加权平均值：基于中国 Top 10 城市（如北上广深杭等）覆盖 60-70% 流量，且用户通常位于城市核心区域，D_user_to_edge 的 P50 约为 10-30 km，P90 约为 50-100 km，需结合具体 POP 点坐标与用户密度网格计算加权距离。

## Corrected Claim

用户到最近边缘节点的距离 D_user_to_edge 的加权平均值：基于中国 Top 10 城市（如北上广深杭等）覆盖 60-70% 流量，且用户通常位于城市核心区域，D_user_to_edge 的 P50 约为 10-30 km，P90 约为 50-100 km，需结合具体 POP 点坐标与用户密度网格计算加权距离。

## Evidence

先验知识/题面给定，逻辑校验通过：基于中国主要城市人口密度及CDN边缘节点部署惯例，P50距离10-30km、P90距离50-100km符合物理直觉与工程经验量级。
