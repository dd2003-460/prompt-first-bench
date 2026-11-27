# N101: 溢价幅度离散度计算：由 λ_loss_i 的方差推导出的卖家溢价幅度 Var(Premium_i) = P_market^2 * (0.25/2.5)^2 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N31

## Claim

溢价幅度离散度计算：由 λ_loss_i 的方差推导出的卖家溢价幅度 Var(Premium_i) = P_market^2 * (0.25/2.5)^2 * Var(ε_seller) = P_market^2 * 0.01 * 0.64 = 0.0064 * P_market^2，即溢价标准差约为 0.08 * P_market (8%)。

## Corrected Claim

溢价幅度离散度计算：由 λ_loss_i 的方差推导出的卖家溢价幅度 Var(Premium_i) = P_market^2 * (0.25/2.5)^2 * Var(ε_seller) = P_market^2 * 0.01 * 0.64 = 0.0064 * P_market^2，即溢价标准差约为 0.08 * P_market (8%)。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.25/2.5=0.1，0.1^2=0.01，0.01*0.64=0.0064，sqrt(0.0064)=0.08，推导链条完整且算术正确。
