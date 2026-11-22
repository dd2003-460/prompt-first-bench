# N203: 成交量损失项 ΔQ 的量化公式：ΔQ = Q_old × (ΔCVR / (1 + ΔCVR))，其中 ΔCVR 为标签警示引起的转化率相对下降幅度（例如 -1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

成交量损失项 ΔQ 的量化公式：ΔQ = Q_old × (ΔCVR / (1 + ΔCVR))，其中 ΔCVR 为标签警示引起的转化率相对下降幅度（例如 -10% 至 -15%），需基于 N18 的 C_search 降低幅度反推或独立估算。

## Corrected Claim

成交量损失项 ΔQ 的量化公式：ΔQ = Q_old × (ΔCVR / (1 + ΔCVR))，其中 ΔCVR 为标签警示引起的转化率相对下降幅度（例如 -10% 至 -15%），需基于 N18 的 C_search 降低幅度反推或独立估算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔQ = Q_old × (ΔCVR / (1 + ΔCVR)) 在数学上等价于 Q_new - Q_old（其中 Q_new = Q_old × (1 + ΔCVR)），量纲一致，逻辑自洽。

## Search Query

conversion rate elasticity price warning label second hand market
