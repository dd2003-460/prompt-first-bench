# N200: GMV 价格弹性分解：ε_GMV_P = (∂GMV/∂P_ask) * (P_ask/GMV) = ε_Q_P + 1，其中 ε_Q_P 为成交量对价格的弹性

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N61

## Claim

GMV 价格弹性分解：ε_GMV_P = (∂GMV/∂P_ask) * (P_ask/GMV) = ε_Q_P + 1，其中 ε_Q_P 为成交量对价格的弹性（通常为负，如 -1.5 至 -2.0）；结合已确认的 ε_GMV_P ∈ [-1.5, -0.8]，可推导出 ε_Q_P ∈ [-2.5, -1.8]，量化了高挂价对成交量的边际抑制效应。

## Corrected Claim

GMV 价格弹性分解：ε_GMV_P = (∂GMV/∂P_ask) * (P_ask/GMV) = ε_Q_P + 1，其中 ε_Q_P 为成交量对价格的弹性（通常为负，如 -1.5 至 -2.0）；结合已确认的 ε_GMV_P ∈ [-1.5, -0.8]，可推导出 ε_Q_P ∈ [-2.5, -1.8]，量化了高挂价对成交量的边际抑制效应。

## Evidence

先验知识/题面给定，逻辑校验通过：GMV=P*Q，对P求导得 ∂GMV/∂P = Q + P*(∂Q/∂P)，两边同乘 P/GMV 即得 ε_GMV_P = 1 + ε_Q_P。代入区间 [-1.5, -0.8] 计算 ε_Q_P = ε_GMV_P - 1，得 [-2.5, -1.8]，数学推导严谨且量级符合经济学直觉。
