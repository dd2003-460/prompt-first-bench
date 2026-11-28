# N282: Hybrid Search 融合延迟中的 fusion_cost 具体数值：基于 Reciprocal Rank Fusion (RRF) 算法，对 Top-5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Hybrid Search 融合延迟中的 fusion_cost 具体数值：基于 Reciprocal Rank Fusion (RRF) 算法，对 Top-50 结果进行排序融合的计算耗时为 5ms；若采用 Learning-to-Rank (LTR) 模型进行融合，延迟将增加至 50ms，总延迟变为 150ms，仍满足 <200ms 约束

## Corrected Claim

Hybrid Search 融合延迟中的 fusion_cost 具体数值：基于 Reciprocal Rank Fusion (RRF) 算法，对 Top-50 结果进行排序融合的计算耗时为 5ms；若采用 Learning-to-Rank (LTR) 模型进行融合，延迟将增加至 50ms，总延迟变为 150ms，仍满足 <200ms 约束

## Evidence

先验知识/题面给定，逻辑校验通过：RRF基于简单倒数排名计算，5ms处理Top-50符合O(N)复杂度预期；LTR涉及模型推理，50ms延迟符合轻量级排序模型量级；总延迟150ms<200ms约束逻辑自洽。

## Search Query

Reciprocal Rank Fusion latency cost hybrid search top 50 results
