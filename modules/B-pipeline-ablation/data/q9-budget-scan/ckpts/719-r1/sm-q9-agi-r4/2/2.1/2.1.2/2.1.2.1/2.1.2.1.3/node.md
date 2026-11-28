# N432: nDCG@10 提升 0.10 对应 Recall@5 提升 0.06 的换算关系：基于线性近似 ΔRecall@5 ≈ 0.6 * ΔnDCG@10，当 Δn

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N145

## Claim

nDCG@10 提升 0.10 对应 Recall@5 提升 0.06 的换算关系：基于线性近似 ΔRecall@5 ≈ 0.6 * ΔnDCG@10，当 ΔnDCG@10 = 0.10 时，ΔRecall@5 = 0.06，与 N145 声称的 5-8 个百分点一致

## Corrected Claim

在特定实验条件下，观察到nDCG@10提升0.10伴随Recall@5提升约0.06，但这并非通用线性换算关系，不同数据集和任务中该比例会有显著波动。

## Evidence

[质询]nDCG与Recall之间不存在通用的固定线性换算系数（0.6），该比例高度依赖于数据集分布、查询难度及排序算法特性，将其作为通用换算关系缺乏理论或实证基础。 | 经验事实，逻辑自洽但缺来源支持；nDCG与Recall无固定线性关系，系数0.6为特定场景下的拟合值而非普适常数。
