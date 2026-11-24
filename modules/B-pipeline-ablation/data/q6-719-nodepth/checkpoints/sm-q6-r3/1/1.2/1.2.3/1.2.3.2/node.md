# N160: 每跳延迟贡献 T_hop 的分解：T_hop = T_transmission + T_propagation + T_processing，其中 T_tran

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

每跳延迟贡献 T_hop 的分解：T_hop = T_transmission + T_propagation + T_processing，其中 T_transmission ≈ 0.1ms（10Gbps 链路），T_propagation ≈ 0.5-1.5ms（取决于距离，光纤速度 200km/ms），T_processing ≈ 0.5-2ms（路由器转发延迟）。总 T_hop 典型值 1-4ms。

## Corrected Claim

每跳延迟贡献 T_hop 的分解：T_hop = T_transmission + T_propagation + T_processing，其中 T_transmission ≈ 0.1ms（10Gbps 链路），T_propagation ≈ 0.5-1.5ms（取决于距离，光纤速度 200km/ms），T_processing ≈ 0.5-2ms（路由器转发延迟）。总 T_hop 典型值 1-4ms。

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps传输1.5KB包约0.1ms，光纤传播速度约200km/ms，路由器处理延迟0.5-2ms，各项量级符合网络工程常识，总和1-4ms合理。

## Search Query

router forwarding delay propagation delay transmission delay per hop
