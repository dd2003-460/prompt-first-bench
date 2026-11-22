# N239: 共享随机源 R_ltv：用户留存率 retention_rate 受共享随机源 β（即前文定义的成交周期缩短率或搜索成本降低率）影响，β 的波动导致流失率 ch

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N71

## Claim

共享随机源 R_ltv：用户留存率 retention_rate 受共享随机源 β（即前文定义的成交周期缩短率或搜索成本降低率）影响，β 的波动导致流失率 churn_rate 在基准值上下波动，churn_rate = churn_base + k_β * β + ε_churn，其中 k_β 为留存敏感度系数，ε_churn ~ N(0, 0.01²)。

## Corrected Claim

共享随机源 R_ltv：用户留存率 retention_rate 受共享随机源 β（即前文定义的成交周期缩短率或搜索成本降低率）影响，β 的波动导致流失率 churn_rate 在基准值上下波动，churn_rate = churn_base + k_β * β + ε_churn，其中 k_β 为留存敏感度系数，ε_churn ~ N(0, 0.01²)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

customer churn rate sensitivity to transaction speed marketplace
