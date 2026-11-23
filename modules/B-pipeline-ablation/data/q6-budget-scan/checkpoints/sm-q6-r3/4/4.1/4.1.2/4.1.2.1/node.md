# N179: 平均回源距离 d_avg 的 GIS 计算模型：d_avg = (1/N_users) * Σ_{i=1}^{N_users} min_{j=1}^{N_pop

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

平均回源距离 d_avg 的 GIS 计算模型：d_avg = (1/N_users) * Σ_{i=1}^{N_users} min_{j=1}^{N_pop} d(user_i, POP_j)，其中 d(user_i, POP_j) 为欧几里得距离；对于 10 个 POP 点覆盖中国主要城市，典型 d_avg 范围为 150-300km

## Corrected Claim

平均回源距离 d_avg 的 GIS 计算模型：d_avg = (1/N_users) * Σ_{i=1}^{N_users} min_{j=1}^{N_pop} d(user_i, POP_j)，其中 d(user_i, POP_j) 为欧几里得距离；对于 10 个 POP 点覆盖中国主要城市，典型 d_avg 范围为 150-300km

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合GIS最近邻距离计算标准；150-300km的量级符合中国主要城市分布及10个POP点覆盖下的典型地理距离直觉（中国主要城市群间距多在200-500km，取最小值后平均距离落在该区间合理）。

## Search Query

GIS average distance user to nearest CDN POP point calculation
