# N201: 归一化请求密度 \( D_R = Q_{total} / N \) 用于判断冷启动收敛速度；本题中 \( D_R = 500 \text{req/day/obj

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

归一化请求密度 \( D_R = Q_{total} / N \) 用于判断冷启动收敛速度；本题中 \( D_R = 500 \text{req/day/obj} \)，结合 Poisson 分布，单对象在 1 小时内至少被访问一次的概率 \( P(\ge 1) = 1 - e^{-500/24} \approx 1 \)，表明系统迅速进入稳态，冷启动效应可忽略。

## Corrected Claim

归一化请求密度 \( D_R = Q_{total} / N \) 用于判断冷启动收敛速度；本题中 \( D_R = 500 \text{req/day/obj} \)，结合 Poisson 分布，单对象在 1 小时内至少被访问一次的概率 \( P(\ge 1) = 1 - e^{-500/24} \approx 1 \)，表明系统迅速进入稳态，冷启动效应可忽略。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

cold start convergence Poisson distribution request density
