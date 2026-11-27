# N342: Sobol 分析共享随机源为拉丁超立方采样（LHS）矩阵 $\mathbf{X} \in \mathbb{R}^{N_{samples} \times 4}$，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N112

## Claim

Sobol 分析共享随机源为拉丁超立方采样（LHS）矩阵 $\mathbf{X} \in \mathbb{R}^{N_{samples} \times 4}$，其中 $N_{samples} = 2^{k+1}$ (k=4 个输入变量)，确保各变量边缘分布均匀且无相关性，用于计算一阶和二阶指数。

## Corrected Claim

Sobol 分析共享随机源为拉丁超立方采样（LHS）矩阵 $\mathbf{X} \in \mathbb{R}^{N_{samples} \times 4}$，其中 $N_{samples} = 2^{k+1}$ (k=4 个输入变量)，确保各变量边缘分布均匀且无相关性，用于计算一阶和二阶指数。

## Evidence

先验知识/题面给定，逻辑校验通过：Sobol 分析确实基于拉丁超立方采样（LHS），且样本量 $N=2^{k+1}$ 是满足一阶和二阶指数计算所需最小样本量的标准配置（$k=4$ 时 $N=32$），各变量边缘均匀且无相关性符合 LHS 定义。
