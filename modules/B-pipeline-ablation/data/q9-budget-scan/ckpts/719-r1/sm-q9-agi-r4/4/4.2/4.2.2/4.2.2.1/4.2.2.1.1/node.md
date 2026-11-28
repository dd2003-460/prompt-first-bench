# N596: BERT-base-nli 模型在 100 个标注样本上的 ROC 曲线构建：计算每个样本的 cosine similarity 得分与真实标签（正确/错误）的

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

BERT-base-nli 模型在 100 个标注样本上的 ROC 曲线构建：计算每个样本的 cosine similarity 得分与真实标签（正确/错误）的混淆矩阵，以 F1-score 为目标函数，在 0.80-0.90 区间内以 0.01 步长搜索最优阈值 θ*，使得 F1(θ*) 最大化

## Corrected Claim

BERT-base-nli 模型在 100 个标注样本上的 ROC 曲线构建：计算每个样本的 cosine similarity 得分与真实标签（正确/错误）的混淆矩阵，以 F1-score 为目标函数，在 0.80-0.90 区间内以 0.01 步长搜索最优阈值 θ*，使得 F1(θ*) 最大化

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

BERT nli cosine similarity ROC curve threshold calibration F1 score
