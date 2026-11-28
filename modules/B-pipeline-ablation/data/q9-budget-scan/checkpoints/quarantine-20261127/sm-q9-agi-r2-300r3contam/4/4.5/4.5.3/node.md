# N67: 工作点A的人工介入成本修正项 C_human_A = H_rewrite_rate × T_rewrite_min × Wage_hourly/60，其中 H_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点A的人工介入成本修正项 C_human_A = H_rewrite_rate × T_rewrite_min × Wage_hourly/60，其中 H_rewrite_rate 当前估计 >80% 需细化为按错误类型分布（语法错误 30%, 逻辑错误 50%, 事实错误 20%），T_rewrite_min 为平均每次重写耗时（分钟），Wage_hourly 取 $50/hr，若 H_rewrite_rate 实测低于 50% 则工作点A的总成本优势将反超工作点B。

## Corrected Claim

工作点A的人工介入成本修正项 C_human_A = H_rewrite_rate × T_rewrite_min × Wage_hourly/60，其中 H_rewrite_rate 当前估计 >80% 需细化为按错误类型分布（语法错误 30%, 逻辑错误 50%, 事实错误 20%），T_rewrite_min 为平均每次重写耗时（分钟），Wage_hourly 取 $50/hr，若 H_rewrite_rate 实测低于 50% 则工作点A的总成本优势将反超工作点B。

## Evidence

先验知识/题面给定，逻辑校验通过
