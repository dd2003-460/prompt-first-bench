# N356: 点击率(CTR)非恒定修正：验证 CTR 是否随价格升高而下降，若 CTR(P) 为减函数，需引入修正项 CTR_ratio = CTR(1.2*P_mkt)/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N113

## Claim

点击率(CTR)非恒定修正：验证 CTR 是否随价格升高而下降，若 CTR(P) 为减函数，需引入修正项 CTR_ratio = CTR(1.2*P_mkt)/CTR(P_mkt) < 1，重新计算有效曝光倍数 R_eff = R_exposure * CTR_ratio。

## Corrected Claim

在CTR随价格升高而下降的假设下，可引入修正项 CTR_ratio = CTR(1.2*P_mkt)/CTR(P_mkt) < 1，重新计算有效曝光倍数 R_eff = R_exposure * CTR_ratio。

## Evidence

[质询]该陈述包含具体的经验性假设（CTR随价格单调递减）和特定的参数设定（1.2倍价格点），这些并非第一性原理可推导的数学或逻辑必然，而是依赖于特定市场环境的经验事实。 | 逻辑自洽：若CTR(P)为减函数，则CTR(1.2*P_mkt) < CTR(P_mkt)，比值小于1，公式推导无误。但作为经验事实，缺乏来源支持其普遍适用性，故降级。

## Search Query

click through rate price sensitivity second-hand goods
