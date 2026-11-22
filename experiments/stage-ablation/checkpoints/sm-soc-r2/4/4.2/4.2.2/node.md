# N71: ΔP_min = P_current * (R - 1.15) 的可行性约束：需验证 ΔP_min 是否超过卖家可接受的最低售价 Floor Price（参考 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

ΔP_min = P_current * (R - 1.15) 的可行性约束：需验证 ΔP_min 是否超过卖家可接受的最低售价 Floor Price（参考 N31），若 ΔP_min > P_current - Floor Price，则触发强制降价而非建议降价，需计算该约束被触发的概率。

## Corrected Claim

ΔP_min = P_current * (R - 1.15) 的可行性约束：需验证 ΔP_min 是否超过卖家可接受的最低售价 Floor Price（参考 N31），若 ΔP_min > P_current - Floor Price，则触发强制降价而非建议降价，需计算该约束被触发的概率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller floor price constraint on mandatory price reduction recommendation feasibility
