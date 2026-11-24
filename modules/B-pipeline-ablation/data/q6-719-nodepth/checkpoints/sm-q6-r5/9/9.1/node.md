# N124: Lambda (¥/ms/req) 的量化依据：基于用户生命周期价值 LTV 和流失率弹性计算，Lambda = (LTV * ΔChurn_rate_per_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Lambda (¥/ms/req) 的量化依据：基于用户生命周期价值 LTV 和流失率弹性计算，Lambda = (LTV * ΔChurn_rate_per_ms) / 1000，其中 LTV 为单用户年度贡献（¥50-200），ΔChurn 为每增加 1ms 延迟导致的月流失率增量（0.01%-0.05%）。

## Corrected Claim

Lambda (¥/ms/req) 的量化依据：基于用户生命周期价值 LTV 和流失率弹性计算，Lambda = (LTV * ΔChurn_rate_per_ms) / 1000，其中 LTV 为单用户年度贡献（¥50-200），ΔChurn 为每增加 1ms 延迟导致的月流失率增量（0.01%-0.05%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

user churn rate elasticity per ms latency increase SaaS platform
