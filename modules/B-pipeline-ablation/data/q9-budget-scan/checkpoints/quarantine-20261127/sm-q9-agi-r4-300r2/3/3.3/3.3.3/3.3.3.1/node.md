# N156: 27B 模型在热门领域（CS/AI）的知识覆盖率 C_hot 可通过抽样测试估算：随机抽取 1000 篇近 5 年顶会论文，计算模型能正确复述标题/作者/核心结

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

27B 模型在热门领域（CS/AI）的知识覆盖率 C_hot 可通过抽样测试估算：随机抽取 1000 篇近 5 年顶会论文，计算模型能正确复述标题/作者/核心结论的比例；当前估计 C_hot ≈ 0.85-0.90，故 P_offline_hot ≈ 0.10-0.15

## Corrected Claim

27B 模型在热门领域（CS/AI）的知识覆盖率 C_hot 可通过抽样测试估算；理论上若 C_hot 较高，则 P_offline_hot 较低，但具体数值需依赖实际基准测试结果，当前缺乏可靠来源确认 0.85-0.90 这一区间。

## Evidence

[质询]该陈述包含具体的经验数值（C_hot ≈ 0.85-0.90），这属于特定模型在特定时间点的性能指标，无法从第一性原理或数学公理中严格推导出来，且缺乏公开权威基准测试的直接支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值非第一性原理可推导项）

## Search Query

Qwen 27B factual accuracy benchmark citation recall rate popular domain CS AI
