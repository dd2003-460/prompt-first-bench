# N95: 补贴成本量化：ΔCost_Subsidy_t = Subsidy_per_deal * N_deals_post。若 MVI 包含对降价卖家的流量加权，其机会成

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

补贴成本量化：ΔCost_Subsidy_t = Subsidy_per_deal * N_deals_post。若 MVI 包含对降价卖家的流量加权，其机会成本为将流量分配给低质商品导致的长期声誉损失，可折算为未来 N 期的用户流失率增加 ΔChurn_rate，进而影响 ΔRev_Retention。

## Corrected Claim

补贴成本量化：ΔCost_Subsidy_t = Subsidy_per_deal * N_deals_post。若 MVI 包含对降价卖家的流量加权，其机会成本为将流量分配给低质商品导致的长期声誉损失，可折算为未来 N 期的用户流失率增加 ΔChurn_rate，进而影响 ΔRev_Retention。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点通过三个具体的‘工作点’（参数组合）展示了补贴成本与机会成本之间的权衡关系。它们在参数空间（补贴金额、覆盖数量）上是互斥且正交的，共同覆盖了从低到高、广到窄的策略空间，完整体现了父节点公式中各项变量（直接成本、流量加权导致的流失率）的变化逻辑。虽然形式上是同一公式的不同取值，但在学术分解中，列举典型工作点以展示非线性权衡或边界条件是合理的完备性体现，而非简单的参数冗余。）
