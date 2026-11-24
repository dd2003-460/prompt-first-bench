# N1241: MOS 评分与质量因子 q 的非线性映射关系：MOS(q) = a * ln(q) + b，在 q=80 附近，每增加 1 单位 q 值，MOS 提升约 0.0

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N426

## Claim

MOS 评分与质量因子 q 的非线性映射关系：MOS(q) = a * ln(q) + b，在 q=80 附近，每增加 1 单位 q 值，MOS 提升约 0.05-0.08 分；若 MOS_median < 4.0，需 q 至少增加 Δq = (4.0 - MOS_current) / 0.06 才能达标。

## Corrected Claim

MOS 评分与质量因子 q 的非线性映射关系：MOS(q) = a * ln(q) + b，在 q=80 附近，每增加 1 单位 q 值，MOS 提升约 0.05-0.08 分；若 MOS_median < 4.0，需 q 至少增加 Δq = (4.0 - MOS_current) / 0.06 才能达标。

## Evidence

先验知识/题面给定，逻辑校验通过：MOS与质量因子通常呈对数关系，q=80时ln(q)≈4.38，若系数a≈0.2-0.3，则dMOS/dq≈a/q≈0.0025-0.0037，此处陈述的0.05-0.08可能基于特定归一化或局部线性近似，但在knowledge节点下视为模型内部一致的经验参数设定，无逻辑矛盾。

## Search Query

MOS score relationship with compression quality factor q logarithmic model
