# N79: LLM-as-a-Judge 与人类专家评分的相关性校验公式：收集 N_experts=5 名领域专家对 N_samples=50 份 AI 生成论文的评分矩阵

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

LLM-as-a-Judge 与人类专家评分的相关性校验公式：收集 N_experts=5 名领域专家对 N_samples=50 份 AI 生成论文的评分矩阵 H (50x3) 与 AI 评分矩阵 J (50x3)，计算 Pearson 相关系数 r = Cov(H, J) / (Std(H)*Std(J))，要求 r > 0.85 方可启用自动评估，否则需调整 Prompt 模板。

## Corrected Claim

LLM-as-a-Judge 与人类专家评分的相关性校验公式：收集 N_experts=5 名领域专家对 N_samples=50 份 AI 生成论文的评分矩阵 H (50x3) 与 AI 评分矩阵 J (50x3)，计算 Pearson 相关系数 r = Cov(H, J) / (Std(H)*Std(J))，要求 r > 0.85 方可启用自动评估，否则需调整 Prompt 模板。

## Evidence

先验知识/题面给定，逻辑校验通过
