# N100: 自建带宽总成本修正公式：C_bw_total = Σ(B_pop_i * P_bw_i) + C_cross_connect + C_bgp_peering，其

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

自建带宽总成本修正公式：C_bw_total = Σ(B_pop_i * P_bw_i) + C_cross_connect + C_bgp_peering，其中C_cross_connect为机房交叉连接费（¥500-2000/月/POP），C_bgp_peering为BGP多线接入费（若需多运营商接入则额外¥2000-5000/月/POP）

## Corrected Claim

自建带宽总成本修正公式：C_bw_total = Σ(B_pop_i * P_bw_i) + C_cross_connect + C_bgp_peering，其中C_cross_connect为机房交叉连接费（¥500-2000/月/POP），C_bgp_peering为BGP多线接入费（若需多运营商接入则额外¥2000-5000/月/POP）

## Evidence

先验知识/题面给定，逻辑校验通过
