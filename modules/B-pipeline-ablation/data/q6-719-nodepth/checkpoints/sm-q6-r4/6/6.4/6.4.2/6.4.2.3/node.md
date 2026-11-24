# N344: 回源带宽冗余的机会成本：预留但未使用的带宽比例 U_redundant = (B_redundant - B_actual_avg) / B_redundant

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

回源带宽冗余的机会成本：预留但未使用的带宽比例 U_redundant = (B_redundant - B_actual_avg) / B_redundant，其中 B_actual_avg 为平均回源带宽；若 U_redundant > 30%，则建议采用弹性带宽计费模式（按小时付费）替代固定预留，成本降低幅度 = U_redundant * (P_fixed - P_elastic)，其中 P_fixed 为固定带宽单价，P_elastic 为弹性带宽单价。

## Corrected Claim

回源带宽冗余的机会成本：预留但未使用的带宽比例 U_redundant = (B_redundant - B_actual_avg) / B_redundant，其中 B_actual_avg 为平均回源带宽；若 U_redundant > 30%，则建议采用弹性带宽计费模式（按小时付费）替代固定预留，成本降低幅度 = U_redundant * (P_fixed - P_elastic)，其中 P_fixed 为固定带宽单价，P_elastic 为弹性带宽单价。

## Evidence

先验知识/题面给定，逻辑校验通过
