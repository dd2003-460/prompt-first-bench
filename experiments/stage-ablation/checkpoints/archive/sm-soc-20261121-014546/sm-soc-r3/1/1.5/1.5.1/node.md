# N51: 质量信号归因比例：买家将高挂价归因于质量信号的比例 q_signal 随挂价偏离度 ΔP 增加而增加，公式为 q_signal = 1 - exp(-ΔP / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

质量信号归因比例：买家将高挂价归因于质量信号的比例 q_signal 随挂价偏离度 ΔP 增加而增加，公式为 q_signal = 1 - exp(-ΔP / σ_buyer)，当 ΔP > 2·σ_buyer 时，q_signal > 0.86，即绝大多数买家认为高价代表高质量。

## Corrected Claim

质量信号归因比例：买家将高挂价归因于质量信号的比例 q_signal 随挂价偏离度 ΔP 增加而增加，公式为 q_signal = 1 - exp(-ΔP / σ_buyer)，当 ΔP > 2·σ_buyer 时，q_signal > 0.86，即绝大多数买家认为高价代表高质量。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 q_signal = 1 - exp(-ΔP / σ_buyer) 为单调递增函数，当 ΔP = 2σ_buyer 时，q_signal = 1 - exp(-2) ≈ 0.8647 > 0.86，数学推导自洽且符合信号理论中价格作为质量信号的基本直觉。

## Search Query

price as quality signal attribution ratio exponential model
