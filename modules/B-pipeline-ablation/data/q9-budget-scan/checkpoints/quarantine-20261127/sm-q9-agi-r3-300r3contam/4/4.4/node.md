# N22: 针对‘可发表级’标准的量化校验框架：建立包含 50 篇顶刊论文的基准集，定义质量指标 Q_pub = w1*Novelty + w2*Rigor + w3*Cl

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

针对‘可发表级’标准的量化校验框架：建立包含 50 篇顶刊论文的基准集，定义质量指标 Q_pub = w1*Novelty + w2*Rigor + w3*Clarity，通过 LLM-as-a-Judge 评分（Scale 1-10）与人类专家评分的相关系数 ρ > 0.85 来验证自动评估的有效性，否则需调整 Prompt 中的评分细则（如增加‘统计显著性检查’权重至 0.4）。

## Corrected Claim

针对‘可发表级’标准的量化校验框架：建立包含 50 篇顶刊论文的基准集，定义质量指标 Q_pub = w1*Novelty + w2*Rigor + w3*Clarity，通过 LLM-as-a-Judge 评分（Scale 1-10）与人类专家评分的相关系数 ρ > 0.85 来验证自动评估的有效性，否则需调整 Prompt 中的评分细则（如增加‘统计显著性检查’权重至 0.4）。

## Evidence

父节点级核验未通过：不完备（子节点分别聚焦于'指标定义与优化'和'数据基准构建'，两者职责明确且无重叠，正交性良好；但父节点中明确提到的核心验证步骤——'LLM评分与人类专家评分的相关系数计算及Prompt迭代调整机制'（即评估闭环）未被任何子节点显式覆盖，存在关键缺失。）

## Search Query

LLM as judge evaluation scientific paper quality correlation
