# N185: 效应量 d 的标准化定义公式为 d = (μ_1 - μ_2) / σ_pooled，其中 σ_pooled = sqrt(((n_1-1)s_1^2 + (n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

效应量 d 的标准化定义公式为 d = (μ_1 - μ_2) / σ_pooled，其中 σ_pooled = sqrt(((n_1-1)s_1^2 + (n_2-1)s_2^2)/(n_1+n_2-2))；在科研假设生成阶段，若模型无法基于文献提供 σ 的估计值，则默认为未知，需触发先验方差查询工具

## Corrected Claim

效应量 d 的标准化定义公式为 d = (μ_1 - μ_2) / σ_pooled，其中 σ_pooled = sqrt(((n_1-1)s_1^2 + (n_2-1)s_2^2)/(n_1+n_2-2))；在科研假设生成阶段，若模型无法基于文献提供 σ 的估计值，则默认为未知，需触发先验方差查询工具

## Evidence

先验知识/题面给定，逻辑校验通过：Cohen's d 的标准定义及合并标准差公式符合统计学第一性原理，后续关于假设生成阶段的流程描述逻辑自洽。
