# N292: 二手交易卖家损失厌恶系数 λ 的回归估计式：λ_hat = β_λ * (P_ask - P_min) / (P_ref - P_min) + ε，其中 P_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

二手交易卖家损失厌恶系数 λ 的回归估计式：λ_hat = β_λ * (P_ask - P_min) / (P_ref - P_min) + ε，其中 P_ask 为实际挂价，P_min 为保留价格（见 N109），P_ref 为参考价。需报告 β_λ 的标准误 SE(β_λ) 及 t 统计量，若 t < 1.96 则 λ 不显著异于 0，损失厌恶假设不成立。

## Corrected Claim

二手交易卖家损失厌恶系数 λ 的回归估计式：λ_hat = β_λ * (P_ask - P_min) / (P_ref - P_min) + ε，其中 P_ask 为实际挂价，P_min 为保留价格（见 N109），P_ref 为参考价。需报告 β_λ 的标准误 SE(β_λ) 及 t 统计量，若 t < 1.96 则 λ 不显著异于 0，损失厌恶假设不成立。

## Evidence

先验知识/题面给定，逻辑校验通过：该回归设定符合行为经济学中损失厌恶（Loss Aversion）的标准计量模型，t统计量与1.96的阈值对应95%置信水平，逻辑自洽且量纲合理。
