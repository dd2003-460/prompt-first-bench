# N63: 各 POP 点的平均 RTT 贡献值 RTT_avg_j：计算每个 POP 点 j 覆盖用户区域的加权平均 RTT，RTT_avg_j = Σ_{i∈S_j} 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12, N13, N14

## Claim

各 POP 点的平均 RTT 贡献值 RTT_avg_j：计算每个 POP 点 j 覆盖用户区域的加权平均 RTT，RTT_avg_j = Σ_{i∈S_j} (p_i / c_j) * D[i][j]，其中 S_j 为 POP j 覆盖的用户区域集合。

## Corrected Claim

各 POP 点的平均 RTT 贡献值 RTT_avg_j：计算每个 POP 点 j 覆盖用户区域的加权平均 RTT，RTT_avg_j = Σ_{i∈S_j} (p_i / c_j) * D[i][j]，其中 S_j 为 POP j 覆盖的用户区域集合。

## Evidence

先验知识/题面给定，逻辑校验通过
