# N126: 用户到边缘节点的单程物理距离 d_user_edge 取决于用户地理分布与最近节点覆盖半径，一线城市平均约 50km，偏远地区平均约 300km，用于计算 RT

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

用户到边缘节点的单程物理距离 d_user_edge 取决于用户地理分布与最近节点覆盖半径，一线城市平均约 50km，偏远地区平均约 300km，用于计算 RTT_min 中的 d 参数。

## Corrected Claim

用户到边缘节点的单程物理距离 d_user_edge 取决于用户地理分布与最近节点覆盖半径，一线城市平均约 50km，偏远地区平均约 300km，用于计算 RTT_min 中的 d 参数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

average distance user to nearest CDN PoP China urban rural
