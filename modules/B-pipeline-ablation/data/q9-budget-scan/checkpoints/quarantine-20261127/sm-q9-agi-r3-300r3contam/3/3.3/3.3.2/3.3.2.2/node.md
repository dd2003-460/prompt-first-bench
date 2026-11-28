# N154: 语义相似度阈值 θ 的设定遵循 ROC 曲线权衡：设虚构引用的余弦相似度分布为 G_fake ~ N(μ_fake, σ_fake²)，真实引用为 G_real

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

语义相似度阈值 θ 的设定遵循 ROC 曲线权衡：设虚构引用的余弦相似度分布为 G_fake ~ N(μ_fake, σ_fake²)，真实引用为 G_real ~ N(μ_real, σ_real²)；最优阈值 θ* = (μ_fake + μ_real)/2 + (σ_fake² - σ_real²)/(μ_fake - μ_real) * ln(σ_fake/σ_real)，此时最小化 F1 损失

## Corrected Claim

语义相似度阈值 θ 的设定遵循 ROC 曲线权衡：设虚构引用的余弦相似度分布为 G_fake ~ N(μ_fake, σ_fake²)，真实引用为 G_real ~ N(μ_real, σ_real²)；最优阈值 θ* = (μ_fake + μ_real)/2 + (σ_fake² - σ_real²)/(μ_fake - μ_real) * ln(σ_fake/σ_real)，此时最小化 F1 损失

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是双正态分布下基于贝叶斯决策理论（最小化0-1损失或特定代价矩阵）推导出的最优分类阈值解析解，数学推导严谨，量纲一致。

## Search Query

optimal threshold cosine similarity hallucinated citation detection ROC curve formula
