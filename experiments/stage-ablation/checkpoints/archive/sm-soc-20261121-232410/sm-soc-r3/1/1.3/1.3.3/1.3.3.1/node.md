# N112: P_cost 的时间动态分解：P_cost(t) = P_initial * (1 + i_storage * t/365)，其中 i_storage 为年化存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

P_cost 的时间动态分解：P_cost(t) = P_initial * (1 + i_storage * t/365)，其中 i_storage 为年化存储/折旧成本率，典型值 10%，t 为持有天数；例如持有 180 天，P_cost 增加 5%，即从 50 升至 52.5。

## Corrected Claim

P_cost 的时间动态分解：P_cost(t) = P_initial * (1 + i_storage * t/365)，其中 i_storage 为年化存储/折旧成本率，典型值 10%，t 为持有天数；例如持有 180 天，P_cost 增加 5%，即从 50 升至 52.5。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P_cost(t) = P_initial * (1 + i_storage * t/365) 为标准的线性年化成本累积模型，量纲一致（t/365 无量纲，i_storage 为比率），数值示例计算正确（50 * (1 + 0.10 * 180/365) = 50 * 1.05 = 52.5），符合基本经济直觉。
