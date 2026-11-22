# N57: 地位信号的成本-收益约束：根据信号博弈理论（Spence Signaling），高挂价作为信号的成本 C_signal 必须满足：对于高净值卖家，C_signa

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

地位信号的成本-收益约束：根据信号博弈理论（Spence Signaling），高挂价作为信号的成本 C_signal 必须满足：对于高净值卖家，C_signal < Benefit(筛选高质买家)；对于低净值卖家，C_signal > Benefit(筛选高质买家)。具体地，C_signal 应量化为因高挂价导致的额外持有成本（资金占用利息 + 机会成本），即 C_signal = (P_list - P_market) * r * t_wait。

## Corrected Claim

地位信号的成本-收益约束：根据信号博弈理论（Spence Signaling），高挂价作为信号的成本 C_signal 必须满足：对于高净值卖家，C_signal < Benefit(筛选高质买家)；对于低净值卖家，C_signal > Benefit(筛选高质买家)。具体地，C_signal 应量化为因高挂价导致的额外持有成本（资金占用利息 + 机会成本），即 C_signal = (P_list - P_market) * r * t_wait。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述准确描述了Spence信号博弈中分离均衡（Separating Equilibrium）的激励相容约束条件（高类型卖家发送信号收益大于成本，低类型卖家发送信号收益小于成本），且给出的成本量化公式在经济学直觉上合理（基于价差、利率和时间的持有成本）。
