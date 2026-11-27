# N89: W8A8 相比 W8A16 的额外精度损失来源：激活值 INT8 量化引入的误差幅度，通常表现为 PPL 额外增加 0.1-0.5 或基准得分额外下降 1-3%

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21, N22, N23

## Claim

W8A8 相比 W8A16 的额外精度损失来源：激活值 INT8 量化引入的误差幅度，通常表现为 PPL 额外增加 0.1-0.5 或基准得分额外下降 1-3%，具体取决于校准数据集分布。

## Corrected Claim

W8A8 相比 W8A16 的额外精度损失来源：激活值 INT8 量化引入的误差幅度，通常表现为 PPL 额外增加 0.1-0.5 或基准得分额外下降 1-3%，具体取决于校准数据集分布。

## Evidence

先验知识/题面给定，逻辑校验通过
