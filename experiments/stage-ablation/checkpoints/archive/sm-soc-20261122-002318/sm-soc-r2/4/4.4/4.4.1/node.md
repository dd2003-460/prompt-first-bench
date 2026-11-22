# N64: ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_n

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_new 为干预前后成交量，P_old/P_new 为干预前后平均成交价，需分别估算成交量弹性和价格弹性。

## Corrected Claim

ΔGMV 的计算公式：ΔGMV = (V_new - V_old) * P_avg + V_old * (P_new - P_old)，其中 V_old/V_new 为干预前后成交量，P_old/P_new 为干预前后平均成交价，需分别估算成交量弹性和价格弹性。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是标准的微分近似分解（ΔGMV ≈ ΔV*P + V*ΔP），量纲正确（成交量*价格=金额），符合经济学中总收益变动分解的基本原理。
