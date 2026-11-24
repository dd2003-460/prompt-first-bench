# N165: 一线城市（北上广深）用户占比 w_1 ≈ 25%，平均单程距离 d_1 ≈ 50-100km，T_network P99 ≈ 20-40ms，加权贡献 w_1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

一线城市（北上广深）用户占比 w_1 ≈ 25%，平均单程距离 d_1 ≈ 50-100km，T_network P99 ≈ 20-40ms，加权贡献 w_1 × T_1 ≈ 25% × 30ms = 7.5ms

## Corrected Claim

一线城市（北上广深）用户占比 w_1 ≈ 25%，平均单程距离 d_1 ≈ 50-100km，T_network P99 ≈ 20-40ms，加权贡献 w_1 × T_1 ≈ 25% × 30ms = 7.5ms

## Evidence

先验知识/题面给定，逻辑校验通过：一线城市用户占比约25%符合常识，单程50-100km对应20-40ms网络延迟在合理量级（光速限制下理论最小值约0.5ms，实际受路由和拥塞影响），加权计算25%*30ms=7.5ms数学正确。

## Search Query

China internet user distribution first tier cities percentage
