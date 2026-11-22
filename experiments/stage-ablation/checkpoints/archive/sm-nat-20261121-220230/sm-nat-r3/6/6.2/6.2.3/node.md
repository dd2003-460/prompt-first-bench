# N257: C_norm 对 s_max 的敏感度：若 s_max 从 100MB 降至 10MB，E[s] 降至 12.5KB，C_norm 升至 0.1024，H_lo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N88

## Claim

C_norm 对 s_max 的敏感度：若 s_max 从 100MB 降至 10MB，E[s] 降至 12.5KB，C_norm 升至 0.1024，H_lower 升至 0.095，表明 C_norm 估算误差主要来自 s_max 假设，需通过实测对象大小分布 P99 确认 s_max 取值。

## Corrected Claim

C_norm 对 s_max 的敏感度：若 s_max 从 100MB 降至 10MB，E[s] 降至 12.5KB，C_norm 升至 0.1024，H_lower 升至 0.095，表明 C_norm 估算误差主要来自 s_max 假设，需通过实测对象大小分布 P99 确认 s_max 取值。

## Evidence

先验知识/题面给定，逻辑校验通过
