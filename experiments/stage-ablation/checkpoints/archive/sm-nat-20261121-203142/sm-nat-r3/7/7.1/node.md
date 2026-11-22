# N218: Gaussian Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = P(U_S > 1-(10)^{-1.1}, U_R >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Gaussian Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = P(U_S > 1-(10)^{-1.1}, U_R > 1-(10)^{-0.9})，其中 U_S, U_R 为标准正态 Copula 变量，需计算该二元正态尾部概率的具体数值

## Corrected Claim

Gaussian Copula 预测的尾部联合概率 P(S>10x_min, R>10r_min) = P(U_S > 1-(10)^{-1.1}, U_R > 1-(10)^{-0.9})，其中 U_S, U_R 为标准正态 Copula 变量，需计算该二元正态尾部概率的具体数值

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 定义下，边缘分布的尾部概率通过逆CDF映射到标准正态空间，公式 P(U_S > 1-(10)^{-1.1}, U_R > 1-(10)^{-0.9}) 正确表达了二元正态尾部概率的计算逻辑，量纲与数学定义自洽。
