# N607: 取回延迟对 RTO 代价的量化修正：若业务要求 RTO < 4h，批量取回的 T_delay_batch (5-12h) 超出阈值，此时必须使用标准取回或归档直

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253, N254, N255

## Claim

取回延迟对 RTO 代价的量化修正：若业务要求 RTO < 4h，批量取回的 T_delay_batch (5-12h) 超出阈值，此时必须使用标准取回或归档直接读取（若支持），否则 RTO 违约代价 C_penalty_rto 需加入成本模型，C_total_retrieval = C_retrieval_fee + C_penalty_rto

## Corrected Claim

取回延迟对 RTO 代价的量化修正：若业务要求 RTO < 4h，批量取回的 T_delay_batch (5-12h) 超出阈值，此时必须使用标准取回或归档直接读取（若支持），否则 RTO 违约代价 C_penalty_rto 需加入成本模型，C_total_retrieval = C_retrieval_fee + C_penalty_rto

## Evidence

先验知识/题面给定，逻辑校验通过：RTO定义与延迟阈值的比较符合逻辑，成本模型中引入违约惩罚项符合经济学直觉及灾备管理最佳实践。
