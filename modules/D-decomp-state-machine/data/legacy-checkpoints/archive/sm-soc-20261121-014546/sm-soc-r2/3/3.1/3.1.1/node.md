# N63: 共享随机源 R_buyer：买家效用函数中的随机参数集合，包括质量概率 q ~ Beta(2, 3)（均值0.4）和搜索成本 C_search ~ LogNor

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N14

## Claim

共享随机源 R_buyer：买家效用函数中的随机参数集合，包括质量概率 q ~ Beta(2, 3)（均值0.4）和搜索成本 C_search ~ LogNormal(μ=ln(50), σ=0.2)，这两个随机变量共同决定 U_buyer 的期望值和方差。

## Corrected Claim

共享随机源 R_buyer：买家效用函数中的随机参数集合，包括质量概率 q ~ Beta(2, 3)（均值0.4）和搜索成本 C_search ~ LogNormal(μ=ln(50), σ=0.2)，这两个随机变量共同决定 U_buyer 的期望值和方差。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta(2,3)均值确为0.4，LogNormal参数定义符合标准，变量定义与效用函数期望/方差的关系在逻辑上自洽。

## Search Query

buyer utility random parameters quality probability search cost distribution second hand market
