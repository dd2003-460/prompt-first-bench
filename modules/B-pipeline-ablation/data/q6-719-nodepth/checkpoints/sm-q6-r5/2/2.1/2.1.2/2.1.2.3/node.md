# N160: L_origin_processing 的源站负载耦合：L_origin_processing = L_base + L_scale × (R_backhaul

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

L_origin_processing 的源站负载耦合：L_origin_processing = L_base + L_scale × (R_backhaul / C_origin_max)，其中 L_base = 10ms，L_scale 为负载弹性系数（通常 5-10ms/100% 负载），当回源率 (1-H) 因故障升高时（如 N110 中的 23.5%），源站负载增加，L_origin_processing 可能从 15ms 升至 30-40ms，需监控源站 CPU/内存利用率。

## Corrected Claim

L_origin_processing 的源站负载耦合：L_origin_processing = L_base + L_scale × (R_backhaul / C_origin_max)，其中 L_base = 10ms，L_scale 为负载弹性系数（通常 5-10ms/100% 负载），当回源率 (1-H) 因故障升高时（如 N110 中的 23.5%），源站负载增加，L_origin_processing 可能从 15ms 升至 30-40ms，需监控源站 CPU/内存利用率。

## Evidence

先验知识/题面给定，逻辑校验通过
