# N109: MMLU-Pro 基准中各学科子集 (STEM, Humanities, Social Sciences) 的准确率方差 σ_subject ≈ 5.0%，导致

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

MMLU-Pro 基准中各学科子集 (STEM, Humanities, Social Sciences) 的准确率方差 σ_subject ≈ 5.0%，导致整体标准误 SE ≈ σ_subject / √n_subjects ≈ 1.2% (假设 n_subjects=16 大类)

## Corrected Claim

MMLU-Pro 基准中各学科子集的准确率方差 σ_subject 约为 5.0%（经验估计），若按 n≈14 个大类计算，整体标准误 SE ≈ σ_subject / √n ≈ 1.3%。

## Evidence

[质询]MMLU-Pro 的官方定义中通常包含 14 个主要类别（Categories），而非 16 个大类；此外，不同学科子集间的准确率方差 σ_subject ≈ 5.0% 是一个具体的经验统计值，并非从基准定义或第一性原理可直接推导出的常数，其具体数值依赖于特定模型的表现分布，存在口径和数值准确性风险。 | source=knowledge，逻辑公式 SE = σ/√n 自洽，但 n=16 与 MMLU-Pro 常见的 14 类分类不符，且 σ=5.0% 为经验估计值，缺乏直接来源支持以确认其精确性，故降级。
