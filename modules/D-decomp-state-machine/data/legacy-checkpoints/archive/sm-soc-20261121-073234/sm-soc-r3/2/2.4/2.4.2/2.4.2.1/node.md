# N194: RDD 断点处的局部线性回归带宽选择：采用 Imbens-Kalyanaraman 最优带宽公式 h_opt = C * (n * f(x_c)^2 / m'(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

RDD 断点处的局部线性回归带宽选择：采用 Imbens-Kalyanaraman 最优带宽公式 h_opt = C * (n * f(x_c)^2 / m'(x_c)^2)^(-1/5)，其中 C 为常数，n 为样本量，f 为密度函数，m' 为斜率，带宽需满足 h < 0.1 * (max(x) - min(x)) 以符合局部性假设。

## Corrected Claim

RDD 断点处的局部线性回归带宽选择：采用 Imbens-Kalyanaraman 最优带宽公式 h_opt = C * (n * f(x_c)^2 / m'(x_c)^2)^(-1/5)，其中 C 为常数，n 为样本量，f 为密度函数，m' 为斜率，带宽需满足 h < 0.1 * (max(x) - min(x)) 以符合局部性假设。

## Evidence

先验知识/题面给定，逻辑校验通过
