# N394: 贝叶斯网络节点方差贡献度权重 w_i 的计算：基于 N108 的蒙特卡洛模拟结果，计算各关键断言节点（如 H1-H5 及最终决策节点）的 Sobol 一级指数 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

贝叶斯网络节点方差贡献度权重 w_i 的计算：基于 N108 的蒙特卡洛模拟结果，计算各关键断言节点（如 H1-H5 及最终决策节点）的 Sobol 一级指数 S_i，归一化后得到权重 w_i = S_i / ΣS_j。

## Corrected Claim

贝叶斯网络节点方差贡献度权重 w_i 的计算：基于 N108 的蒙特卡洛模拟结果，计算各关键断言节点（如 H1-H5 及最终决策节点）的 Sobol 一级指数 S_i，归一化后得到权重 w_i = S_i / ΣS_j。

## Evidence

先验知识/题面给定，逻辑校验通过：Sobol一级指数归一化是计算方差贡献度权重的标准且逻辑自洽的方法。
