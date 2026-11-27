# N377: 匹配效率参数 λ_match 的基准值需基于平台历史成交数据中‘估值区间覆盖挂价’的转化频率回归得出，假设 λ_match ≈ 0.5-1.0（单位：1/价格单

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N133, N134, N135

## Claim

匹配效率参数 λ_match 的基准值需基于平台历史成交数据中‘估值区间覆盖挂价’的转化频率回归得出，假设 λ_match ≈ 0.5-1.0（单位：1/价格单位），若该参数缺失，P_deal_tail 的置信区间无法收敛。

## Corrected Claim

匹配效率参数 λ_match 的基准值需基于平台历史成交数据中‘估值区间覆盖挂价’的转化频率回归得出；若该参数缺失，P_deal_tail 的置信区间可能无法收敛。

## Evidence

[质询]该陈述包含具体的经验参数范围（λ_match ≈ 0.5-1.0）和特定的统计推断结论（置信区间无法收敛），属于经验事实而非第一性原理可推导的数学/逻辑恒等式。在缺乏外部来源支持的情况下，无法验证该具体数值范围及统计性质的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

second hand marketplace conversion rate price valuation match efficiency parameter estimation
