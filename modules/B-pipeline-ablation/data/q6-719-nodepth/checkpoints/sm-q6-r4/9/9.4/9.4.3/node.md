# N394: 高延迟/低成本工作点：假设公有云 P99 为 50ms，自建为 60ms（因架构复杂度高延迟 10ms），则 ΔRetention 为负值 -0.05%，导致 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N139

## Claim

高延迟/低成本工作点：假设公有云 P99 为 50ms，自建为 60ms（因架构复杂度高延迟 10ms），则 ΔRetention 为负值 -0.05%，导致 ΔLTV = -¥0.06/用户/月。即使 Unit_Cost_Diff 为负（自建更便宜，如 -¥0.02），总收益 ΔLTV + Unit_Cost_Diff = -0.08 < 0，自建策略在长期 ROI 上劣于公有云

## Corrected Claim

高延迟/低成本工作点：假设公有云 P99 为 50ms，自建为 60ms（因架构复杂度高延迟 10ms），则 ΔRetention 为负值 -0.05%，导致 ΔLTV = -¥0.06/用户/月。即使 Unit_Cost_Diff 为负（自建更便宜，如 -¥0.02），总收益 ΔLTV + Unit_Cost_Diff = -0.08 < 0，自建策略在长期 ROI 上劣于公有云

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（-0.06 + (-0.02) = -0.08 < 0），符合经济直觉（延迟增加导致留存下降，抵消成本优势后总收益为负）。
