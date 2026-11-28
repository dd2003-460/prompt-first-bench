# N13: 假设生成阶段的Prompt模板需包含结构化字段：[Research Question], [Existing Literature Gap], [Hypothe

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

假设生成阶段的Prompt模板需包含结构化字段：[Research Question], [Existing Literature Gap], [Hypothesis Statement], [Testable Prediction]，其中[Existing Literature Gap]需通过向量数据库检索Top-K=5相关论文摘要注入，以减少幻觉率

## Corrected Claim

假设生成阶段的Prompt模板需包含结构化字段：[Research Question], [Existing Literature Gap], [Hypothesis Statement], [Testable Prediction]，其中[Existing Literature Gap]需通过向量数据库检索相关论文摘要注入，以减少幻觉率

## Evidence

[质询]Top-K=5 是一个具体的经验参数，缺乏普适的理论依据或广泛共识支持其能显著减少幻觉率，不同场景下最优 K 值可能不同。 | 先验知识/题面给定，逻辑校验通过，但 Top-K=5 为经验事实，缺来源直接支持，故降级。
