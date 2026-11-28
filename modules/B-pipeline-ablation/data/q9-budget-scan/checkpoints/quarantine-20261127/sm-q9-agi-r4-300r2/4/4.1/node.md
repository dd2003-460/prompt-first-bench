# N17: 混合调度决策边界：当单次请求的本地推理时间 T_local(L) > (API单价/L_tokens) * L / (1 - p_reject) + T_ove

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

混合调度决策边界：当单次请求的本地推理时间 T_local(L) > (API单价/L_tokens) * L / (1 - p_reject) + T_overhead 时切换至云端，其中 L 为 token 数，p_reject 为投机解码拒绝率

## Corrected Claim

混合调度决策边界：当单次请求的本地推理时间 T_local(L) > (API单价/L_tokens) * L / (1 - p_reject) + T_overhead 时切换至云端，其中 L 为 token 数，p_reject 为投机解码拒绝率

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid local cloud LLM inference cost latency tradeoff threshold formula
