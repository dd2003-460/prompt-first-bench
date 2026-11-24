# N701: 云对象存储5年TCO中网络出口带宽的累计成本 C_egress_5y = Σ_t [V(t) * r_egress_daily * 365 * 1024 * P

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N290

## Claim

云对象存储5年TCO中网络出口带宽的累计成本 C_egress_5y = Σ_t [V(t) * r_egress_daily * 365 * 1024 * P_gb_out]，其中 V(t)为第t年数据量(TB)，r_egress_daily为日均出口流量占数据量比例(需根据业务场景设定，如0.01)，P_gb_out为出口单价(¥/GB)。

## Corrected Claim

云对象存储5年TCO中网络出口带宽的累计成本 C_egress_5y = Σ_t [V(t) * r_egress_daily * 365 * 1024 * P_gb_out]，其中 V(t)为第t年数据量(TB)，r_egress_daily为日均出口流量占数据量比例(需根据业务场景设定，如0.01)，P_gb_out为出口单价(¥/GB)。

## Evidence

先验知识/题面给定，逻辑校验通过
