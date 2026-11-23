# N167: 一线城市用户到最近边缘节点的物理距离 d_city 分布：基于用户地理密度与POP覆盖半径，假设80%用户位于半径 R=20km 内，平均直线距离 d_avg 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

一线城市用户到最近边缘节点的物理距离 d_city 分布：基于用户地理密度与POP覆盖半径，假设80%用户位于半径 R=20km 内，平均直线距离 d_avg ≈ 13km（2D均匀分布平均距离 r/2），光纤传播延迟 t_prop = 2 * 13km / 2.0e8 * 1.05 ≈ 0.14ms，忽略不计，主要延迟来自链路处理与排队，故 RTT_city_base ≈ 5-10ms（含接入网最后一公里延迟）。

## Corrected Claim

一线城市用户到最近边缘节点的物理距离 d_city 分布：基于用户地理密度与POP覆盖半径，假设80%用户位于半径 R=20km 内，平均直线距离 d_avg ≈ 13km（2D均匀分布平均距离 r/2），光纤传播延迟 t_prop = 2 * 13km / 2.0e8 * 1.05 ≈ 0.14ms，忽略不计，主要延迟来自链路处理与排队，故 RTT_city_base ≈ 5-10ms（含接入网最后一公里延迟）。

## Evidence

先验知识/题面给定，逻辑校验通过：2D均匀分布平均距离r/2推导正确，光纤延迟量级合理，RTT估算符合工程常识

## Search Query

CDN edge node coverage radius average distance urban China
