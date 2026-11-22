# N24: 量化TCO对比的条件性结论模板：单卡vs多卡方案的TCO比较必须输出'交叉点预算'（即多卡方案TCO低于单卡方案的最低预算阈值）和'交叉点延迟'（即多卡方案延迟

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

量化TCO对比的条件性结论模板：单卡vs多卡方案的TCO比较必须输出'交叉点预算'（即多卡方案TCO低于单卡方案的最低预算阈值）和'交叉点延迟'（即多卡方案延迟优势开始抵消成本劣势的延迟阈值）；例如'当预算>25k且要求延迟<150ms时，2×RTX 4090的3年TCO比1×L40低18%，但延迟仅快23%'，所有数值需标注来源和置信区间

## Corrected Claim

量化TCO对比的条件性结论模板：单卡vs多卡方案的TCO比较必须输出'交叉点预算'（即多卡方案TCO低于单卡方案的最低预算阈值）和'交叉点延迟'（即多卡方案延迟优势开始抵消成本劣势的延迟阈值）；例如'当预算>25k且要求延迟<150ms时，2×RTX 4090的3年TCO比1×L40低18%，但延迟仅快23%'，所有数值需标注来源和置信区间

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU vs single GPU TCO crossover LLM inference 2024 2025
