# N206: 点击率下降 ΔCTR 的量化公式：ΔCTR = CTR_old × (ΔC_search / C_search_old)，其中 ΔC_search 为标签警示带

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N67

## Claim

点击率下降 ΔCTR 的量化公式：ΔCTR = CTR_old × (ΔC_search / C_search_old)，其中 ΔC_search 为标签警示带来的额外认知负荷或负面信号效应，假设标签导致 CTR 相对下降 5%-10%，需基于 N18 的 C_search 变化幅度校准。

## Corrected Claim

点击率下降 ΔCTR 可近似量化为 ΔCTR ≈ CTR_old × (ΔC_search / C_search_old)，其中 ΔC_search 代表标签警示带来的额外认知负荷或负面信号效应。该公式为线性近似模型，实际 CTR 相对下降幅度（如 5%-10%）需基于具体场景下 N18 的 C_search 变化幅度及用户行为数据校准，不可直接套用固定比例。

## Evidence

[质询]公式将复杂的用户行为变化（CTR下降）简化为单一变量（认知负荷/负面信号）的线性比例关系，忽略了用户偏好、标签内容具体语义、页面布局等多重混杂因素，且5%-10%的假设缺乏普适性实证支持，属于过度简化的经验估算。 | 先验知识/题面给定，逻辑校验通过（量纲一致，线性近似在局部小变化下合理），但作为经验事实缺乏外部来源直接支持，且模型简化程度较高，故降级。

## Search Query

click through rate impact price warning label user behavior study
