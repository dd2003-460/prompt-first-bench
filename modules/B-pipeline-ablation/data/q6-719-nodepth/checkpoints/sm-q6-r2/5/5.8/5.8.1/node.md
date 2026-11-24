# N120: 自建10个POP点单点故障风险的成本惩罚项 = P_POP_Failure × (Affected_Traffic_Ratio × Business_Loss_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

自建10个POP点单点故障风险的成本惩罚项 = P_POP_Failure × (Affected_Traffic_Ratio × Business_Loss_Per_Unit_Traffic × Recovery_Time)，其中P_POP_Failure为单POP年故障率，Affected_Traffic_Ratio=0.1，Business_Loss_Per_Unit_Traffic为每GB流量损失价值。

## Corrected Claim

自建10个POP点单点故障风险的成本惩罚项 = P_POP_Failure × (Affected_Traffic_Ratio × Business_Loss_Per_Unit_Traffic × Recovery_Time)，其中P_POP_Failure为单POP年故障率，Affected_Traffic_Ratio=0.1，Business_Loss_Per_Unit_Traffic为每GB流量损失价值。

## Evidence

先验知识/题面给定，逻辑校验通过
