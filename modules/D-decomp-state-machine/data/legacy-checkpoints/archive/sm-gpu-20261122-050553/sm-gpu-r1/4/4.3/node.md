# N22: 散热与空间隐含成本 (C_infra) = (P_avg_W × T_hours × E_price) × (1 + 1/COP)；COP 为制冷系统能效比（家

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

散热与空间隐含成本 (C_infra) = (P_avg_W × T_hours × E_price) × (1 + 1/COP)；COP 为制冷系统能效比（家用空调约 3.0, 数据中心约 1.5-2.0），反映额外制冷能耗；多卡方案因散热密度高，COP 可能下降，需修正。

## Corrected Claim

散热与空间隐含成本 (C_infra) = (P_avg_W × T_hours × E_price) × (1 + 1/COP)；COP 为制冷系统能效比（家用空调约 3.0, 数据中心约 1.5-2.0），反映额外制冷能耗；多卡方案因散热密度高，COP 可能下降，需修正。

## Evidence

先验知识/题面给定，逻辑校验通过
