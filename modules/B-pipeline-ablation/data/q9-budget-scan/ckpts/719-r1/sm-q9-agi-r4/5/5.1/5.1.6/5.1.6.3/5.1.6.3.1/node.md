# N673: 基准测试集的复杂度评分定义：Complexity_Score (1-10) 基于任务所需推理步数、检索文档数量及逻辑链条长度加权计算，例如：Score = 0.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N245

## Claim

基准测试集的复杂度评分定义：Complexity_Score (1-10) 基于任务所需推理步数、检索文档数量及逻辑链条长度加权计算，例如：Score = 0.4×Steps + 0.3×Docs + 0.3×LogicDepth，需确保 100 个样本在 1-10 区间均匀分布

## Corrected Claim

基准测试集的复杂度评分定义：Complexity_Score (1-10) 基于任务所需推理步数、检索文档数量及逻辑链条长度加权计算，例如：Score = 0.4×Steps + 0.3×Docs + 0.3×LogicDepth，需确保 100 个样本在 1-10 区间均匀分布

## Evidence

先验知识/题面给定，逻辑校验通过
