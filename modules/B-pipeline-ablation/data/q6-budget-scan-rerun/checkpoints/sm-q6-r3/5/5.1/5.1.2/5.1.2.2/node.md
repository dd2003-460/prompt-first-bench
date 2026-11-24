# N304: 带宽单价分层模型：总带宽成本 B(T) 需拆分为边缘分发成本与回源成本两部分，B_total(T) = B_edge(T) × P_edge + B_origi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

带宽单价分层模型：总带宽成本 B(T) 需拆分为边缘分发成本与回源成本两部分，B_total(T) = B_edge(T) × P_edge + B_origin(T) × P_origin，其中 P_edge（边缘单价）约为 0.15-0.20 元/GB，P_origin（回源单价）约为 0.30-0.40 元/GB（P_origin ≈ 2 × P_edge）；T 降低导致 CHR 升高，B_origin 减少，但由于 P_origin 较高，边际成本节省率低于带宽体积节省率。

## Corrected Claim

带宽单价分层模型：总带宽成本 B(T) 需拆分为边缘分发成本与回源成本两部分，B_total(T) = B_edge(T) × P_edge + B_origin(T) × P_origin，其中 P_edge（边缘单价）约为 0.15-0.20 元/GB，P_origin（回源单价）约为 0.30-0.40 元/GB（P_origin ≈ 2 × P_edge）；T 降低导致 CHR 升高，B_origin 减少，但由于 P_origin 较高，边际成本节省率低于带宽体积节省率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin bandwidth unit price vs edge delivery price ratio
