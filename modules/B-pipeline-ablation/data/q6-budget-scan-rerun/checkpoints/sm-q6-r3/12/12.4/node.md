# N410: 运维加班成本的量化公式：C_overtime = T_fault_response × N_engineers_on_call × hourly_rate_ov

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

运维加班成本的量化公式：C_overtime = T_fault_response × N_engineers_on_call × hourly_rate_overtime，其中 T_fault_response 为平均故障响应时间（典型值 30-60分钟），N_engineers_on_call 为值班工程师数量（假设1人），hourly_rate_overtime 为加班费率（通常为正常时薪的1.5-2倍）；年预期加班成本 = P_fault × 365 × C_overtime_per_incident

## Corrected Claim

运维加班成本的量化公式：C_overtime = T_fault_response × N_engineers_on_call × hourly_rate_overtime，其中 T_fault_response 为平均故障响应时间（典型值 30-60分钟），N_engineers_on_call 为值班工程师数量（假设1人），hourly_rate_overtime 为加班费率（通常为正常时薪的1.5-2倍）；年预期加班成本 = P_fault × 365 × C_overtime_per_incident

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

DevOps on-call engineer overtime cost calculation SRE incident response
