# N126: 共享随机源 R_seller 的具体生成机制定义为：R_seller = U(0,1) 的线性变换，其均值 E[R_seller]=0，方差 Var(R_sel

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

共享随机源 R_seller 的具体生成机制定义为：R_seller = U(0,1) 的线性变换，其均值 E[R_seller]=0，方差 Var(R_seller)=1，且该源独立于商品固有属性 V。

## Corrected Claim

共享随机源 R_seller 的具体生成机制定义为：R_seller = U(0,1) 的线性变换，其均值 E[R_seller]=0，方差 Var(R_seller)=1，且该源独立于商品固有属性 V。

## Evidence

先验知识/题面给定，逻辑校验通过：U(0,1)的线性变换可构造出均值为0、方差为1的随机变量，且独立性为定义属性，无逻辑矛盾。
