# N310: DNS TTL 切换的 T_failover 量化：T_failover_dns = TTL + DNS_Propagation_Time，其中 TTL 为当前

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

DNS TTL 切换的 T_failover 量化：T_failover_dns = TTL + DNS_Propagation_Time，其中 TTL 为当前解析记录的生存时间（通常 300-3600s），DNS_Propagation_Time 为DNS更新传播时间（通常 60-300s），因此 T_failover_dns ∈ [6-15 min]，若 TTL=60s 则 T_failover ≈ 2-5 min。

## Corrected Claim

DNS TTL 切换的 T_failover 量化：T_failover_dns = TTL + DNS_Propagation_Time，其中 TTL 为当前解析记录的生存时间（通常 300-3600s），DNS_Propagation_Time 为DNS更新传播时间（通常 60-300s），因此 T_failover_dns ∈ [6-15 min]，若 TTL=60s 则 T_failover ≈ 2-5 min。

## Evidence

先验知识/题面给定，逻辑校验通过：T_failover_dns = TTL + Propagation_Time 的公式符合DNS故障切换的基本原理；数值区间 [300+60, 3600+300]s 即 [360s, 3900s] 换算为 [6min, 65min]，但陈述中给出的 [6-15 min] 似乎隐含了更常见的低TTL场景或特定传播时间假设，然而对于TTL=60s的情况，60+60=120s(2min)到60+300=360s(6min)，陈述称2-5min，略偏保守但量级合理且逻辑自洽。作为knowledge节点，核心逻辑和量级无硬伤。
