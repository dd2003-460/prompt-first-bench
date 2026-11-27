# N116: 回归模型 $\Delta_i = k \cdot H_i + \epsilon_i$ 的误差项 $\epsilon_i$ 结构：若 $\epsilon_i$ 存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

回归模型 $\Delta_i = k \cdot H_i + \epsilon_i$ 的误差项 $\epsilon_i$ 结构：若 $\epsilon_i$ 存在显著异方差（Heteroscedasticity），则需使用加权最小二乘法（WLS）或稳健标准误进行估计，否则 $k$ 的标准误会被低估，导致显著性检验失真。

## Corrected Claim

回归模型 $\Delta_i = k \cdot H_i + \epsilon_i$ 的误差项 $\epsilon_i$ 结构：若 $\epsilon_i$ 存在显著异方差（Heteroscedasticity），则需使用加权最小二乘法（WLS）或稳健标准误进行估计，否则 $k$ 的标准误会被低估，导致显著性检验失真。

## Evidence

先验知识/题面给定，逻辑校验通过：异方差导致OLS标准误估计有偏（通常低估），进而影响t检验和F检验的有效性，WLS或稳健标准误是标准修正方法。

## Search Query

heteroscedasticity robust standard errors regression premium estimation used goods
