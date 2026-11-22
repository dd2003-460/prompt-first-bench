# N53: SEM 模型识别条件：归因决策规则要求模型满足过度识别条件，即外生变量数 > 内生变量数，且各驱动指标 (S_buyer, R_strategic, B_alg

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

SEM 模型识别条件：归因决策规则要求模型满足过度识别条件，即外生变量数 > 内生变量数，且各驱动指标 (S_buyer, R_strategic, B_algo) 与结果变量 (T_close, P_markup) 之间的路径系数需通过最大似然估计 (MLE) 求解，残差平方和 (RSS) 需小于 0.1 * 总方差。

## Corrected Claim

SEM 模型识别条件：归因决策规则要求模型满足过度识别条件，即外生变量数 > 内生变量数，且各驱动指标 (S_buyer, R_strategic, B_algo) 与结果变量 (T_close, P_markup) 之间的路径系数需通过最大似然估计 (MLE) 求解，残差平方和 (RSS) 需小于 0.1 * 总方差。

## Evidence

先验知识/题面给定，逻辑校验通过：SEM 过度识别条件（外生变量数 > 内生变量数）是模型可识别性的标准数学要求，MLE 是结构方程模型的标准估计方法，RSS 阈值属于模型拟合优度的具体设定，逻辑自洽且无内部矛盾。

## Search Query

structural equation model identification conditions maximum likelihood estimation
