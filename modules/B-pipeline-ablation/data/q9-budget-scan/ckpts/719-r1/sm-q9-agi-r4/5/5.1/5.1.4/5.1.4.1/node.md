# N237: Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh)

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh) × 0.8，其中 Power_Station_W 为 N66/N81 确定的实测稳态整机功耗（取值范围 750W-1000W），Price_per_kWh 为 $0.15/kWh，计算得单日本地能耗成本区间为 $2.16 - $3.00

## Corrected Claim

Cost_Local_80% 的具体计算公式为 Cost_Local_80% = (Power_Station_W × 24h × Price_per_kWh) × 0.8，其中 Power_Station_W 为 N66/N81 确定的实测稳态整机功耗（取值范围 750W-1000W），Price_per_kWh 为 $0.15/kWh，计算得单日本地能耗成本区间为 $2.16 - $3.00

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式中‘电价(Price_per_kWh)’和‘功耗(Power_Station_W)’两个变量在不同极端取值下的计算实例，而非独立的逻辑维度，因此存在严重的结构冗余（同一公式的多个案例）。此外，父节点明确给出了基于 $0.15/kWh 和 750-1000W 的基础成本区间 ($2.16-$3.00)，但子节点仅讨论了电价变化的上下限，完全缺失了对‘功耗’变量敏感性的分析（例如在 $0.15 电价下，功耗从 750W 变到 1000W 的影响），导致对父节点关键参数的覆盖不完备。）
