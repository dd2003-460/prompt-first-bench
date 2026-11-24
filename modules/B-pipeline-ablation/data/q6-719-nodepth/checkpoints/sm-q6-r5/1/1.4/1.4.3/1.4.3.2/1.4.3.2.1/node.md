# N477: 成本放大系数 C_amp 的推导：C_amp = 1 + (C_overload_penalty / C_base_bw)，其中 C_overload_pena

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N153

## Claim

成本放大系数 C_amp 的推导：C_amp = 1 + (C_overload_penalty / C_base_bw)，其中 C_overload_penalty 为过载导致的 SLA 违约赔偿或用户体验损失，C_base_bw 为基础带宽成本；需量化 C_overload_penalty 与过载时长、幅度的关系。

## Corrected Claim

成本放大系数 C_amp 的推导：C_amp = 1 + (C_overload_penalty / C_base_bw)，其中 C_overload_penalty 为过载导致的 SLA 违约赔偿或用户体验损失，C_base_bw 为基础带宽成本；需量化 C_overload_penalty 与过载时长、幅度的关系。

## Evidence

先验知识/题面给定，逻辑校验通过
