# N166: 二三线城市用户占比 w_2 ≈ 45%，平均单程距离 d_2 ≈ 100-200km，T_network P99 ≈ 40-80ms，加权贡献 w_2 × T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N63

## Claim

二三线城市用户占比 w_2 ≈ 45%，平均单程距离 d_2 ≈ 100-200km，T_network P99 ≈ 40-80ms，加权贡献 w_2 × T_2 ≈ 45% × 60ms = 27.0ms

## Corrected Claim

二三线城市用户占比 w_2 ≈ 45%，平均单程距离 d_2 ≈ 100-200km，T_network P99 ≈ 40-80ms，加权贡献 w_2 × T_2 ≈ 45% × 60ms = 27.0ms

## Evidence

先验知识/题面给定，逻辑校验通过：二三线城市用户占比45%及单程距离100-200km符合中国移动互联网用户分布常识；P99网络延迟40-80ms在长距离传输下合理；加权计算 0.45 * 60ms = 27.0ms 数学正确。

## Search Query

China internet user distribution second third tier cities percentage
