# N125: 在 ρ=-0.3 的负相关约束下，LRU 工作集字节数 W_LRU_bytes 的解析近似公式为 W_LRU_bytes ≈ N_cap * E[S | P >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在 ρ=-0.3 的负相关约束下，LRU 工作集字节数 W_LRU_bytes 的解析近似公式为 W_LRU_bytes ≈ N_cap * E[S | P > P_cap]，其中 N_cap 为缓存能容纳的对象数，P_cap 为对应分位数

## Corrected Claim

在 ρ=-0.3 的负相关约束下，LRU 工作集字节数 W_LRU_bytes 的解析近似公式为 W_LRU_bytes ≈ N_cap * E[S | P > P_cap]，其中 N_cap 为缓存能容纳的对象数，P_cap 为对应分位数

## Evidence

先验知识/题面给定，逻辑校验通过
