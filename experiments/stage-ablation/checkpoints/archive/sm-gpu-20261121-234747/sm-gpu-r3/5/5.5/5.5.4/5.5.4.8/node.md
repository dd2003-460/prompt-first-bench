# N414: FID 分数计算中使用的嵌入模型选择对结果的影响：需明确使用 CLIP ViT-L/14 还是其他文本嵌入模型（如 Sentence-BERT），不同嵌入空间会

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N134, N135, N136

## Claim

FID 分数计算中使用的嵌入模型选择对结果的影响：需明确使用 CLIP ViT-L/14 还是其他文本嵌入模型（如 Sentence-BERT），不同嵌入空间会导致 FID 绝对值差异，但 ΔFID 的相对趋势应保持一致

## Corrected Claim

FID 分数计算中使用的嵌入模型选择对结果的影响：需明确使用 CLIP ViT-L/14 还是其他文本嵌入模型（如 Sentence-BERT），不同嵌入空间会导致 FID 绝对值差异，但 ΔFID 的相对趋势应保持一致

## Evidence

先验知识/题面给定，逻辑校验通过：FID 基于特征空间分布距离，嵌入模型改变特征空间几何结构，绝对值不可比，但相对变化趋势（ΔFID）在模型性能提升时通常保持一致，符合生成模型评估的基本原理。
