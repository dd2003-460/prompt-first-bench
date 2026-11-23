# N140: 策略A（全公有云）在启用Premium Tier后的修正成本函数：C_A_premium(Q) = Max(Monthly_Usage_Cost_Premium

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

策略A（全公有云）在启用Premium Tier后的修正成本函数：C_A_premium(Q) = Max(Monthly_Usage_Cost_Premium, CUD_Threshold) / (Q/1000)。其中 Monthly_Usage_Cost_Premium = Q * s_avg * Premium_BW_Price + Q * P_req_premium。若 Q_daily=1.8M，s_avg=1.1MB，Premium_BW_Price=0.28元/GB，则月流量成本 ≈ 1.8M * 30 * 0.0011 * 0.28 ≈ 16,632 元，超过10,000元门槛，CUD生效。

## Corrected Claim

策略A（全公有云）在启用Premium Tier后的修正成本函数：C_A_premium(Q) = Max(Monthly_Usage_Cost_Premium, CUD_Threshold) / (Q/1000)。其中 Monthly_Usage_Cost_Premium = Q * s_avg * Premium_BW_Price + Q * P_req_premium。若 Q_daily=1.8M，s_avg=1.1MB，Premium_BW_Price=0.28元/GB，则月流量成本 ≈ 1.8M * 30 * 0.0011 * 0.28 ≈ 16,632 元，超过10,000元门槛，CUD生效。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 1.8M * 30 * 0.0011 * 0.28 ≈ 16,632 元，量级与逻辑自洽，且符合公有云计费常识。
