# N96: 置信度映射函数：买家驱动假设置信度 C_buyer = 0.5 + 0.5 * (f_adjust / 0.7)，其中 f_adjust 为观测到的调整预算比例

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N26

## Claim

置信度映射函数：买家驱动假设置信度 C_buyer = 0.5 + 0.5 * (f_adjust / 0.7)，其中 f_adjust 为观测到的调整预算比例；若 f_adjust < 0.3，则 C_buyer < 0.55，视为弱证据；若 f_adjust > 0.7，则 C_buyer > 0.7，视为强证据；中间值线性插值。

## Corrected Claim

置信度映射函数：买家驱动假设置信度 C_buyer = 0.5 + 0.5 * (f_adjust / 0.7)，其中 f_adjust 为观测到的调整预算比例；若 f_adjust < 0.3，则 C_buyer < 0.55，视为弱证据；若 f_adjust > 0.7，则 C_buyer > 0.7，视为强证据；中间值线性插值。

## Search Query

Confidence mapping function for buyer-driven hypothesis based on behavioral metrics
