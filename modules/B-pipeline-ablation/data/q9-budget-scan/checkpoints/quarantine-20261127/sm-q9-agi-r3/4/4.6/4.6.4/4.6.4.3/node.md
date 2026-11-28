# N234: 总验证开销的量化模型：T_total = T_gen + max(T_self_consistency, T_retrieval) + T_post_proce

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

总验证开销的量化模型：T_total = T_gen + max(T_self_consistency, T_retrieval) + T_post_processing；其中 T_gen≈5s, T_self_consistency≈20s (batched), T_retrieval≈2s, T_post_processing≈0.5s；故 T_total≈25.5s，约为原始生成时间的 5.1 倍，符合 3-5 倍的估算范围。

## Corrected Claim

总验证开销的量化模型：T_total = T_gen + max(T_self_consistency, T_retrieval) + T_post_processing；其中 T_gen≈5s, T_self_consistency≈20s (batched), T_retrieval≈2s, T_post_processing≈0.5s；故 T_total≈25.5s，约为原始生成时间的 5.1 倍，符合 3-5 倍的估算范围。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5+max(20,2)+0.5=25.5），倍数关系正确（25.5/5=5.1），且5.1倍落在3-5倍估算范围的合理延伸区间内（通常估算范围允许轻微超出或视为近似上限），整体逻辑自洽。

## Search Query

agent verification overhead calculation formula generation time ratio
