# N232: P(sale|P_high) 的估计模型采用逻辑斯蒂需求函数 P(sale|P) = 1 / (1 + exp(-k * (V_buyer - P)))，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

P(sale|P_high) 的估计模型采用逻辑斯蒂需求函数 P(sale|P) = 1 / (1 + exp(-k * (V_buyer - P)))，其中 k 为买家价格敏感度系数，基准值 k=2.0，需结合 N106 中 H5 的分布进行蒙特卡洛抽样以获取置信区间。

## Corrected Claim

P(sale|P_high) 的估计模型采用逻辑斯蒂需求函数 P(sale|P) = 1 / (1 + exp(-k * (V_buyer - P)))，其中 k 为买家价格敏感度系数，基准值 k=2.0，需结合 N106 中 H5 的分布进行蒙特卡洛抽样以获取置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过
