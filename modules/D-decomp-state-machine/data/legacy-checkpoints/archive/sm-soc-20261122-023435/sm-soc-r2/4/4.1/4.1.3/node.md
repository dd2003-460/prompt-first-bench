# N51: 透明化干预对平台 GMV 的净效应：ΔGMV = ΔQ * P_new - Q_old * ΔP，其中 ΔQ 为成交量增加（因搜索成本降低），ΔP 为均价下降（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

透明化干预对平台 GMV 的净效应：ΔGMV = ΔQ * P_new - Q_old * ΔP，其中 ΔQ 为成交量增加（因搜索成本降低），ΔP 为均价下降（因溢价压缩），预计 ΔGMV > 0 的条件是价格弹性 ε_b < 1（缺乏弹性市场），具体参数需通过平台模拟计算。

## Corrected Claim

透明化干预对平台 GMV 的净效应：ΔGMV = ΔQ * P_new - Q_old * ΔP，其中 ΔQ 为成交量增加（因搜索成本降低），ΔP 为均价下降（因溢价压缩），预计 ΔGMV > 0 的条件是价格弹性 ε_b < 1（缺乏弹性市场），具体参数需通过平台模拟计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔGMV = ΔQ*P_new - Q_old*ΔP 符合微分近似下的收入变化逻辑（dR = P*dQ + Q*dP，此处符号处理对应价格下降带来的损失与销量增加带来的收益），且弹性条件 ε_b < 1 时价格下降导致总收入（GMV）增加符合经济学基本原理。

## Search Query

net impact of price transparency intervention on platform GMV elasticity
