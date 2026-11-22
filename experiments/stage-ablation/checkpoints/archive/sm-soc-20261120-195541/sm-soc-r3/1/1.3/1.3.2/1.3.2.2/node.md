# N89: N29中T_deal>30天时P_ask*趋于C_acq的收敛速率：当T_deal=30, α=0.01时，P_ask* = C_acq + 100*(1-e^

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29, N30, N31

## Claim

N29中T_deal>30天时P_ask*趋于C_acq的收敛速率：当T_deal=30, α=0.01时，P_ask* = C_acq + 100*(1-e^-0.3) ≈ C_acq + 25.9，距C_acq仍有25.9的差距，未完全收敛；需T_deal>100天（α*T>1）时误差才<37%，该断言‘趋于C_acq’在30天尺度下不成立，需修正阈值或引入渐近展开。

## Corrected Claim

N29中T_deal>30天时P_ask*趋于C_acq的收敛速率：当T_deal=30, α=0.01时，P_ask* = C_acq + 100*(1-e^-0.3) ≈ C_acq + 25.9，距C_acq仍有25.9的差距，未完全收敛；需T_deal>100天（α*T>1）时误差才<37%，该断言‘趋于C_acq’在30天尺度下不成立，需修正阈值或引入渐近展开。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1-e^-0.3 ≈ 0.2592，与陈述中的 25.9 一致；且 α*T>1 时误差 e^-1 ≈ 36.8% < 37%，逻辑自洽。
