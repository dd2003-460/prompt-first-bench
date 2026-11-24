# N498: 源站出口带宽争用因子 Contention_Factor：当并发回源请求数 N_concurrent 增加时，单请求有效带宽 Bandwidth_eff = B

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N167

## Claim

源站出口带宽争用因子 Contention_Factor：当并发回源请求数 N_concurrent 增加时，单请求有效带宽 Bandwidth_eff = Bandwidth_nominal / N_concurrent × (1 - Loss_Rate)，若源站 10Gbps 出口同时服务 10 个边缘节点，单节点有效带宽降至 1Gbps，传输 5MB 对象时间从 4ms 升至 40ms

## Corrected Claim

源站出口带宽争用因子 Contention_Factor：当并发回源请求数 N_concurrent 增加时，单请求有效带宽 Bandwidth_eff = Bandwidth_nominal / N_concurrent × (1 - Loss_Rate)，若源站 10Gbps 出口同时服务 10 个边缘节点，单节点有效带宽降至 1Gbps，传输 5MB 对象时间从 4ms 升至 40ms

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps/10=1Gbps，5MB/1Gbps=40ms，计算自洽

## Search Query

bandwidth contention concurrent requests effective throughput degradation
