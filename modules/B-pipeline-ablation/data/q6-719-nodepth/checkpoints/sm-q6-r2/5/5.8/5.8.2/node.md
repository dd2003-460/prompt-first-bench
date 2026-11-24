# N121: 自建节点弹性不足的成本惩罚项 = (Peak_Traffic - Provisioned_Capacity) × P_Overflow × Loss_Per_O

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

自建节点弹性不足的成本惩罚项 = (Peak_Traffic - Provisioned_Capacity) × P_Overflow × Loss_Per_Overflow_Byte，其中Provisioned_Capacity为预置2x峰值带宽，P_Overflow为超出预置容量的概率，Loss_Per_Overflow_Byte为每字节溢出导致的用户流失或降级成本。

## Corrected Claim

自建节点弹性不足的成本惩罚项 = (Peak_Traffic - Provisioned_Capacity) × P_Overflow × Loss_Per_Overflow_Byte，其中Provisioned_Capacity为预置2x峰值带宽，P_Overflow为超出预置容量的概率，Loss_Per_Overflow_Byte为每字节溢出导致的用户流失或降级成本。

## Evidence

先验知识/题面给定，逻辑校验通过
