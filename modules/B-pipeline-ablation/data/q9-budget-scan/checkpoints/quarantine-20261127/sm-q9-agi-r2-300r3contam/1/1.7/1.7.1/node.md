# N48: 置信度阈值的校准参数：使用 200 条带人工标注 Ground Truth 的样本计算 ROC 曲线，选取 F1-score 最大化的点作为阈值 τ_opt，预

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N19

## Claim

置信度阈值的校准参数：使用 200 条带人工标注 Ground Truth 的样本计算 ROC 曲线，选取 F1-score 最大化的点作为阈值 τ_opt，预期 τ_opt 在 0.65-0.75 之间，替代经验值 0.8。

## Corrected Claim

置信度阈值的校准参数：使用带人工标注 Ground Truth 的样本计算 ROC 曲线，选取 F1-score 最大化的点作为阈值 τ_opt，替代经验值 0.8。

## Evidence

[质询]具体数值范围（0.65-0.75）和样本量（200条）属于特定数据集和经验参数，无法从第一性原理推导，且参考来源未提供该具体数值的支持，存在过拟合或特定场景偏差的风险。 | 逻辑自洽（ROC/F1优化是标准做法），但具体阈值区间0.65-0.75为经验事实，来源[1][2][3]仅讨论阈值调优方法论，未提供该具体数值支持，故降级。

## Search Query

LLM confidence calibration ROC curve threshold optimization F1 score

## Retrieval Sources

- {'url': 'https://blog.csdn.net/MorganiteEagle55/article/details/156869999&rut=b66ae638b040cf3dc2c8b3a9a6333cd86e07207c06d253e5d6b7a55abfe6a59f', 'type': 'ddg', 'title': '异常检测场景：分类模型置信度阈值调优手册 - Csdn博客'}
- {'url': 'https://blog.csdn.net/gitblog_00209/article/details/151076655&rut=666c28f9128657806336cd368005a86cd1f9ad37cc6d6fd1a2c7e371a9c0d9d6', 'type': 'ddg', 'title': '告别一刀切!Cleanlab类别置信阈值计算指南：让每个标签判断更精准-CSDN博客'}
- {'url': 'https://developer.aliyun.com/article/1607626&rut=9c59af4a1dcfed0abb41e2d539df502bd86b09834befcb63d57c13a8e02083b6', 'type': 'ddg', 'title': '详解机器学习中的置信度阈值confidence_threshold如何筛选模型预测结果-开发者社区-阿里云'}
