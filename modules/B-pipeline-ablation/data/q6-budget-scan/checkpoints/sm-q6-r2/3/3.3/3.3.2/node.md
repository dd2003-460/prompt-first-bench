# N106: 源站负载成本增量：ΔC_origin_server = (V_download_total * R_origin / s_avg) * C_cpu_per_re

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

源站负载成本增量：ΔC_origin_server = (V_download_total * R_origin / s_avg) * C_cpu_per_req，其中C_cpu_per_req为源站处理单请求的CPU/内存成本（估算约¥0.001-0.005/req），R_origin每增加1%导致源站QPS增加约 (2TB/s_avg)/100

## Corrected Claim

源站负载成本增量：ΔC_origin_server = (V_download_total * R_origin / s_avg) * C_cpu_per_req，其中C_cpu_per_req为源站处理单请求的CPU/内存成本（估算约¥0.001-0.005/req），R_origin每增加1%导致源站QPS增加约 (2TB/s_avg)/100

## Evidence

先验知识/题面给定，逻辑校验通过
