# N24: 干预对平台的净收益量化：ΔRev_platform = Commission * ΔGMV - Subsidy_Cost - Churn_Cost，其中 Chu

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

干预对平台的净收益量化：ΔRev_platform = Commission * ΔGMV - Subsidy_Cost - Churn_Cost，其中 Churn_Cost = ΔChurn_rate * LTV_seller * N_sellers，需估算 ΔChurn_rate 与 LTV_seller 的关系 [待核验]

## Corrected Claim

干预对平台的净收益量化：ΔRev_platform = Commission * ΔGMV - Subsidy_Cost - Churn_Cost，其中 Churn_Cost = ΔChurn_rate * LTV_seller * N_sellers，需估算 ΔChurn_rate 与 LTV_seller 的关系 [待核验]

## Evidence

父节点级核验通过：正交+完备+无冗余（四个子节点分别对应父节点公式中的 ΔGMV、Subsidy_Cost、ΔChurn_rate 和 LTV_seller 四个独立变量，彼此之间没有逻辑重叠或矛盾，且完整覆盖了净收益公式的所有组成部分。）
