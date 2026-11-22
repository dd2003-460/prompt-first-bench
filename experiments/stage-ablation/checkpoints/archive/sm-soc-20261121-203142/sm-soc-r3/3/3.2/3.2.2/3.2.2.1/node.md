# N171: 买家效用变化的共享随机源为流量重分配导致的搜索成本波动 C_search_new，其方差 Var(C_search) 取决于平台算法调整引起的曝光分布偏移量 ε

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

买家效用变化的共享随机源为流量重分配导致的搜索成本波动 C_search_new，其方差 Var(C_search) 取决于平台算法调整引起的曝光分布偏移量 ε_traffic，具体需计算 C_search_new = C_search_old * (1 + ε_traffic * β_search)，其中 β_search 为搜索成本对流量密度的弹性系数。

## Corrected Claim

买家效用变化的共享随机源为流量重分配导致的搜索成本波动 C_search_new，其方差 Var(C_search) 取决于平台算法调整引起的曝光分布偏移量 ε_traffic，具体需计算 C_search_new = C_search_old * (1 + ε_traffic * β_search)，其中 β_search 为搜索成本对流量密度的弹性系数。

## Evidence

先验知识/题面给定，逻辑校验通过
