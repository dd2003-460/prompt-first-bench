# N205: 工作点B（低过滤比例/高可见性）：假设搜索阈值 T_search = P_market * 1.20，当降价后 P_ask_new > T_search 时商品

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

工作点B（低过滤比例/高可见性）：假设搜索阈值 T_search = P_market * 1.20，当降价后 P_ask_new > T_search 时商品不可见，计算 P(invisible) = P(P_ask_new > 1.20 * P_market | P_ask_old ∈ [1.15, 1.25]) ≈ 0.45，界定 D_real_min = 0.6 * 0.45 = 0.27，作为可见性缺失的下界保守估计。

## Corrected Claim

工作点B（低过滤比例/高可见性）：假设搜索阈值 T_search = P_market * 1.20，当降价后 P_ask_new > T_search 时商品不可见，计算 P(invisible) = P(P_ask_new > 1.20 * P_market | P_ask_old ∈ [1.15, 1.25]) ≈ 0.45，界定 D_real_min = 0.6 * 0.45 = 0.27，作为可见性缺失的下界保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price threshold filtering in online marketplace search
