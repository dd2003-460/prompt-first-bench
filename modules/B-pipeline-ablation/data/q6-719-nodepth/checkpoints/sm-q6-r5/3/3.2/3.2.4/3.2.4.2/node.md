# N232: 自建POP回源流量成本 C_bw_origin_self = Traffic_out_daily * (1-H) * P_backhaul，其中 P_backh

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N73

## Claim

自建POP回源流量成本 C_bw_origin_self = Traffic_out_daily * (1-H) * P_backhaul，其中 P_backhaul 为运营商专线/骨干网单价（通常¥0.2-0.4/GB，约为公网出网价的1/3-1/5），计算得月成本约 ¥936-1,872，显著低于公有云方案。

## Corrected Claim

自建POP回源流量成本 C_bw_origin_self = Traffic_out_daily * (1-H) * P_backhaul，其中 P_backhaul 为运营商专线/骨干网单价（通常¥0.2-0.4/GB，约为公网出网价的1/3-1/5），计算得月成本约 ¥936-1,872，显著低于公有云方案。

## Evidence

先验知识/题面给定，逻辑校验通过
