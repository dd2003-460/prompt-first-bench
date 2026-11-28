# N110: Gold Standard 数据集的标注一致性量化指标：采用 Cohen's Kappa 系数 κ 评估两名标注员对 50 篇论文关键事实提取的一致性，要求 κ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Gold Standard 数据集的标注一致性量化指标：采用 Cohen's Kappa 系数 κ 评估两名标注员对 50 篇论文关键事实提取的一致性，要求 κ ≥ 0.75 方可作为基准；若 κ < 0.75，需引入第三仲裁者并使用 Fleiss' Kappa 重新计算，否则 Gold Standard 本身的噪声将导致 F1-score 测量误差 σ_F1 > 0.05，无法准确判定模型能力是否达标。

## Corrected Claim

Gold Standard 数据集的标注一致性量化指标：采用 Cohen's Kappa 系数 κ 评估两名标注员对 50 篇论文关键事实提取的一致性，要求 κ ≥ 0.75 方可作为基准；若 κ < 0.75，需引入第三仲裁者并使用 Fleiss' Kappa 重新计算，否则 Gold Standard 本身的噪声将导致 F1-score 测量误差 σ_F1 > 0.05，无法准确判定模型能力是否达标。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

inter-rater reliability Cohen's Kappa annotation consistency threshold
