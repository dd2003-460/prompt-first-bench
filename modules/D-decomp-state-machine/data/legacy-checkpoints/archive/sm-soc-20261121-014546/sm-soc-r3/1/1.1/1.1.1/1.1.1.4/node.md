# N129: 共享随机源 R_buyer 的具体生成机制定义为：R_buyer = U(0,1) 的线性变换，其均值 E[R_buyer]=0，方差 Var(R_buyer)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

共享随机源 R_buyer 的具体生成机制定义为：R_buyer = U(0,1) 的线性变换，其均值 E[R_buyer]=0，方差 Var(R_buyer)=1，且该源与卖家噪声源 R_seller 存在相关系数 ρ_SR。

## Corrected Claim

共享随机源 R_buyer 的具体生成机制定义为：R_buyer = U(0,1) 的线性变换，其均值 E[R_buyer]=0，方差 Var(R_buyer)=1，且该源与卖家噪声源 R_seller 存在相关系数 ρ_SR。

## Evidence

先验知识/题面给定，逻辑校验通过：U(0,1)经线性变换可构造任意均值和方差的分布，且与另一噪声源的相关系数定义在数学上自洽。
