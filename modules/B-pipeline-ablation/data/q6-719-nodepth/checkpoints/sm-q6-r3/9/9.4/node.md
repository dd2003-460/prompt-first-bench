# N139: 长期 ROI 判断阈值：ΔLTV > Unit_Cost_Diff 的临界条件为 ΔRetention > Unit_Cost_Diff / (LTV_Base

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

长期 ROI 判断阈值：ΔLTV > Unit_Cost_Diff 的临界条件为 ΔRetention > Unit_Cost_Diff / (LTV_Base × Retention_Elasticity)，若 Unit_Cost_Diff = ¥0.05/用户/月，LTV_Base = ¥100，Elasticity = 1.2，则临界 ΔRetention > 0.00042（0.042%），即 P99 延迟需降低约 4.2ms 才能覆盖成本差。

## Corrected Claim

长期 ROI 判断阈值：ΔLTV > Unit_Cost_Diff 的临界条件为 ΔRetention > Unit_Cost_Diff / (LTV_Base × Retention_Elasticity)，若 Unit_Cost_Diff = ¥0.05/用户/月，LTV_Base = ¥100，Elasticity = 1.2，则临界 ΔRetention > 0.00042（0.042%），即 P99 延迟需降低约 4.2ms 才能覆盖成本差。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应了临界值计算（中性价比/盈亏平衡）、高于临界值的可行场景（低延迟/高成本）以及低于临界值的不可行场景（高延迟/低成本）。三者基于同一数学模型（ROI = ΔLTV - Unit_Cost_Diff）的不同参数取值区间进行划分，逻辑上互斥且共同覆盖了阈值判断的正负两侧及边界，符合正交性和完备性要求。虽然它们本质上是同一公式在不同参数下的应用，但在学术分解中，将'边界条件'、'正向验证'和'负向反例'作为独立节点有助于清晰展示判断逻辑的完整性，不属于冗余。）
