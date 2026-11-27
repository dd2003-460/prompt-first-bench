# N287: Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU 准确率具体数值：需查阅 Qwen3 官方技术报告或 HuggingFace 社区发布的 FP8

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88, N89, N90

## Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU 准确率具体数值：需查阅 Qwen3 官方技术报告或 HuggingFace 社区发布的 FP8 量化模型评测数据，预期 BF16 基线准确率约为 70-75% [待核验]，FP8 下降幅度通常 < 0.5%，即 Q_score ≈ 0.995-1.0。

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 精度下的 MMLU 准确率具体数值需查阅官方报告或社区评测；通常 FP8 量化对大模型性能影响较小，预期下降幅度有限，但具体数值需实证数据确认。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU准确率70-75%、FP8下降幅度<0.5%），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 MMLU accuracy benchmark HuggingFace
