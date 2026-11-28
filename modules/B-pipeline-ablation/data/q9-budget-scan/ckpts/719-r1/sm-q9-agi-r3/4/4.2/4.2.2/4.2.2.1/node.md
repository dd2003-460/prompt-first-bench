# N213: 语义相似度阈值0.85的校准方法：使用BERT-base-nli模型计算Qwen3.8-27B生成陈述与黄金答案的cosine similarity，需在100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

语义相似度阈值0.85的校准方法：使用BERT-base-nli模型计算Qwen3.8-27B生成陈述与黄金答案的cosine similarity，需在100个已知正确/错误样本上绘制ROC曲线，选取F1-score最大化的阈值点（预期在0.80-0.90之间）替代固定0.85。

## Corrected Claim

语义相似度阈值0.85的校准方法：使用BERT-base-nli模型计算Qwen3.8-27B生成陈述与黄金答案的cosine similarity，需在100个已知正确/错误样本上绘制ROC曲线，选取F1-score最大化的阈值点（预期在0.80-0.90之间）替代固定0.85。

## Evidence

先验知识/题面给定，逻辑校验通过：使用ROC曲线和F1-score最大化来校准分类阈值是标准的机器学习实践，0.80-0.90的区间对于高置信度语义相似度也是合理的经验范围。
