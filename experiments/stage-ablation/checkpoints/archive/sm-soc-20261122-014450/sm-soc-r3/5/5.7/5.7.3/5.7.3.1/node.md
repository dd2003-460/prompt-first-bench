# N338: 蒙特卡洛抽样策略采用拉丁超立方采样 (LHS) 而非简单随机采样，以确保 H1-H5 在各自分布域内的均匀覆盖；每次抽样生成一组参数向量 θ^(k)，代入均衡模

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N108

## Claim

蒙特卡洛抽样策略采用拉丁超立方采样 (LHS) 而非简单随机采样，以确保 H1-H5 在各自分布域内的均匀覆盖；每次抽样生成一组参数向量 θ^(k)，代入均衡模型计算干预效果 Y^(k)，记录 Y^(k) < Y_threshold (最小干预有效阈值) 的二值结果 I^(k)。

## Corrected Claim

蒙特卡洛抽样策略采用拉丁超立方采样 (LHS) 而非简单随机采样，以确保 H1-H5 在各自分布域内的均匀覆盖；每次抽样生成一组参数向量 θ^(k)，代入均衡模型计算干预效果 Y^(k)，记录 Y^(k) < Y_threshold (最小干预有效阈值) 的二值结果 I^(k)。

## Evidence

先验知识/题面给定，逻辑校验通过：LHS 是蒙特卡洛模拟中确保多维参数空间均匀覆盖的标准策略，且二值结果记录逻辑自洽。

## Search Query

Latin Hypercube Sampling Monte Carlo simulation parameter space coverage efficiency
