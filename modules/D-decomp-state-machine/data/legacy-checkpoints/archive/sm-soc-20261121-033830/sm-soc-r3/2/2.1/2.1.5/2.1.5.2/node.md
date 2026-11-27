# N164: 高溢价下的买家流失率投影：P_churn_high = 1 - exp(-λ_b(P_high, t) * T_window)，其中 T_window 为观察窗

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N49

## Claim

高溢价下的买家流失率投影：P_churn_high = 1 - exp(-λ_b(P_high, t) * T_window)，其中 T_window 为观察窗口，需代入 λ_b 的均值和方差计算期望流失率。

## Corrected Claim

高溢价下的买家流失率投影：P_churn_high = 1 - exp(-λ_b(P_high, t) * T_window)，其中 T_window 为观察窗口，需代入 λ_b 的均值和方差计算期望流失率。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合泊松过程下事件发生概率的标准定义（1 - exp(-λT)），量纲与逻辑自洽。

## Search Query

buyer churn rate probability exponential decay model
