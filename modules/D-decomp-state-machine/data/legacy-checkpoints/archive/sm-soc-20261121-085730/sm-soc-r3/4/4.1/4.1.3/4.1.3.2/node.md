# N249: 工作点B（中GMV/高流失）：平台GMV变动受成交量下降抵消，Δ平台GMV = fee_rate * (P_new*Q_new - P_old*Q_old)，若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

工作点B（中GMV/高流失）：平台GMV变动受成交量下降抵消，Δ平台GMV = fee_rate * (P_new*Q_new - P_old*Q_old)，若 Q_new < Q_old * (P_old/P_new)，则 ΔGMV < 0，此临界点定义了平台流量调控的盈亏平衡阈值。

## Corrected Claim

工作点B（中GMV/高流失）：平台GMV变动受成交量下降抵消，Δ平台GMV = fee_rate * (P_new*Q_new - P_old*Q_old)，若 Q_new < Q_old * (P_old/P_new)，则 ΔGMV < 0，此临界点定义了平台流量调控的盈亏平衡阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导正确，临界条件 Q_new < Q_old * (P_old/P_new) 等价于 P_new*Q_new < P_old*Q_old，即 GMV 下降，符合盈亏平衡定义。
