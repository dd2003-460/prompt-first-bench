# N178: ESS 崩溃的量化条件：当 L < L_min 时，高挂价策略的期望收益 E(Resident) = (P_ask_high - C) * exp(-α*T_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

ESS 崩溃的量化条件：当 L < L_min 时，高挂价策略的期望收益 E(Resident) = (P_ask_high - C) * exp(-α*T_high(L)) 需低于低挂价策略 E(Deviant) = (P_ask_low - C) * exp(-α*T_low(L))，其中 T_high(L) 随 L 下降呈非线性上升，需计算使不等式翻转的临界流动性 L_critical。

## Corrected Claim

ESS 崩溃的量化条件：当 L < L_min 时，高挂价策略的期望收益 E(Resident) = (P_ask_high - C) * exp(-α*T_high(L)) 需低于低挂价策略 E(Deviant) = (P_ask_low - C) * exp(-α*T_low(L))，其中 T_high(L) 随 L 下降呈非线性上升，需计算使不等式翻转的临界流动性 L_critical。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

evolutionarily stable strategy collapse condition liquidity threshold expected utility comparison
