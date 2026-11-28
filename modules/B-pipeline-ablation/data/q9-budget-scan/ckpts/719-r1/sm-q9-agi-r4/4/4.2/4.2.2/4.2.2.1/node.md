# N213: 语义相似度阈值0.85的校准方法：使用BERT-base-nli模型计算Qwen3.8-27B生成陈述与黄金答案的cosine similarity，需在100

- **status**: pending
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

父节点级核验未通过：不完备（子节点之间存在轻微的功能重叠（节点1包含ROC构建逻辑，节点2包含数据准备，节点3包含计算细节，彼此正交）。但完备性不足：父节点明确要求‘使用BERT-base-nli模型...计算Qwen3.8-27B生成陈述与黄金答案的cosine similarity’，这暗示了具体的输入构造方式（如Prompt模板、是否包含[CLS] token、如何拼接两个文本等）。现有的三个子节点均未涵盖‘BERT输入预处理/Prompt工程’这一关键步骤，导致无法复现具体的相似度计算过程。）
