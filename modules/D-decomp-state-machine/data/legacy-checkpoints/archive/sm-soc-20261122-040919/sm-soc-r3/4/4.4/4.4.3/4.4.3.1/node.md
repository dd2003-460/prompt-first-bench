# N312: 动态修正因子 $\alpha(P(H))$ 的线性近似公式：$\theta_{adj}(P(H)) = 0.8 + \beta \cdot (0.5 - P(H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

动态修正因子 $\alpha(P(H))$ 的线性近似公式：$\theta_{adj}(P(H)) = 0.8 + \beta \cdot (0.5 - P(H))$。若设定当 $P(H)=0.1$ 时 $\theta_{adj}=0.85$，则斜率 $\beta = (0.85 - 0.8) / (0.5 - 0.1) = 0.125$。因此，对于任意先验 $P(H)$，调整后阈值 $\theta_{adj} = 0.8 + 0.125 \cdot (0.5 - P(H))$。

## Corrected Claim

动态修正因子 $\alpha(P(H))$ 的线性近似公式：$\theta_{adj}(P(H)) = 0.8 + \beta \cdot (0.5 - P(H))$。若设定当 $P(H)=0.1$ 时 $\theta_{adj}=0.85$，则斜率 $\beta = (0.85 - 0.8) / (0.5 - 0.1) = 0.125$。因此，对于任意先验 $P(H)$，调整后阈值 $\theta_{adj} = 0.8 + 0.125 \cdot (0.5 - P(H))$。

## Evidence

先验知识/题面给定，逻辑校验通过：线性方程两点式推导正确，数值计算无误（0.05/0.4=0.125），公式自洽。
