# N81: 建议价区间 [P_min, P_max] 的动态调整机制：静态区间 [P_ref*0.95, P_ref*1.10] 未考虑季节性或供需波动。动态区间应基于近7

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

建议价区间 [P_min, P_max] 的动态调整机制：静态区间 [P_ref*0.95, P_ref*1.10] 未考虑季节性或供需波动。动态区间应基于近7天成交量 Q_7d 调整：若 Q_7d > Q_avg * 1.2（供不应求），P_max 上调 5%；若 Q_7d < Q_avg * 0.8（供过于求），P_min 下调 5%。量化动态调整对卖家采纳率 A_adopt 的影响，假设静态区间 A_adopt=60%，动态区间 A_adopt=75%。

## Corrected Claim

建议价区间 [P_min, P_max] 的动态调整机制：静态区间 [P_ref*0.95, P_ref*1.10] 未考虑季节性或供需波动。动态区间应基于近7天成交量 Q_7d 调整：若 Q_7d > Q_avg * 1.2（供不应求），P_max 上调 5%；若 Q_7d < Q_avg * 0.8（供过于求），P_min 下调 5%。量化动态调整对卖家采纳率 A_adopt 的影响，假设静态区间 A_adopt=60%，动态区间 A_adopt=75%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic pricing recommendation adoption rate e-commerce sellers
