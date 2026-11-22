# N307: 特征值 λ_i 的解析表达式：λ_1, λ_2 = (trace(J) ± √(trace(J)² - 4*det(J))) / 2，需计算 Re(λ_i) 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

特征值 λ_i 的解析表达式：λ_1, λ_2 = (trace(J) ± √(trace(J)² - 4*det(J))) / 2，需计算 Re(λ_i) 的最大绝对值以判断系统收敛速度。

## Corrected Claim

特征值 λ_i 的解析表达式：λ_1, λ_2 = (trace(J) ± √(trace(J)² - 4*det(J))) / 2，需计算 Re(λ_i) 的最大绝对值以判断系统收敛速度。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式为2x2矩阵特征值的标准解析解（二次方程求根公式），且实部最大绝对值确实决定线性系统收敛速度（谱半径），逻辑自洽。
