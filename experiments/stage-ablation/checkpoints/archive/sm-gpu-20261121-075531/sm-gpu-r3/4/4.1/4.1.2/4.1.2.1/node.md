# N252: Qwen3-27B 在 BF16 精度下，MMLU-Pro 基准测试的得分需查阅 Qwen3 官方技术报告或 HuggingFace Open LLM Lead

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

Qwen3-27B 在 BF16 精度下，MMLU-Pro 基准测试的得分需查阅 Qwen3 官方技术报告或 HuggingFace Open LLM Leaderboard，当前模型先验知识估计该值在 80-85% 区间，具体数值需检索确认以作为量化后性能下降百分比 (ΔScore%) 的基准分子。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的 MMLU-Pro 得分需查阅官方技术报告或 HuggingFace 榜单确认，当前缺乏可靠数据源，暂无法提供具体数值区间作为量化基准。

## Evidence

[质询]该陈述包含具体的经验性数值估计（80-85%），属于硬件/模型性能指标，无法从第一性原理推导，且当前无检索来源支持该具体区间，存在估计偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B BF16 MMLU-Pro score benchmark
