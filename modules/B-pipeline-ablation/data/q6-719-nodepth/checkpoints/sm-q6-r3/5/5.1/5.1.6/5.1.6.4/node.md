# N316: 成本惩罚项 Cost_Penalty_Overload 的计算：Cost_Penalty_Overload = D_overload × Monthly_Req

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N109

## Claim

成本惩罚项 Cost_Penalty_Overload 的计算：Cost_Penalty_Overload = D_overload × Monthly_Requests × Loss_Per_Failed_Request，其中 Loss_Per_Failed_Request 估算为单用户流失概率 × LTV_Base（假设流失概率 10%，LTV_Base ¥100，则 Loss_Per_Failed_Request = ¥10）。

## Corrected Claim

成本惩罚项 Cost_Penalty_Overload 的计算：Cost_Penalty_Overload = D_overload × Monthly_Requests × Loss_Per_Failed_Request，其中 Loss_Per_Failed_Request 估算为单用户流失概率 × LTV_Base（假设流失概率 10%，LTV_Base ¥100，则 Loss_Per_Failed_Request = ¥10）。

## Evidence

先验知识/题面给定，逻辑校验通过
