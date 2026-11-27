# N216: 下游投影2：挂价分布宽度 P_ask 的标准差计算，Var(P_ask) = Var(λ * δ_loss * P_ref + ε_s) = (0.225 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N57

## Claim

下游投影2：挂价分布宽度 P_ask 的标准差计算，Var(P_ask) = Var(λ * δ_loss * P_ref + ε_s) = (0.225 * P_ref)² + 0.04² * P_ref²，标准差为 P_ref * sqrt(0.225² + 0.04²) ≈ 0.228 * P_ref。

## Corrected Claim

下游投影2：挂价分布宽度 P_ask 的标准差计算，Var(P_ask) = Var(λ * δ_loss * P_ref + ε_s) = (0.225 * P_ref)² + 0.04² * P_ref²，标准差为 P_ref * sqrt(0.225² + 0.04²) ≈ 0.228 * P_ref。

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式 Var(aX+bY) 在独立变量下为 a²Var(X)+b²Var(Y)，此处假设 λ*δ_loss 为常数系数 0.225，ε_s 为独立噪声项且标准差为 0.04*P_ref，计算 sqrt(0.225² + 0.04²) ≈ 0.228 符合数学推导。
