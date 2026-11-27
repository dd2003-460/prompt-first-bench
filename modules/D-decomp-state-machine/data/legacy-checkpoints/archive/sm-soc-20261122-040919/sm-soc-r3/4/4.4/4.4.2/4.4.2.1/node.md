# N310: 决策论中阈值0.5的推导基于最小化期望损失（Bayes Risk）。设损失函数 $L(\text{decide } H | \neg H) = L_{FP}$ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

决策论中阈值0.5的推导基于最小化期望损失（Bayes Risk）。设损失函数 $L(\text{decide } H | \neg H) = L_{FP}$ 和 $L(\text{decide } \neg H | H) = L_{FN}$。当 $L_{FP} = L_{FN}$ 时，决策边界为 $P(H|D) = 0.5$；若 $L_{FN} > L_{FP}$（漏报代价更高），则阈值应下调至 $P(H|D) > \frac{L_{FP}}{L_{FP} + L_{FN}}$。

## Corrected Claim

决策论中阈值0.5的推导基于最小化期望损失（Bayes Risk）。设损失函数 $L(\text{decide } H | \neg H) = L_{FP}$ 和 $L(\text{decide } \neg H | H) = L_{FN}$。当 $L_{FP} = L_{FN}$ 时，决策边界为 $P(H|D) = 0.5$；若 $L_{FN} > L_{FP}$（漏报代价更高），则阈值应下调至 $P(H|D) > \frac{L_{FP}}{L_{FP} + L_{FN}}$。

## Evidence

先验知识/题面给定，逻辑校验通过：基于贝叶斯风险最小化推导，当误报损失L_FP与漏报损失L_FN相等时，决策边界确为0.5；当L_FN > L_FP时，阈值公式 P(H|D) > L_FP / (L_FP + L_FN) 符合决策论标准推导。
