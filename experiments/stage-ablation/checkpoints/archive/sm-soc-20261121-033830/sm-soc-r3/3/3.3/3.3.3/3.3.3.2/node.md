# N202: GMV背离风险的临界点计算：GMV = P * Q，d(GMV)/dP = Q(1 + ε)；当 ε = -1 时 GMV 达到极值。若实测 ε = -0.8，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

GMV背离风险的临界点计算：GMV = P * Q，d(GMV)/dP = Q(1 + ε)；当 ε = -1 时 GMV 达到极值。若实测 ε = -0.8，则涨价 10% 导致 GMV 变化率 ≈ 10% * (1 - 0.8) = 2%，需计算在何种涨价幅度下 GMV 开始下降（即 P_new/P_old > 1/|ε| 的阈值）。

## Corrected Claim

GMV背离风险的临界点计算：GMV = P * Q，d(GMV)/dP = Q(1 + ε)；当 ε = -1 时 GMV 达到极值。若实测 ε = -0.8，则涨价 10% 导致 GMV 变化率 ≈ 10% * (1 - 0.8) = 2%，需计算在何种涨价幅度下 GMV 开始下降（即 P_new/P_old > 1/|ε| 的阈值）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于微积分与弹性定义，GMV=P*Q，d(GMV)/dP = Q(1+ε)，当ε=-1时导数为0，GMV达到极值；涨价10%时GMV变化率≈10%*(1-0.8)=2%，阈值条件P_new/P_old > 1/|ε|推导正确。
