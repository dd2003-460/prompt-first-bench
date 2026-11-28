# N191: 分块检索策略的额外延迟开销 T_chunk_overhead = N_chunks * (T_retrieve + T_merge)，其中N_chunks = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

分块检索策略的额外延迟开销 T_chunk_overhead = N_chunks * (T_retrieve + T_merge)，其中N_chunks = L_ctx / chunk_size，T_retrieve为单次检索延迟（参考N51约0.5s），T_merge为结果合并耗时（约0.1s），需评估是否抵消质量增益

## Corrected Claim

分块检索策略的额外延迟开销 T_chunk_overhead = N_chunks * (T_retrieve + T_merge)，其中N_chunks = L_ctx / chunk_size，T_retrieve为单次检索延迟（参考N51约0.5s），T_merge为结果合并耗时（约0.1s），需评估是否抵消质量增益

## Evidence

先验知识/题面给定，逻辑校验通过
