# N139: 动态阈值 δ 的计算公式：δ_t = P90(Deviation_history_top10pct_error_samples)，其中 history_top1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

动态阈值 δ 的计算公式：δ_t = P90(Deviation_history_top10pct_error_samples)，其中 history_top10pct_error_samples 为过去 N=100 次人工标注为“错误”的样本中 Deviation 值的集合；若样本不足 30 个，默认 δ=0.25 并标记为 [degraded]。

## Corrected Claim

动态阈值 δ 的计算公式：δ_t = P90(Deviation_history_top10pct_error_samples)，其中 history_top10pct_error_samples 为过去 N=100 次人工标注为“错误”的样本中 Deviation 值的集合；若样本不足 30 个，默认 δ=0.25 并标记为 [degraded]。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic threshold calibration percentile error samples machine learning
