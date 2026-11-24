# N263: 扩容期间的服务降级成本 Cost_Degradation = (T_expansion_duration × Traffic_During_Expansion)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

扩容期间的服务降级成本 Cost_Degradation = (T_expansion_duration × Traffic_During_Expansion) × (P99_Latency_Penalty_Per_Byte × Business_Value_Per_Byte)，其中 T_expansion_duration 通常为 4-8 小时，P99 延迟惩罚系数需根据 N136 的留存率模型量化

## Corrected Claim

扩容期间的服务降级成本 Cost_Degradation = (T_expansion_duration × Traffic_During_Expansion) × (P99_Latency_Penalty_Per_Byte × Business_Value_Per_Byte)，其中 T_expansion_duration 通常为 4-8 小时，P99 延迟惩罚系数需根据 N136 的留存率模型量化

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN maintenance window service degradation cost calculation
