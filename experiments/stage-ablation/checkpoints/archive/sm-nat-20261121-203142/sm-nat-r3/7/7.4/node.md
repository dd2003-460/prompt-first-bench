# N221: Gaussian Copula 与 Frank Copula 在尾部 (S>10x_min, R>10r_min) 的相对误差计算：ε_rel = |P_Gau

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Gaussian Copula 与 Frank Copula 在尾部 (S>10x_min, R>10r_min) 的相对误差计算：ε_rel = |P_Gaussian - P_Frank| / P_Frank，需通过数值计算两个概率值后求比，预期 Gaussian 会低估或高估尾部依赖，具体误差值需计算

## Corrected Claim

Gaussian Copula 与 Frank Copula 在尾部 (S>10x_min, R>10r_min) 的相对误差计算：ε_rel = |P_Gaussian - P_Frank| / P_Frank，需通过数值计算两个概率值后求比，预期 Gaussian 会低估或高估尾部依赖，具体误差值需计算

## Evidence

先验知识/题面给定，逻辑校验通过
