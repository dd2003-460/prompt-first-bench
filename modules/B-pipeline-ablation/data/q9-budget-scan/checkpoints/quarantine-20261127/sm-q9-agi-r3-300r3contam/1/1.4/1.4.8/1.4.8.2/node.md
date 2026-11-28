# N132: 二元判定 {pass/fail} 的量化映射规则：Pass 当且仅当 p_value < α 且 Effect_Size (Cohen's d) > 0.2；F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

二元判定 {pass/fail} 的量化映射规则：Pass 当且仅当 p_value < α 且 Effect_Size (Cohen's d) > 0.2；Fail 当 p_value >= α 或 Effect_Size < 0.2。置信区间计算采用 95% CI，基于 t 分布或非参数 bootstrap 方法。

## Corrected Claim

二元判定 {pass/fail} 的量化映射规则：Pass 当且仅当 p_value < α 且 Effect_Size (Cohen's d) > 0.2；Fail 当 p_value >= α 或 Effect_Size < 0.2。置信区间计算采用 95% CI，基于 t 分布或非参数 bootstrap 方法。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

effect size Cohen's d threshold pass fail criteria confidence interval
