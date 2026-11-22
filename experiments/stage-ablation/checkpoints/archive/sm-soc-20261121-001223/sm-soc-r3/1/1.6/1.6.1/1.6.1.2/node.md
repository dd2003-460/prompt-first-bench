# N130: 联合概率模型的分解项 2：P(Short Cycle | Consultation) 的量化。定义为 1 - e^(-k_deal * T_observatio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

联合概率模型的分解项 2：P(Short Cycle | Consultation) 的量化。定义为 1 - e^(-k_deal * T_observation)，其中 T_observation 为观察窗口（如 48 小时）。该公式源自泊松过程，表示在给定咨询发生的前提下，在 T_observation 内完成成交的概率。若 k_deal * T_observation < 0.1，则此概率近似线性，表明成交主要受转化率和时间窗口限制，而非随机性。

## Corrected Claim

联合概率模型的分解项 2：P(Short Cycle | Consultation) 的量化。定义为 1 - e^(-k_deal * T_observation)，其中 T_observation 为观察窗口（如 48 小时）。该公式源自泊松过程，表示在给定咨询发生的前提下，在 T_observation 内完成成交的概率。若 k_deal * T_observation < 0.1，则此概率近似线性，表明成交主要受转化率和时间窗口限制，而非随机性。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程在时间T内至少发生一次事件的概率公式为1-e^(-λT)，此处λ=k_deal，逻辑自洽且符合数学定义；小量近似1-e^(-x)≈x在x<0.1时成立，推导正确。
