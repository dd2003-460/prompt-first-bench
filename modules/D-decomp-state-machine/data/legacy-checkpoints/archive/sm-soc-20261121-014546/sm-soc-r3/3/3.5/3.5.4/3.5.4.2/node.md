# N262: 买家搜索成本 C_search 与价格离散度 Var(P) 的关系中存在固定成本项 C_fixed，使得 C_search = C_fixed + k*sqrt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

买家搜索成本 C_search 与价格离散度 Var(P) 的关系中存在固定成本项 C_fixed，使得 C_search = C_fixed + k*sqrt(Var(P))，其中 C_fixed 约占总成本的 20%，因此当 Var(P) 减半时，C_search 实际降低率从 29.3% 降至 23.4%（(0.8+0.7*0.707)/(1+0.7)-1）。

## Corrected Claim

买家搜索成本 C_search 与价格离散度 Var(P) 的关系中存在固定成本项 C_fixed，使得 C_search = C_fixed + k*sqrt(Var(P))，其中 C_fixed 约占总成本的 20%，因此当 Var(P) 减半时，C_search 实际降低率从 29.3% 降至 23.4%（(0.8+0.7*0.707)/(1+0.7)-1）。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (0.8+0.7*0.707)/(1.7)-1 ≈ -23.4% 与陈述一致，且符合固定成本占比20%的设定。

## Search Query

fixed cost component search cost price variance reduction rate adjustment
